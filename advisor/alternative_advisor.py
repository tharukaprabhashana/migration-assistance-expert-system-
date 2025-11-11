from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
import json
import os
import re

# Lightweight loader utils

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_country_specs(path: str = None) -> Dict[str, Dict[str, Any]]:
    """Load rules/country_specs.json and return a map name->spec."""
    if not path:
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "rules", "country_specs.json")
    data = load_json(path)
    by_name: Dict[str, Dict[str, Any]] = {}
    for c in data.get("countries", []):
        by_name[c["name"]] = c
    return by_name


def load_static_kb(path: str = None) -> Dict[str, Any]:
    if not path:
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static_kb.json")
    return load_json(path)


# Simple currency conversion
# Rate is USD per 1 unit of currency
RATES_TO_USD: Dict[str, float] = {
    "USD": 1.0,
    "CAD": 0.73,
    "AUD": 0.66,
    "NZD": 0.60,
    "GBP": 1.28,
    "EUR": 1.08,
    "NOK": 0.09,
    "SEK": 0.09,
    "DKK": 0.14,
    "JPY": 0.0067,
    "AED": 0.27,
    "SAR": 0.27,
}


def convert(amount: Optional[float], from_currency: Optional[str], to_currency: Optional[str], rates_to_usd: Dict[str, float]) -> Optional[float]:
    if amount is None or from_currency is None or to_currency is None:
        return None
    f = rates_to_usd.get(from_currency)
    t = rates_to_usd.get(to_currency)
    if not f or not t:
        return None
    usd = amount * f
    return usd / t


def derive_occupation_category(occupation: Optional[str]) -> Optional[str]:
    if not occupation:
        return None
    s = occupation.lower()
    mapping = [
        ("IT", ["software", "developer", "programmer", "data", "machine learning", "ml", "ai", "devops"]),
        ("Engineering", ["engineer", "engineering", "civil", "mechanical", "electrical", "electronics"]),
        ("Healthcare", ["nurse", "doctor", "physician", "clinician", "pharma", "medical", "dentist"]),
        ("Business", ["manager", "accountant", "finance", "marketing", "sales", "hr", "business"]),
        ("Hospitality", ["hospitality", "chef", "hotel", "tourism", "restaurant"]),
        ("Research", ["research", "scientist", "phd", "postdoc", "academic"]),
    ]
    for cat, kws in mapping:
        if any(kw in s for kw in kws):
            return cat
    return None


def suggest_alternatives(
    person: Dict[str, Any],
    top_n: int = 3,
    country_specs_path: Optional[str] = None,
    static_kb_path: Optional[str] = None,
    rates_to_usd: Optional[Dict[str, float]] = None,
) -> List[Dict[str, Any]]:
    specs = load_country_specs(country_specs_path)
    kb = load_static_kb(static_kb_path)
    rates = rates_to_usd or RATES_TO_USD

    preferred = person.get("preferred_country")
    salary = person.get("salary_local")
    salary_cur = person.get("salary_currency")
    ielts = person.get("ielts")
    occupation = person.get("occupation")
    occ_cat = derive_occupation_category(occupation)

    # Helper: get group for a country
    def group_of(name: str) -> Optional[str]:
        c = specs.get(name)
        return c.get("group") if c else None

    preferred_group = group_of(preferred) if preferred else None

    # Iterate candidate countries
    scored: List[Tuple[str, float, List[str]]] = []
    for cname, c in specs.items():
        if preferred and cname == preferred:
            continue
        score = 0.0
        reasons: List[str] = []

        # IELTS fit
        c_ielts_required = bool(c.get("ielts_required"))
        if not ielts:
            if not c_ielts_required:
                score += 20
                reasons.append("no IELTS needed")
        else:
            # If user has IELTS and candidate requires, small bonus if thresholds exist
            strong = c.get("ielts_strong")
            med = c.get("ielts_medium")
            try:
                iv = float(ielts)
            except Exception:
                iv = None
            if iv is not None and c_ielts_required:
                if strong and iv >= strong:
                    score += 10
                    reasons.append("strong IELTS")
                elif med and iv >= med:
                    score += 6
                    reasons.append("IELTS meets threshold")

        # Salary fit (convert to candidate currency)
        cand_cur = c.get("currency")
        cand_thr = c.get("salary_threshold")
        if salary is not None and cand_cur and cand_thr:
            conv = convert(float(salary), str(salary_cur) if salary_cur else None, cand_cur, rates)
            if conv is not None:
                if conv >= float(cand_thr):
                    score += 12
                    reasons.append("meets salary threshold")
                elif conv >= 0.85 * float(cand_thr):
                    score += 5
                    reasons.append("near salary threshold")

        # Group/cultural fit
        cg = c.get("group")
        if preferred_group and cg == preferred_group:
            score += 8
            reasons.append("same group")

        # Occupation bonus
        if occ_cat:
            bonus_map = c.get("occupation_bonus") or {}
            bonus = 0
            # exact match or fallback by a few aliases
            for key, val in bonus_map.items():
                if key.lower() == occ_cat.lower():
                    bonus = int(val)
                    break
            if bonus > 0:
                score += bonus
                reasons.append(f"{occ_cat} bonus +{bonus}")

        if score > 0:
            scored.append((cname, score, reasons))

    # Sort and take top N
    scored.sort(key=lambda x: x[1], reverse=True)
    top = scored[: max(0, top_n)]

    return [
        {"name": name, "score": score, "reasons": reasons}
        for name, score, reasons in top
    ]


