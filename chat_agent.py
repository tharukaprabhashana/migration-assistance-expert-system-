from __future__ import annotations
from dataclasses import dataclass, asdict, replace
from typing import Optional, Dict, Any, Tuple, List
import os
import re
import json

# -----------------------------
# Country and policy helpers
# -----------------------------
IELTS_COUNTRIES = {"Canada", "Australia", "New Zealand", "United Kingdom"}

COUNTRY_TO_CURRENCY: Dict[str, str] = {
    "Canada": "CAD",
    "Australia": "AUD",
    "New Zealand": "NZD",
    "Singapore": "SGD",
    "Japan": "JPY",
    "United Kingdom": "GBP",
    "United States": "USD",
    "Germany": "EUR",
    "Netherlands": "EUR",
    "France": "EUR",
    "Italy": "EUR",
    "Norway": "NOK",
    "Finland": "EUR",
    "Sweden": "SEK",
    "Denmark": "DKK",
    "Latvia": "EUR",
    "Saudi Arabia": "SAR",
    "United Arab Emirates": "AED",
}

RECOGNIZED_COUNTRIES = set(COUNTRY_TO_CURRENCY.keys())


def requires_ielts(country: Optional[str]) -> bool:
    return bool(country) and country in IELTS_COUNTRIES


# -----------------------------
# Slot container (dataclass, no hard deps)
# -----------------------------
@dataclass
class PersonSlots:
    role: Optional[str] = None
    age: Optional[int] = None
    education: Optional[str] = None
    degree_field: Optional[str] = None
    occupation: Optional[str] = None
    experience_years: Optional[int] = None
    ielts: Optional[float] = None
    salary_local: Optional[int] = None
    salary_currency: Optional[str] = None
    current_country: Optional[str] = None
    preferred_country: Optional[str] = None
    marital_status: Optional[str] = None
    has_spouse: Optional[bool] = None
    spouse_education: Optional[str] = None
    spouse_is_working: Optional[bool] = None
    num_children: Optional[int] = None

    def dict(self) -> Dict[str, Any]:
        return asdict(self)

    def merge(self, other: "PersonSlots") -> "PersonSlots":
        base = self.dict()
        for k, v in other.dict().items():
            if v is not None:
                base[k] = v
        return PersonSlots(**base)

    def validate(self) -> "PersonSlots":
        # Clamp/normalize simple ranges; ignore errors but keep safe values
        if self.age is not None:
            if not (18 <= int(self.age) <= 70):
                return replace(self, age=None)
        if self.ielts is not None:
            try:
                val = float(self.ielts)
            except Exception:
                val = -1.0
            if not (0.0 <= val <= 9.0):
                return replace(self, ielts=None)
        if self.experience_years is not None:
            if not (0 <= int(self.experience_years) <= 50):
                return replace(self, experience_years=None)
        if self.num_children is not None:
            if not (0 <= int(self.num_children) <= 10):
                return replace(self, num_children=None)
        return self

    def is_complete(self) -> bool:
        required = [
            "role", "age", "education", "degree_field", "occupation",
            "experience_years", "current_country", "preferred_country",
            "marital_status", "salary_local",
        ]
        if requires_ielts(self.preferred_country):
            required.append("ielts")
        if (self.marital_status or "").lower() == "married":
            required.extend(["has_spouse", "spouse_education", "spouse_is_working", "num_children"])
        return all(getattr(self, k) is not None for k in required)


# -----------------------------
# Normalization and heuristics
# -----------------------------
def normalize_country(text: Optional[str]) -> Optional[str]:
    """Normalize to a recognized country name.
    Accepts exact names and common aliases (e.g., UK -> United Kingdom, USA -> United States).
    """
    if not text:
        return None
    raw = text.strip()
    # Exact match first
    for c in RECOGNIZED_COUNTRIES:
        if raw == c:
            return c
    # Alias mapping (case-insensitive)
    alias_map = {
        "UK": "United Kingdom",
        "U.K.": "United Kingdom",
        "ENGLAND": "United Kingdom",
        "BRITAIN": "United Kingdom",
        "GREAT BRITAIN": "United Kingdom",
        "UAE": "United Arab Emirates",
        "U.A.E.": "United Arab Emirates",
        "EMIRATES": "United Arab Emirates",
        "KSA": "Saudi Arabia",
        "USA": "United States",
        "U.S.": "United States",
        "US": "United States",
        "AMERICA": "United States",
        "UNITED STATES OF AMERICA": "United States",
        "NZ": "New Zealand",
        "HOLLAND": "Netherlands",
    }
    key = raw.upper()
    mapped = alias_map.get(key)
    if mapped and mapped in RECOGNIZED_COUNTRIES:
        return mapped
    return None


