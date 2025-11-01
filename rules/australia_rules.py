# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class AustraliaRules:
    """Rules for Australia"""
    @Rule(Person(preferred_country='Australia', education='PhD', ielts=P(lambda x: x is not None and x >= 7.5), experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def australia_strong(self):
        self.declare(Fact(eligibility=('Australia', 'TopPath', 0.95)))
        self.declare(Fact(points=('Australia', 80)))
        self.declare(Fact(explanation="Australia: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Australia', education='Masters', ielts=P(lambda x: x is not None and x >= 6.5), experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def australia_medium(self):
        self.declare(Fact(eligibility=('Australia', 'MidPath', 0.85)))
        self.declare(Fact(points=('Australia', 65)))
        self.declare(Fact(explanation="Australia: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Australia', role='student'), salience=60)
    def australia_student(self):
        self.declare(Fact(eligibility=('Australia', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Australia', 35)))
        self.declare(Fact(explanation="Australia: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Australia', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def australia_it(self):
        self.declare(Fact(add_points=('Australia','IT', 12)))
        self.declare(Fact(explanation="Australia: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Australia', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def australia_engineering(self):
        self.declare(Fact(add_points=('Australia','Engineering', 12)))
        self.declare(Fact(explanation="Australia: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Australia', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def australia_healthcare(self):
        self.declare(Fact(add_points=('Australia','Healthcare', 15)))
        self.declare(Fact(explanation="Australia: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Australia', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def australia_business(self):
        self.declare(Fact(add_points=('Australia','Business', 8)))
        self.declare(Fact(explanation="Australia: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Australia', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def australia_hospitality(self):
        self.declare(Fact(add_points=('Australia','Hospitality', 6)))
        self.declare(Fact(explanation="Australia: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Australia', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def australia_research(self):
        self.declare(Fact(add_points=('Australia','Research', 10)))
        self.declare(Fact(explanation="Australia: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Australia', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def australia_spouse_edu(self):
        self.declare(Fact(add_points=('Australia','SpouseEducation', 15)))
        self.declare(Fact(explanation="Australia: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Australia', has_spouse=True, spouse_is_working=True))
    def australia_spouse_work(self):
        self.declare(Fact(add_points=('Australia','SpouseWorking', 10)))
        self.declare(Fact(explanation="Australia: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Australia', salary_local=P(lambda s: s is not None and s >= 45000)), salience=30)
    def australia_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Australia: reported salary meets conservative threshold (45000 AUD)."))

    @Rule(Person(preferred_country='Australia', num_children=P(lambda n: n is not None and n > 0)))
    def australia_dependent(self):
        self.declare(Fact(dependent_possible=('Australia', True)))
        self.declare(Fact(explanation="Australia: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Australia'))
    def australia_alternatives(self):
        self.declare(Fact(alternative_suggestions=['United Kingdom', 'United States', 'Canada', 'New Zealand']))
        self.declare(Fact(explanation="Australia: suggested alternative countries based on climate/culture group."))


# end of Australia