def estimate_salary(
    person: Dict[str, Any],
    country_specs_path: Optional[str] = None,
    static_kb_path: Optional[str] = None,
    rates_to_usd: Optional[Dict[str, float]] = None,
) -> Optional[int]:
    """Estimate an annual salary in the preferred country's local currency.
    Heuristic: start from static_kb typical_min_income_usd_annual, adjust by occupation bonus,
    education, and experience. Convert to target currency. Returns an int (rounded to nearest 1000).
    """
    specs = load_country_specs(country_specs_path)
    kb = load_static_kb(static_kb_path)
    rates = rates_to_usd or RATES_TO_USD

    preferred = person.get("preferred_country")
    if not preferred:
        return None
    cand = specs.get(preferred) or {}
    target_cur = cand.get("currency")
    if not target_cur:
        return None

    # Find base USD income for that country from static_kb
    base_usd: Optional[float] = None
    for c in kb.get("countries", []):
        if c.get("name") == preferred:
            try:
                base_usd = float(c.get("typical_min_income_usd_annual"))
            except Exception:
                base_usd = None
            break
    if base_usd is None:
        # fallback: take a generic base
        base_usd = 28000.0

    # Adjustments
    occupation = person.get("occupation")
    occ_cat = derive_occupation_category(occupation)
    bonus_pct = 0.0
    if occ_cat:
        bonus_map = cand.get("occupation_bonus") or {}
        # scale bonus (e.g., +12 -> +9%)
        raw = 0
        for k, v in bonus_map.items():
            if k.lower() == occ_cat.lower():
                try:
                    raw = int(v)
                except Exception:
                    raw = 0
                break
        bonus_pct += 0.0075 * raw  # 0.75% per bonus point

    edu = (person.get("education") or "").lower()
    if "phd" in edu:
        bonus_pct += 0.20
    elif "master" in edu:
        bonus_pct += 0.12
    elif "bachelor" in edu:
        bonus_pct += 0.05

    try:
        exp = int(person.get("experience_years") or 0)
    except Exception:
        exp = 0
    bonus_pct += min(0.02 * max(0, exp), 0.20)  # up to +20% for experience

    adj_usd = base_usd * (1.0 + bonus_pct)
    # Convert USD -> local currency
    amount_local = convert(adj_usd, "USD", target_cur, rates)
    if amount_local is None:
        return None
    # Round to nearest 1000
    try:
        return int(round(amount_local / 1000.0) * 1000)
    except Exception:
        return int(amount_local)