def heuristic_extract(user_text: str) -> Dict[str, Any]:
    """Rule-based extraction is intentionally disabled to honor the design request.
    We rely on LLM extraction; this returns no fields.
    """
    return {}


# -----------------------------
# Optional LangChain-based extractor (fully optional)
# -----------------------------
try:
    # Load environment variables from a local .env file if present
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()  # safe to call multiple times; no-op if .env missing
except Exception:
    pass

try:
    from langchain_openai import ChatOpenAI  # type: ignore
except Exception:  # pragma: no cover
    ChatOpenAI = None

try:
    # For structured output
    from pydantic import BaseModel
except Exception:
    BaseModel = None  # type: ignore


def llm_extract(user_text: str, missing_fields: Optional[List[str]] = None, last_question: Optional[str] = None) -> PersonSlots:
    """Extract fields with an LLM using structured output. Fails fast if not configured."""
    if ChatOpenAI is None or BaseModel is None:
        raise RuntimeError("LLM extraction is required: install langchain-openai and pydantic, and set OPENAI_API_KEY.")

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY not found. Add it to your .env and restart.")

    class LLMSlots(BaseModel):  # type: ignore
        role: Optional[str] = None
        age: Optional[int] = None
        education: Optional[str] = None
        degree_field: Optional[str] = None
        occupation: Optional[str] = None
        experience_years: Optional[int] = None
        ielts: Optional[float] = None
        salary_local: Optional[int] = None
        salary_currency: Optional[str] = None
        current_country: Optional[str] = None
        preferred_country: Optional[str] = None
        marital_status: Optional[str] = None
        has_spouse: Optional[bool] = None
        spouse_education: Optional[str] = None
        spouse_is_working: Optional[bool] = None
        num_children: Optional[int] = None

    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    llm = ChatOpenAI(model=model_name, temperature=0).with_structured_output(LLMSlots)

    hint_missing = ", ".join(missing_fields or []) or "(none)"
    hint_last_q = last_question or "(none)"
    instruction = (
        "Extract migration profile fields as JSON only. Use null when unknown. "
        "Use EXACT country names from this list (no aliases): " + ", ".join(sorted(RECOGNIZED_COUNTRIES)) + ". "
        "If the user's message is brief (e.g., a single number or yes/no), interpret it as an answer to the LAST_QUESTION when reasonable. "
        f"MISSING_FIELDS (for context): {hint_missing}. LAST_QUESTION: {hint_last_q}. "
        "NEVER assume marital status. Only set marital_status if explicitly stated in the user's message; otherwise leave it null. "
        "If explicitly 'married', set marital_status='married' and has_spouse=true. "
        "If explicitly 'single' or 'divorced', set the value accordingly and has_spouse=false. "
        "Do not guess IELTS unless explicitly stated."
    )

    try:
        parsed: LLMSlots = llm.invoke(
            f"{instruction}\n\nMessage: {user_text}"
        )
    except Exception as e:
        raise RuntimeError(f"LLM extraction failed: {e}")

    data = parsed.model_dump()

    # Enforce explicit-only marital status: ignore any inferred value unless user text clearly states it
    try:
        ut = user_text.lower()
    except Exception:
        ut = ""
    explicit_status: Optional[str] = None
    # Clear, explicit mentions
    if re.search(r"\bmarried\b", ut) or re.search(r"\b(spouse|wife|husband)\b", ut):
        explicit_status = "married"
    elif re.search(r"\b(single|unmarried)\b", ut):
        explicit_status = "single"
    elif re.search(r"\b(divorced|separated|widow|widowed)\b", ut):
        explicit_status = "divorced"

    if explicit_status is None:
        # No explicit status in this message: do not set/override marital fields from this turn
        data["marital_status"] = None
        data["has_spouse"] = None
        # Do not touch spouse details; merging keeps prior known values
    else:
        data["marital_status"] = explicit_status
        data["has_spouse"] = True if explicit_status == "married" else False

    # Normalize and coerce
    if data.get("preferred_country"):
        norm = normalize_country(str(data["preferred_country"]))
        if norm:
            data["preferred_country"] = norm
            data["salary_currency"] = COUNTRY_TO_CURRENCY.get(norm)
        else:
            data["preferred_country"] = None
            data["salary_currency"] = None

    if data.get("current_country"):
        # For current country, accept any user-provided country (don't restrict to recognized list).
        # If it matches a known alias or recognized name, normalize; otherwise keep the original string.
        raw_cc = str(data["current_country"]).strip()
        normc = normalize_country(raw_cc)
        data["current_country"] = normc if normc else raw_cc

    # Coerce simple ranges
    try:
        if data.get("age") is not None:
            age = int(data["age"])  # type: ignore
            if not (18 <= age <= 70):
                data["age"] = None
    except Exception:
        data["age"] = None

    try:
        if data.get("ielts") is not None:
            i = float(data["ielts"])  # type: ignore
            if not (0.0 <= i <= 9.0):
                data["ielts"] = None
    except Exception:
        data["ielts"] = None

    try:
        if data.get("experience_years") is not None:
            ey = int(data["experience_years"])  # type: ignore
            if not (0 <= ey <= 50):
                data["experience_years"] = None
    except Exception:
        data["experience_years"] = None

    try:
        if data.get("num_children") is not None:
            nc = int(data["num_children"])  # type: ignore
            if not (0 <= nc <= 10):
                data["num_children"] = None
    except Exception:
        data["num_children"] = None

    return PersonSlots(**data).validate()


