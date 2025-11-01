# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class FranceRules:
    """Rules for France"""
    @Rule(Person(preferred_country='France', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def france_strong(self):
        self.declare(Fact(eligibility=('France', 'TopPath', 0.95)))
        self.declare(Fact(points=('France', 80)))
        self.declare(Fact(explanation="France: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='France', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def france_medium(self):
        self.declare(Fact(eligibility=('France', 'MidPath', 0.85)))
        self.declare(Fact(points=('France', 65)))
        self.declare(Fact(explanation="France: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='France', role='student'), salience=60)
    def france_student(self):
        self.declare(Fact(eligibility=('France', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('France', 35)))
        self.declare(Fact(explanation="France: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='France', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def france_it(self):
        self.declare(Fact(add_points=('France','IT', 10)))
        self.declare(Fact(explanation="France: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='France', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def france_engineering(self):
        self.declare(Fact(add_points=('France','Engineering', 10)))
        self.declare(Fact(explanation="France: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='France', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def france_healthcare(self):
        self.declare(Fact(add_points=('France','Healthcare', 10)))
        self.declare(Fact(explanation="France: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='France', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def france_business(self):
        self.declare(Fact(add_points=('France','Business', 9)))
        self.declare(Fact(explanation="France: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='France', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def france_hospitality(self):
        self.declare(Fact(add_points=('France','Hospitality', 7)))
        self.declare(Fact(explanation="France: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='France', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def france_research(self):
        self.declare(Fact(add_points=('France','Research', 12)))
        self.declare(Fact(explanation="France: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='France', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def france_spouse_edu(self):
        self.declare(Fact(add_points=('France','SpouseEducation', 15)))
        self.declare(Fact(explanation="France: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='France', has_spouse=True, spouse_is_working=True))
    def france_spouse_work(self):
        self.declare(Fact(add_points=('France','SpouseWorking', 10)))
        self.declare(Fact(explanation="France: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='France', salary_local=P(lambda s: s is not None and s >= 32000)), salience=30)
    def france_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="France: reported salary meets conservative threshold (32000 EUR)."))

    @Rule(Person(preferred_country='France', num_children=P(lambda n: n is not None and n > 0)))
    def france_dependent(self):
        self.declare(Fact(dependent_possible=('France', True)))
        self.declare(Fact(explanation="France: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='France'))
    def france_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Germany', 'Italy', 'Netherlands', 'Latvia']))
        self.declare(Fact(explanation="France: suggested alternative countries based on climate/culture group."))


# end of France
