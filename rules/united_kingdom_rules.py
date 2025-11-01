# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class UnitedKingdomRules:
    """Rules for United Kingdom"""
    @Rule(Person(preferred_country='United Kingdom', education='PhD', ielts=P(lambda x: x is not None and x >= 6.5), experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def united_kingdom_strong(self):
        self.declare(Fact(eligibility=('United Kingdom', 'TopPath', 0.95)))
        self.declare(Fact(points=('United Kingdom', 80)))
        self.declare(Fact(explanation="United Kingdom: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='United Kingdom', education='Masters', ielts=P(lambda x: x is not None and x >= 6.0), experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def united_kingdom_medium(self):
        self.declare(Fact(eligibility=('United Kingdom', 'MidPath', 0.85)))
        self.declare(Fact(points=('United Kingdom', 65)))
        self.declare(Fact(explanation="United Kingdom: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='United Kingdom', role='student'), salience=60)
    def united_kingdom_student(self):
        self.declare(Fact(eligibility=('United Kingdom', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('United Kingdom', 35)))
        self.declare(Fact(explanation="United Kingdom: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='United Kingdom', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def united_kingdom_it(self):
        self.declare(Fact(add_points=('United Kingdom','IT', 12)))
        self.declare(Fact(explanation="United Kingdom: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Kingdom', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def united_kingdom_engineering(self):
        self.declare(Fact(add_points=('United Kingdom','Engineering', 10)))
        self.declare(Fact(explanation="United Kingdom: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Kingdom', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def united_kingdom_healthcare(self):
        self.declare(Fact(add_points=('United Kingdom','Healthcare', 15)))
        self.declare(Fact(explanation="United Kingdom: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Kingdom', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def united_kingdom_business(self):
        self.declare(Fact(add_points=('United Kingdom','Business', 10)))
        self.declare(Fact(explanation="United Kingdom: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Kingdom', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def united_kingdom_hospitality(self):
        self.declare(Fact(add_points=('United Kingdom','Hospitality', 6)))
        self.declare(Fact(explanation="United Kingdom: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Kingdom', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def united_kingdom_research(self):
        self.declare(Fact(add_points=('United Kingdom','Research', 12)))
        self.declare(Fact(explanation="United Kingdom: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United Kingdom', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def united_kingdom_spouse_edu(self):
        self.declare(Fact(add_points=('United Kingdom','SpouseEducation', 15)))
        self.declare(Fact(explanation="United Kingdom: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='United Kingdom', has_spouse=True, spouse_is_working=True))
    def united_kingdom_spouse_work(self):
        self.declare(Fact(add_points=('United Kingdom','SpouseWorking', 10)))
        self.declare(Fact(explanation="United Kingdom: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='United Kingdom', salary_local=P(lambda s: s is not None and s >= 25000)), salience=30)
    def united_kingdom_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="United Kingdom: reported salary meets conservative threshold (25000 GBP)."))

    @Rule(Person(preferred_country='United Kingdom', num_children=P(lambda n: n is not None and n > 0)))
    def united_kingdom_dependent(self):
        self.declare(Fact(dependent_possible=('United Kingdom', True)))
        self.declare(Fact(explanation="United Kingdom: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='United Kingdom'))
    def united_kingdom_alternatives(self):
        self.declare(Fact(alternative_suggestions=['United States', 'Canada', 'Australia', 'New Zealand']))
        self.declare(Fact(explanation="United Kingdom: suggested alternative countries based on climate/culture group."))


# end of United Kingdom
