# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class LatviaRules:
    """Rules for Latvia"""
    @Rule(Person(preferred_country='Latvia', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def latvia_strong(self):
        self.declare(Fact(eligibility=('Latvia', 'TopPath', 0.95)))
        self.declare(Fact(points=('Latvia', 80)))
        self.declare(Fact(explanation="Latvia: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Latvia', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def latvia_medium(self):
        self.declare(Fact(eligibility=('Latvia', 'MidPath', 0.85)))
        self.declare(Fact(points=('Latvia', 65)))
        self.declare(Fact(explanation="Latvia: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Latvia', role='student'), salience=60)
    def latvia_student(self):
        self.declare(Fact(eligibility=('Latvia', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Latvia', 35)))
        self.declare(Fact(explanation="Latvia: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Latvia', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def latvia_it(self):
        self.declare(Fact(add_points=('Latvia','IT', 8)))
        self.declare(Fact(explanation="Latvia: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Latvia', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def latvia_engineering(self):
        self.declare(Fact(add_points=('Latvia','Engineering', 9)))
        self.declare(Fact(explanation="Latvia: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Latvia', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def latvia_healthcare(self):
        self.declare(Fact(add_points=('Latvia','Healthcare', 8)))
        self.declare(Fact(explanation="Latvia: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Latvia', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def latvia_business(self):
        self.declare(Fact(add_points=('Latvia','Business', 7)))
        self.declare(Fact(explanation="Latvia: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Latvia', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def latvia_hospitality(self):
        self.declare(Fact(add_points=('Latvia','Hospitality', 6)))
        self.declare(Fact(explanation="Latvia: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Latvia', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def latvia_research(self):
        self.declare(Fact(add_points=('Latvia','Research', 8)))
        self.declare(Fact(explanation="Latvia: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Latvia', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def latvia_spouse_edu(self):
        self.declare(Fact(add_points=('Latvia','SpouseEducation', 15)))
        self.declare(Fact(explanation="Latvia: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Latvia', has_spouse=True, spouse_is_working=True))
    def latvia_spouse_work(self):
        self.declare(Fact(add_points=('Latvia','SpouseWorking', 10)))
        self.declare(Fact(explanation="Latvia: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Latvia', salary_local=P(lambda s: s is not None and s >= 18000)), salience=30)
    def latvia_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Latvia: reported salary meets conservative threshold (18000 EUR)."))

    @Rule(Person(preferred_country='Latvia', num_children=P(lambda n: n is not None and n > 0)))
    def latvia_dependent(self):
        self.declare(Fact(dependent_possible=('Latvia', True)))
        self.declare(Fact(explanation="Latvia: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Latvia'))
    def latvia_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Germany', 'France', 'Italy', 'Netherlands']))
        self.declare(Fact(explanation="Latvia: suggested alternative countries based on climate/culture group."))


# end of Latvia