# -----------------------------
# Conversational agent (LLM decides next turn)
# -----------------------------

CONV_SYSTEM_PROMPT = (
    "You are a friendly migration consultant. Hold a natural conversation. "
    "Ask at most ONE concise, human question per turn ONLY about fields listed in MISSING_FIELDS. "
    "Never ask about anything not in MISSING_FIELDS. Never repeat the same question twice in a row. If you just asked about a field and the user didn't answer, pick a different missing field or rephrase. "
    "Never assume marital status; only set it when the user explicitly states it. If unknown and listed in MISSING_FIELDS, ask about it. "
    "If MISSING_FIELDS is empty, DO NOT ask questions — acknowledge succinctly and confirm you'll run the assessment. "
    "Skip IELTS questions unless the preferred country requires IELTS (Canada, Australia, New Zealand, United Kingdom). "
    "If the user is single or divorced, avoid spouse questions. If married, you may ask briefly about spouse education and employment. "
    "Your goal is to help the user complete their profile so an expert system can evaluate eligibility. "
    "Write short messages (1–2 sentences)."
)


def _missing_fields_for(state: PersonSlots) -> List[str]:
    """Return the list of missing keys given current state and policy (IELTS/spouse)."""
    required = [
        "role", "age", "education", "degree_field", "occupation",
        "experience_years", "current_country", "preferred_country", "marital_status",
    ]
    if requires_ielts(state.preferred_country):
        required.append("ielts")
    required.append("salary_local")
    if (state.marital_status or "").lower() == "married":
        required.extend(["spouse_education", "spouse_is_working", "num_children"])
    return [k for k in required if getattr(state, k) is None]


