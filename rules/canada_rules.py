# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class CanadaRules:
    """Rules for Canada"""
    @Rule(Person(preferred_country='Canada', education='PhD', ielts=P(lambda x: x is not None and x >= 7.0), experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def canada_strong(self):
        self.declare(Fact(eligibility=('Canada', 'TopPath', 0.95)))
        self.declare(Fact(points=('Canada', 80)))
        self.declare(Fact(explanation="Canada: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Canada', education='Masters', ielts=P(lambda x: x is not None and x >= 6.0), experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def canada_medium(self):
        self.declare(Fact(eligibility=('Canada', 'MidPath', 0.85)))
        self.declare(Fact(points=('Canada', 65)))
        self.declare(Fact(explanation="Canada: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Canada', role='student'), salience=60)
    def canada_student(self):
        self.declare(Fact(eligibility=('Canada', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Canada', 35)))
        self.declare(Fact(explanation="Canada: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Canada', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def canada_it(self):
        self.declare(Fact(add_points=('Canada','IT', 10)))
        self.declare(Fact(explanation="Canada: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Canada', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def canada_engineering(self):
        self.declare(Fact(add_points=('Canada','Engineering', 12)))
        self.declare(Fact(explanation="Canada: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Canada', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def canada_healthcare(self):
        self.declare(Fact(add_points=('Canada','Healthcare', 14)))
        self.declare(Fact(explanation="Canada: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Canada', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def canada_business(self):
        self.declare(Fact(add_points=('Canada','Business', 8)))
        self.declare(Fact(explanation="Canada: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Canada', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def canada_hospitality(self):
        self.declare(Fact(add_points=('Canada','Hospitality', 6)))
        self.declare(Fact(explanation="Canada: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Canada', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def canada_research(self):
        self.declare(Fact(add_points=('Canada','Research', 10)))
        self.declare(Fact(explanation="Canada: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Canada', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def canada_spouse_edu(self):
        self.declare(Fact(add_points=('Canada','SpouseEducation', 15)))
        self.declare(Fact(explanation="Canada: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Canada', has_spouse=True, spouse_is_working=True))
    def canada_spouse_work(self):
        self.declare(Fact(add_points=('Canada','SpouseWorking', 10)))
        self.declare(Fact(explanation="Canada: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Canada', salary_local=P(lambda s: s is not None and s >= 36000)), salience=30)
    def canada_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Canada: reported salary meets conservative threshold (36000 CAD)."))

    @Rule(Person(preferred_country='Canada', num_children=P(lambda n: n is not None and n > 0)))
    def canada_dependent(self):
        self.declare(Fact(dependent_possible=('Canada', True)))
        self.declare(Fact(explanation="Canada: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Canada'))
    def canada_alternatives(self):
        self.declare(Fact(alternative_suggestions=['United Kingdom', 'United States', 'Australia', 'New Zealand']))
        self.declare(Fact(explanation="Canada: suggested alternative countries based on climate/culture group."))


# end of Canada
