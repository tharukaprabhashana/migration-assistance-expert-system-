# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class UnitedStatesRules:
    """Rules for United States"""
    @Rule(Person(preferred_country='United States', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def united_states_strong(self):
        self.declare(Fact(eligibility=('United States', 'TopPath', 0.95)))
        self.declare(Fact(points=('United States', 80)))
        self.declare(Fact(explanation="United States: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='United States', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def united_states_medium(self):
        self.declare(Fact(eligibility=('United States', 'MidPath', 0.85)))
        self.declare(Fact(points=('United States', 65)))
        self.declare(Fact(explanation="United States: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='United States', role='student'), salience=60)
    def united_states_student(self):
        self.declare(Fact(eligibility=('United States', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('United States', 35)))
        self.declare(Fact(explanation="United States: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='United States', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def united_states_it(self):
        self.declare(Fact(add_points=('United States','IT', 12)))
        self.declare(Fact(explanation="United States: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United States', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def united_states_engineering(self):
        self.declare(Fact(add_points=('United States','Engineering', 12)))
        self.declare(Fact(explanation="United States: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United States', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def united_states_healthcare(self):
        self.declare(Fact(add_points=('United States','Healthcare', 15)))
        self.declare(Fact(explanation="United States: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United States', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def united_states_business(self):
        self.declare(Fact(add_points=('United States','Business', 10)))
        self.declare(Fact(explanation="United States: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United States', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def united_states_hospitality(self):
        self.declare(Fact(add_points=('United States','Hospitality', 6)))
        self.declare(Fact(explanation="United States: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United States', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def united_states_research(self):
        self.declare(Fact(add_points=('United States','Research', 15)))
        self.declare(Fact(explanation="United States: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='United States', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def united_states_spouse_edu(self):
        self.declare(Fact(add_points=('United States','SpouseEducation', 15)))
        self.declare(Fact(explanation="United States: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='United States', has_spouse=True, spouse_is_working=True))
    def united_states_spouse_work(self):
        self.declare(Fact(add_points=('United States','SpouseWorking', 10)))
        self.declare(Fact(explanation="United States: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='United States', salary_local=P(lambda s: s is not None and s >= 40000)), salience=30)
    def united_states_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="United States: reported salary meets conservative threshold (40000 USD)."))

    @Rule(Person(preferred_country='United States', num_children=P(lambda n: n is not None and n > 0)))
    def united_states_dependent(self):
        self.declare(Fact(dependent_possible=('United States', True)))
        self.declare(Fact(explanation="United States: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='United States'))
    def united_states_alternatives(self):
        self.declare(Fact(alternative_suggestions=['United Kingdom', 'Canada', 'Australia', 'New Zealand']))
        self.declare(Fact(explanation="United States: suggested alternative countries based on climate/culture group."))


# end of United States