def chat_generate_reply(history: List[Dict[str, str]], state: PersonSlots) -> str:
    """Let the LLM generate the assistant's next natural message using the conversation history and known state.
    This is NOT a rule-based planner; LLM chooses what to ask/say. We provide known facts for grounding.
    """
    if ChatOpenAI is None:
        raise RuntimeError("LLM chat is required: install langchain-openai and set OPENAI_API_KEY.")
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY not found. Add it to your .env and restart.")

    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    llm = ChatOpenAI(model=model_name, temperature=0.3)

    facts_lines = []
    for k, v in state.dict().items():
        if v is not None and v != "":
            facts_lines.append(f"- {k}: {v}")
    facts = "\n".join(facts_lines) or "- none yet"

    missing = _missing_fields_for(state)
    missing_text = ", ".join(missing) if missing else "(none)"

    # Convert history to a simple transcript for context
    transcript = []
    for m in history[-12:]:  # limit context
        role = m.get("role", "user")
        content = m.get("content", "")
        transcript.append(f"{role.upper()}: {content}")
    transcript_text = "\n".join(transcript)

    prompt = (
        f"SYSTEM:\n{CONV_SYSTEM_PROMPT}\n\n"
        f"MISSING_FIELDS: {missing_text}\n\n"
        f"KNOWN FACTS:\n{facts}\n\n"
        f"RECENT CONVERSATION:\n{transcript_text}\n\n"
        "ASSISTANT: Respond naturally based on the conversation, KNOWN FACTS, and MISSING_FIELDS."
    )

    resp = llm.invoke(prompt)
    return resp.content.strip() if hasattr(resp, "content") else str(resp)


def chat_turn(user_text: str, state: PersonSlots, history: List[Dict[str, str]]) -> Tuple[str, PersonSlots, bool]:
    """One chat turn: extract fields from user text, merge into state, and let the LLM craft the next reply.
    Returns (assistant_message, new_state, ready_to_run_engine).
    """
    # 1) Extract fields via LLM (turn-aware)
    # Determine missing before extraction and last assistant question to guide mapping
    missing_before = _missing_fields_for(state)
    last_assistant_msg = next((m for m in reversed(history) if m.get("role") == "assistant"), None)
    last_q = last_assistant_msg.get("content") if last_assistant_msg else None
    extracted = llm_extract(user_text, missing_fields=missing_before, last_question=last_q)
    merged = state.merge(extracted)
    merged = derive(merged)

    # 2) Let LLM decide what to say next (no ordered questioning)
    next_msg = chat_generate_reply(history + [{"role": "user", "content": user_text}], merged)

    # 3) Decide if we can run engine now (minimal logic for completion)
    ready = merged.is_complete()
    return next_msg, merged, ready


# -----------------------------
# Planning next questions
# -----------------------------
QUESTION_TEXT: Dict[str, str] = {
    "preferred_country": "Which country do you plan to migrate to?",
    "role": "What is your role (professional, student, or unemployed)?",
    "age": "What is your age?",
    "education": "What is your highest education level (Diploma, Bachelors, Masters, PhD)?",
    "degree_field": "What is your field of study?",
    "occupation": "What is your current occupation?",
    "experience_years": "How many years of work experience do you have?",
    "current_country": "Which country are you currently living in?",
    "marital_status": "What is your marital status (single, married, divorced)?",
    "ielts": "What is your IELTS overall band score?",
    "salary_local": "What is your expected annual salary (amount only)?",
    "spouse_education": "What is your spouse's highest education level?",
    "spouse_is_working": "Is your spouse currently employed? (yes/no)",
    "num_children": "How many children do you have?",
}


def next_questions(slots: PersonSlots) -> Tuple[str, ...]:
    order: List[str] = [
        "preferred_country", "role", "age", "education", "degree_field", "occupation",
        "experience_years", "current_country", "marital_status",
    ]
    if requires_ielts(slots.preferred_country):
        order.append("ielts")
    order.append("salary_local")  # currency derived
    if (slots.marital_status or "").lower() == "married":
        order.extend(["spouse_education", "spouse_is_working", "num_children"])

    missing: List[str] = [k for k in order if getattr(slots, k) is None]
    prompts: List[str] = []
    for k in missing[:2]:  # ask up to 2 questions at a time
        # Tailor salary question to currency if known
        if k == "salary_local" and slots.preferred_country:
            cur = COUNTRY_TO_CURRENCY.get(slots.preferred_country, "local currency")
            prompts.append(f"What is your expected annual salary in {cur}? (amount only)")
        else:
            prompts.append(QUESTION_TEXT[k])
    return tuple(prompts)


# -----------------------------
# Orchestration: extract -> derive -> merge -> next questions
# -----------------------------

