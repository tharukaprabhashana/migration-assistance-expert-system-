# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class UnitedArabEmiratesRules:
    """Rules for United Arab Emirates"""
    @Rule(Person(preferred_country='United Arab Emirates', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def united_arab_emirates_strong(self):
        self.declare(Fact(eligibility=('United Arab Emirates', 'TopPath', 0.95)))
        self.declare(Fact(points=('United Arab Emirates', 80)))
        self.declare(Fact(explanation="United Arab Emirates: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='United Arab Emirates', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def united_arab_emirates_medium(self):
        self.declare(Fact(eligibility=('United Arab Emirates', 'MidPath', 0.85)))
        self.declare(Fact(points=('United Arab Emirates', 65)))
        self.declare(Fact(explanation="United Arab Emirates: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='United Arab Emirates', role='student'), salience=60)
    def united_arab_emirates_student(self):
        self.declare(Fact(eligibility=('United Arab Emirates', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('United Arab Emirates', 35)))
        self.declare(Fact(explanation="United Arab Emirates: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='United Arab Emirates', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def united_arab_emirates_it(self):
        self.declare(Fact(add_points=('United Arab Emirates','IT', 10)))
        self.declare(Fact(explanation="United Arab Emirates: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Arab Emirates', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def united_arab_emirates_engineering(self):
        self.declare(Fact(add_points=('United Arab Emirates','Engineering', 10)))
        self.declare(Fact(explanation="United Arab Emirates: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Arab Emirates', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def united_arab_emirates_healthcare(self):
        self.declare(Fact(add_points=('United Arab Emirates','Healthcare', 10)))
        self.declare(Fact(explanation="United Arab Emirates: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Arab Emirates', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def united_arab_emirates_business(self):
        self.declare(Fact(add_points=('United Arab Emirates','Business', 10)))
        self.declare(Fact(explanation="United Arab Emirates: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Arab Emirates', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def united_arab_emirates_hospitality(self):
        self.declare(Fact(add_points=('United Arab Emirates','Hospitality', 12)))
        self.declare(Fact(explanation="United Arab Emirates: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Arab Emirates', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def united_arab_emirates_research(self):
        self.declare(Fact(add_points=('United Arab Emirates','Research', 8)))
        self.declare(Fact(explanation="United Arab Emirates: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Arab Emirates', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def united_arab_emirates_spouse_edu(self):
        self.declare(Fact(add_points=('United Arab Emirates','SpouseEducation', 15)))
        self.declare(Fact(explanation="United Arab Emirates: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='United Arab Emirates', has_spouse=True, spouse_is_working=True))
    def united_arab_emirates_spouse_work(self):
        self.declare(Fact(add_points=('United Arab Emirates','SpouseWorking', 10)))
        self.declare(Fact(explanation="United Arab Emirates: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='United Arab Emirates', salary_local=P(lambda s: s is not None and s >= 60000)), salience=30)
    def united_arab_emirates_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="United Arab Emirates: reported salary meets conservative threshold (60000 AED)."))

    @Rule(Person(preferred_country='United Arab Emirates', num_children=P(lambda n: n is not None and n > 0)))
    def united_arab_emirates_dependent(self):
        self.declare(Fact(dependent_possible=('United Arab Emirates', True)))
        self.declare(Fact(explanation="United Arab Emirates: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='United Arab Emirates'))
    def united_arab_emirates_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Saudi Arabia']))
        self.declare(Fact(explanation="United Arab Emirates: suggested alternative countries based on climate/culture group."))


# end of United Arab Emirates
