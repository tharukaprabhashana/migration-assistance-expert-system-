# engine.py
import json
from rules import BaseRules
from rules import Person
from rules import __all__ as RULE_CLASSES  # names of classes imported into rules.__init__

# Build list of country Rule classes from globals (in rules.__init__ they are exposed)
import rules as rules_pkg
country_rule_classes = []
for name in RULE_CLASSES:
    if name not in ("Person", "BaseRules"):
        cls = getattr(rules_pkg, name, None)
        if cls is not None:
            country_rule_classes.append(cls)

# Create a dynamic engine class that inherits BaseRules + all country rule classes
EngineBases = tuple([BaseRules] + country_rule_classes)

class AllCountriesEngine(*EngineBases):  
    """Combined engine class (BaseRules + per-country rule mixins)."""
    pass

def load_static_kb(path="static_kb.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

class MigrationEngine:
    def __init__(self, kb=None):
        self.kb = kb or load_static_kb()
        self.engine = AllCountriesEngine()
        self.results = None

    def run_for_person(self, person_dict):
        self.results = {
            "eligibility": [],
            "points": [],
            "add_points": [],
            "financial": [],
            "dependent": [],
            "explanations": [],
            "recommendations": [],
            "alternative_suggestions": []
        }
        # Build Person Fact with salary_local and salary_currency fields
        person_fact = Person(
            role=person_dict.get("role"),
            age=person_dict.get("age"),
            education=person_dict.get("education"),
            degree_field=person_dict.get("degree_field"),
            occupation=person_dict.get("occupation"),
            experience_years=person_dict.get("experience_years"),
            ielts=person_dict.get("ielts"),
            salary_local=person_dict.get("salary_local"),
            salary_currency=person_dict.get("salary_currency"),
            current_country=person_dict.get("current_country"),
            preferred_country=person_dict.get("preferred_country"),
            marital_status=person_dict.get("marital_status"),
            has_spouse=person_dict.get("has_spouse", False),
            spouse_education=person_dict.get("spouse_education"),
            spouse_is_working=person_dict.get("spouse_is_working", False),
            num_children=person_dict.get("num_children", 0)
        )
        self.engine.reset()
        self.engine.declare(person_fact)
        self.engine.run()

        for fid, fact in list(self.engine.facts.items()):
            try:
                d = fact.as_dict()
            except Exception:
                continue
            if "eligibility" in d:
                self.results["eligibility"].append(d["eligibility"])
            if "points" in d:
                self.results["points"].append(d["points"])
            if "add_points" in d:
                self.results["add_points"].append(d["add_points"])
            if "financial_ok" in d:
                self.results["financial"].append(d["financial_ok"])
            if "dependent_possible" in d:
                self.results["dependent"].append(d["dependent_possible"])
            if "explanation" in d:
                self.results["explanations"].append(d["explanation"])
            if "recommendation" in d:
                self.results["recommendations"].append(d["recommendation"])
            if "alternative_suggestions" in d:
                self.results["alternative_suggestions"].extend(d["alternative_suggestions"])

        # Deduplicate alternatives
        self.results["alternative_suggestions"] = list(dict.fromkeys(self.results["alternative_suggestions"]))
        return self.results

if __name__ == "__main__":
    
    kb = load_static_kb()
    engine = MigrationEngine(kb)
