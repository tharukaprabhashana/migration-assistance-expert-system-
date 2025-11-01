# rules/base_rules.py
from experta import Fact, KnowledgeEngine, Rule, P

class Person(Fact):
    """
    Core applicant Fact. Use these fields (UI should collect them).
    - role: professional / student / unemployed
    - age: int
    - education: None/Diploma/Bachelors/Masters/PhD
    - degree_field: str
    - occupation: str (freeform; rules match substrings like 'IT','Engineer','Health','Finance','Hospitality','Research')
    - experience_years: number
    - ielts: number (if applicable)
    - salary_local: numeric (amount in LOCAL CURRENCY of preferred country)
    - salary_currency: currency code string (e.g., 'CAD', 'AUD', 'GBP') — optional but helpful
    - current_country: string
    - preferred_country: string (canonical country name used in specs)
    - marital_status: single/married/...
    - has_spouse: bool
    - spouse_education: None/Diploma/Bachelors/Masters/PhD
    - spouse_is_working: bool
    - num_children: int
    """
    pass

class BaseRules(KnowledgeEngine):
    """
    Generic rules shared across countries:
     - spouse education/employment boosts
     - dependent detection
     - generic low-income check (salary_local missing or zero)
     - final global recommendation placeholder
    """

    @Rule(Person(has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def base_spouse_education(self):
        self.declare(Fact(add_points=('SpouseEducation', 15)))
        self.declare(Fact(explanation="Spouse has higher education — adaptability points applicable."))

    @Rule(Person(has_spouse=True, spouse_is_working=True))
    def base_spouse_employment(self):
        self.declare(Fact(add_points=('SpouseWorking', 10)))
        self.declare(Fact(explanation="Spouse currently employed — adaptability points applicable."))

    @Rule(Person(num_children=P(lambda n: n is not None and n > 0)))
    def base_dependent_present(self):
        self.declare(Fact(dependent_possible=True))
        self.declare(Fact(explanation="Applicant has dependent children — dependent visa considerations apply."))

    @Rule(Person(salary_local=P(lambda s: s is None or s <= 0)))
    def base_low_income(self):
        self.declare(Fact(financial_ok=False))
        self.declare(Fact(explanation="Reported salary is missing or non-positive; many pathways require proof of funds."))

    @Rule(Fact(eligibility=P(lambda e: e is not None)))
    def base_final_recommendation(self):
        self.declare(Fact(recommendation="Review eligibility facts above for country-specific guidance; consult official immigration sources."))