def derive(slots: PersonSlots) -> PersonSlots:
    data = slots.dict()
    # Normalize preferred country & currency
    if slots.preferred_country:
        norm = normalize_country(slots.preferred_country)
        if norm:
            data["preferred_country"] = norm
            data["salary_currency"] = COUNTRY_TO_CURRENCY.get(norm)
    # If not married, clear spouse details
    if (slots.marital_status or "").lower() in {"single", "divorced"}:
        data.update({
            "has_spouse": False,
            "spouse_education": None,
            "spouse_is_working": False,
        })
    return PersonSlots(**data).validate()


def extract_and_plan(user_text: str, state: PersonSlots) -> Tuple[PersonSlots, Tuple[str, ...]]:
    # 1) Extraction (LLM optional)
    slots = llm_extract(user_text)
    slots = derive(slots)
    # 2) Merge with conversation state
    merged = state.merge(slots).validate()
    # 3) Plan next questions
    questions = next_questions(merged)
    return merged, questions


# -----------------------------
# Natural formatting of engine results via LLM
# -----------------------------

def _stringify_results(results: Dict[str, Any]) -> str:
    """Compact string summary used as a fallback or LLM context."""
    lines: List[str] = []
    elig = results.get("eligibility") or []
    points = results.get("points") or []
    add_pts = results.get("add_points") or []
    expl = results.get("explanations") or []
    recs = results.get("recommendations") or []
    alts = results.get("alternative_suggestions") or []

    if elig:
        lines.append("Eligibility findings:")
        for item in elig:
            lines.append(f"- {item}")
    else:
        lines.append("No explicit eligibility facts detected.")

    if points:
        try:
            total = sum(p[1] for p in points if isinstance(p, (list, tuple)) and len(p) >= 2)
            lines.append(f"Points total: {total}")
        except Exception:
            pass
        for p in points:
            lines.append(f"- {p}")

    if add_pts:
        lines.append("Bonus points:")
        for p in add_pts:
            lines.append(f"- {p}")

    if expl:
        lines.append("Explanations:")
        for e in expl:
            lines.append(f"- {e}")

    if recs:
        lines.append("Recommendations:")
        for r in recs:
            lines.append(f"- {r}")

    if alts:
        lines.append("Alternatives: " + ", ".join(map(str, alts)))

    return "\n".join(lines)


def format_results_natural(results: Dict[str, Any], state: PersonSlots, show_alternatives: bool = True) -> str:
    """Use the LLM to produce a concise, human-friendly final message from engine results.
    Fallback to a compact string if LLM is unavailable.
    """
    # Fallback when LLM not configured
    if ChatOpenAI is None or not os.getenv("OPENAI_API_KEY"):
        # Optionally hide alternatives in fallback
        if not show_alternatives:
            res_copy = dict(results)
            res_copy["alternative_suggestions"] = []
            return _stringify_results(res_copy)
        return _stringify_results(results)

    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    llm = ChatOpenAI(model=model_name, temperature=0.4)

    facts_lines = []
    for k, v in state.dict().items():
        if v is not None and v != "":
            facts_lines.append(f"- {k}: {v}")
    facts = "\n".join(facts_lines) or "- none"

    # Optionally hide alternatives from the LLM context
    res_ctx = dict(results)
    if not show_alternatives:
        res_ctx["alternative_suggestions"] = []
    results_json = json.dumps(res_ctx, ensure_ascii=False)

    system = (
        "You are a friendly migration consultant. Based on KNOWN FACTS and ENGINE RESULTS, "
        "explain the applicant's situation and next steps in plain English. Keep it concise: "
        "4–6 sentences or short bullets. Include: eligibility status (if any), key reasons, points/bonuses, "
        "effects of spouse/children if relevant, and 2–3 alternative countries if provided. "
        "Avoid raw arrays, tuples, or bracketed data. Do not invent facts."
    )

    prompt = (
        f"SYSTEM:\n{system}\n\n"
        f"KNOWN FACTS:\n{facts}\n\n"
        f"ENGINE RESULTS (JSON):\n{results_json}\n\n"
        "ASSISTANT: Provide one concise, user-facing message."
    )

    resp = llm.invoke(prompt)
    return resp.content.strip() if hasattr(resp, "content") else str(resp)
