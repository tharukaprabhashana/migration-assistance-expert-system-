# tools/generate_country_rules.py
import json
import os
import re

SRC_DIR = os.path.dirname(os.path.dirname(__file__)) if "__file__" in globals() else "."
RULES_DIR = os.path.join(SRC_DIR, "rules")
SPEC_PATH = os.path.join(RULES_DIR, "country_specs.json")

TEMPLATE_HEADER = '''# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class {class_name}:
    """Rules for {country_name}"""
'''

TEMPLATE_FOOTER = """
# end of {country_name}
"""

def sanitize_class_name(name):
    return re.sub(r'[^0-9a-zA-Z]', '_', name).title().replace('_', '')

def write_country_rules(spec):
    country = spec["name"]
    class_name = sanitize_class_name(country) + "Rules"

    lines = [TEMPLATE_HEADER.format(class_name=class_name, country_name=country)]

    # Strong rule
    if spec.get("ielts_required"):
        strong_cond = "education='PhD', ielts=P(lambda x: x is not None and x >= {0}), experience_years=P(lambda e: e is not None and e >= 3)".format(spec.get("ielts_strong"))
    else:
        strong_cond = "education='PhD', experience_years=P(lambda e: e is not None and e >= 3)"
    lines.append(
        f"    @Rule(Person(preferred_country='{country}', {strong_cond}), salience=80)\n"
        f"    def {country.lower().replace(' ','_')}_strong(self):\n"
        f"        self.declare(Fact(eligibility=('{country}', 'TopPath', 0.95)))\n"
        f"        self.declare(Fact(points=('{country}', 80)))\n"
        f"        self.declare(Fact(explanation=\"{country}: PhD-level top path (illustrative).\"))\n\n"
    )

    # Medium rule
    if spec.get("ielts_required"):
        med_cond = "education='Masters', ielts=P(lambda x: x is not None and x >= {0}), experience_years=P(lambda e: e is not None and e >= 2)".format(spec.get("ielts_medium"))
    else:
        med_cond = "education='Masters', experience_years=P(lambda e: e is not None and e >= 2)"
    lines.append(
        f"    @Rule(Person(preferred_country='{country}', {med_cond}), salience=70)\n"
        f"    def {country.lower().replace(' ','_')}_medium(self):\n"
        f"        self.declare(Fact(eligibility=('{country}', 'MidPath', 0.85)))\n"
        f"        self.declare(Fact(points=('{country}', 65)))\n"
        f"        self.declare(Fact(explanation=\"{country}: Masters-level / mid path (illustrative).\"))\n\n"
    )

    # Student path rule
    lines.append(
        f"    @Rule(Person(preferred_country='{country}', role='student'), salience=60)\n"
        f"    def {country.lower().replace(' ','_')}_student(self):\n"
        f"        self.declare(Fact(eligibility=('{country}', 'StudentToWorkPath', 0.6)))\n"
        f"        self.declare(Fact(points=('{country}', 35)))\n"
        f"        self.declare(Fact(explanation=\"{country}: student->work/graduate path often exists (illustrative).\"))\n\n"
    )

    # Occupation-based rules: for each of the 6 domains create a rule using occupation substring checks
    occ = spec.get("occupation_bonus", {})
    for domain_key in ["IT", "Engineering", "Healthcare", "Business", "Hospitality", "Research"]:
        bonus = occ.get(domain_key, 8)
        method_name = f"{country.lower().replace(' ','_')}_{domain_key.lower()}"
        lines.append(
            f"    @Rule(Person(preferred_country='{country}', occupation=P(lambda o: o and ('{domain_key}' in o or '{domain_key[:-1]}' in o))), salience=65)\n"
            f"    def {method_name}(self):\n"
            f"        self.declare(Fact(add_points=('{country}','{domain_key}', {bonus})))\n"
            f"        self.declare(Fact(explanation=\"{country}: occupation {domain_key} receives bonus points (illustrative).\"))\n\n"
        )

    # Spouse rules (education + working) - localized but similar pattern
    lines.append(
        f"    @Rule(Person(preferred_country='{country}', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))\n"
        f"    def {country.lower().replace(' ','_')}_spouse_edu(self):\n"
        f"        self.declare(Fact(add_points=('{country}','SpouseEducation', 15)))\n"
        f"        self.declare(Fact(explanation=\"{country}: spouse education adds adaptability points.\"))\n\n"
    )
    lines.append(
        f"    @Rule(Person(preferred_country='{country}', has_spouse=True, spouse_is_working=True))\n"
        f"    def {country.lower().replace(' ','_')}_spouse_work(self):\n"
        f"        self.declare(Fact(add_points=('{country}','SpouseWorking', 10)))\n"
        f"        self.declare(Fact(explanation=\"{country}: spouse employment adds adaptability points.\"))\n\n"
    )

    # Financial rule (use salary_local threshold from spec)
    thr = spec.get("salary_threshold", 0)
    lines.append(
        f"    @Rule(Person(preferred_country='{country}', salary_local=P(lambda s: s is not None and s >= {thr})), salience=30)\n"
        f"    def {country.lower().replace(' ','_')}_financial_ok(self):\n"
        f"        self.declare(Fact(financial_ok=True))\n"
        f"        self.declare(Fact(explanation=\"{country}: reported salary meets conservative threshold ({thr} {spec.get('currency')}).\"))\n\n"
    )

    # Dependent rule (if num_children>0)
    lines.append(
        f"    @Rule(Person(preferred_country='{country}', num_children=P(lambda n: n is not None and n > 0)))\n"
        f"    def {country.lower().replace(' ','_')}_dependent(self):\n"
        f"        self.declare(Fact(dependent_possible=('{country}', True)))\n"
        f"        self.declare(Fact(explanation=\"{country}: dependent child detected — family visa streams may apply.\"))\n\n"
    )

    # Alternative suggestion using group
    group = spec.get("group", "")
    alt_list = []
    if group == "Nordic":
        alt_list = ["Norway","Sweden","Finland","Denmark"]
    elif group == "Gulf":
        alt_list = ["United Arab Emirates","Saudi Arabia"]
    elif group == "Anglo":
        alt_list = ["United Kingdom","United States","Canada","Australia","New Zealand"]
    elif group == "Schengen":
        alt_list = ["Germany","France","Italy","Netherlands","Latvia"]
    elif group == "Asia-Urban":
        alt_list = ["Singapore","Japan"]

    # remove self from alt_list
    alt_list = [c for c in alt_list if c != country]
    lines.append(
        f"    @Rule(Person(preferred_country='{country}'))\n"
        f"    def {country.lower().replace(' ','_')}_alternatives(self):\n"
        f"        self.declare(Fact(alternative_suggestions={alt_list}))\n"
        f"        self.declare(Fact(explanation=\"{country}: suggested alternative countries based on climate/culture group.\"))\n\n"
    )

    lines.append(TEMPLATE_FOOTER.format(country_name=country))
    # Write file
    fname = os.path.join(RULES_DIR, f"{country.lower().replace(' ','_')}_rules.py")
    with open(fname, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print("Wrote", fname)

def main():
    with open(SPEC_PATH, "r", encoding="utf-8") as f:
        spec = json.load(f)
    for c in spec["countries"]:
        write_country_rules(c)
    print("All country rule files generated.")

if __name__ == "__main__":
    main()
