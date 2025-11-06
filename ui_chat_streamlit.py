import os
import logging
import streamlit as st
import httpx
from engine import MigrationEngine
from chat_agent import (
    PersonSlots,
    chat_turn,
    COUNTRY_TO_CURRENCY,
    format_results_natural,
)

st.set_page_config(page_title="Migration Expert System (Chat)", layout="wide")
st.title("💬 Migration Assistance Expert System — Chat")
logging.getLogger("streamlit").setLevel(logging.WARNING)

# Backend configuration (FastAPI). If not available, we use local functions.
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

# Session state init
if "messages" not in st.session_state:
    st.session_state.messages = []
if "slots" not in st.session_state:
    st.session_state.slots = PersonSlots()
if "completed" not in st.session_state:
    st.session_state.completed = False
if "results" not in st.session_state:
    st.session_state.results = None


def add_assistant(msg: str):
    st.session_state.messages.append({"role": "assistant", "content": msg})


def add_user(msg: str):
    st.session_state.messages.append({"role": "user", "content": msg})


def summarize_results(results: dict) -> str:
    lines = []
    elig = results.get("eligibility") or []
    points = results.get("points") or []
    add_pts = results.get("add_points") or []
    expl = results.get("explanations") or []
    recs = results.get("recommendations") or []
    alts = results.get("alternative_suggestions") or []

    if elig:
        lines.append("Eligibility findings:")
        for item in elig:
            # item format depends on rules; show as string safely
            lines.append(f"- {item}")
    else:
        lines.append("No explicit eligibility facts detected.")

    if points:
        # If points are tuples like (label, score)
        try:
            total = sum(p[1] for p in points if isinstance(p, (list, tuple)) and len(p) >= 2)
            lines.append(f"\nPoints summary: total = {total}")
        except Exception:
            pass
        for p in points:
            lines.append(f"- {p}")

    if add_pts:
        lines.append("\nBonus:")
        for p in add_pts:
            lines.append(f"- {p}")

    if expl:
        lines.append("\nExplanations:")
        for e in expl:
            lines.append(f"- {e}")

    if recs:
        lines.append("\nRecommendations:")
        for r in recs:
            lines.append(f"- {r}")

    if alts:
        lines.append("\nAlternatives:")
        lines.append(", ".join(map(str, alts)))

    return "\n".join(lines)


with st.sidebar:
    st.header("Session")
    if st.button("Reset chat"):
        st.session_state.messages = []
        st.session_state.slots = PersonSlots()
        st.session_state.completed = False
        st.session_state.results = None
        st.rerun()
    st.write("Fields collected so far:")
    st.json(st.session_state.slots.dict())

def call_backend_chat_turn(text: str, state_dict: dict, history: list[dict]) -> tuple[str, dict, bool]:
    with httpx.Client(timeout=30.0) as client:
        resp = client.post(
            f"{BACKEND_URL}/chat_turn",
            json={"text": text, "state": state_dict, "history": history},
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("assistant", ""), data.get("state", {}), bool(data.get("ready", False))


def call_backend_run(person: dict) -> dict:
    with httpx.Client(timeout=30.0) as client:
        resp = client.post(f"{BACKEND_URL}/run_engine", json={"person": person})
        resp.raise_for_status()
        data = resp.json()
        return data

def call_backend_format(results: dict, state: dict, show_alternatives: bool = True) -> str:
    with httpx.Client(timeout=30.0) as client:
        resp = client.post(
            f"{BACKEND_URL}/format_results",
            json={"results": results, "state": state, "show_alternatives": show_alternatives},
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("message", "")
def has_preferred_eligibility(results: dict, preferred: str | None) -> bool:
    if not preferred:
        return False
    elig = results.get("eligibility") or []
    preferred_lower = str(preferred).lower()
    for item in elig:
        s = str(item).lower()
        if preferred_lower in s and not any(neg in s for neg in ["not eligible", "ineligible", "no eligibility"]):
            return True
    return False


"""
Rendering strategy:
1) Render entire history from session_state.
2) Accept new input; update session_state with user and assistant messages.
3) st.rerun() to re-render history in correct order and sides; avoids duplicates.
"""

# Initial assistant greeting
if not st.session_state.messages:
    greeting = "Hi! I can assess your migration eligibility. Tell me your plan (e.g., ‘I want to move to Canada’)."
    st.session_state.messages.append({"role": "assistant", "content": greeting})

# Render history
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Input
prompt = st.chat_input("Type your message")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    asked_alternatives = any(k in prompt.lower() for k in ["alternative", "suggest", "other country"])        

    # Backend first; fallback to local
    try:
        assistant_msg, state_dict, ready = call_backend_chat_turn(
            prompt, st.session_state.slots.dict(), st.session_state.messages
        )
        st.session_state.slots = PersonSlots(**state_dict)
    except Exception:
        try:
            assistant_msg, new_state, ready = chat_turn(
                prompt, st.session_state.slots, st.session_state.messages
            )
            st.session_state.slots = new_state
        except Exception:
            warn = (
                "LLM isn't configured. Please set OPENAI_API_KEY in your .env and restart, "
                "or run the FastAPI backend."
            )
            st.session_state.messages.append({"role": "assistant", "content": warn})
            st.rerun()

    # Append the assistant's natural reply first
    if assistant_msg:
        st.session_state.messages.append({"role": "assistant", "content": assistant_msg})

    # Currency derivation still applied silently
    if st.session_state.slots.preferred_country and not st.session_state.slots.salary_currency:
        st.session_state.slots.salary_currency = COUNTRY_TO_CURRENCY.get(st.session_state.slots.preferred_country)

    # If the LLM indicates we're ready (or completion check passes), run engine
    if (locals().get("ready") is True) or st.session_state.slots.is_complete():
        person_data = st.session_state.slots.dict()
        if (person_data.get("marital_status") or "").lower() != "married":
            person_data["has_spouse"] = False
            person_data["spouse_is_working"] = False
        try:
            run_payload = call_backend_run(person_data)
            results = run_payload.get("results", {})
            formatted = ""
        except Exception:
            engine = MigrationEngine()
            results = engine.run_for_person(person_data)
            # Try local natural formatting
            formatted = ""
        st.session_state.results = results
        st.session_state.completed = True
        # Decide when to show alternatives: if user asked OR user not eligible for preferred country
        show_alts = asked_alternatives or not has_preferred_eligibility(results, st.session_state.slots.preferred_country)
        # Prefer formatted natural message; fallback to raw summary
        if not formatted:
            try:
                # Ask backend to compute data-driven alternatives when allowed
                formatted = call_backend_format(
                    results,
                    st.session_state.slots.dict(),
                    show_alternatives=show_alts,
                )
            except Exception:
                try:
                    # Local fallback: best-effort natural formatting without advisor enrichment
                    formatted = format_results_natural(
                        results,
                        st.session_state.slots,
                        show_alternatives=show_alts,
                    )
                except Exception:
                    formatted = ""
        final_msg = formatted or summarize_results(results)
        st.session_state.messages.append({"role": "assistant", "content": final_msg})
        st.rerun()
    else:
        st.rerun()
