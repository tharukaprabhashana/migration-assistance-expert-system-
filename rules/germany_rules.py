# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class GermanyRules:
    """Rules for Germany"""
    @Rule(Person(preferred_country='Germany', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def germany_strong(self):
        self.declare(Fact(eligibility=('Germany', 'TopPath', 0.95)))
        self.declare(Fact(points=('Germany', 80)))
        self.declare(Fact(explanation="Germany: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Germany', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def germany_medium(self):
        self.declare(Fact(eligibility=('Germany', 'MidPath', 0.85)))
        self.declare(Fact(points=('Germany', 65)))
        self.declare(Fact(explanation="Germany: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Germany', role='student'), salience=60)
    def germany_student(self):
        self.declare(Fact(eligibility=('Germany', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Germany', 35)))
        self.declare(Fact(explanation="Germany: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Germany', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def germany_it(self):
        self.declare(Fact(add_points=('Germany','IT', 12)))
        self.declare(Fact(explanation="Germany: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Germany', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def germany_engineering(self):
        self.declare(Fact(add_points=('Germany','Engineering', 14)))
        self.declare(Fact(explanation="Germany: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Germany', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def germany_healthcare(self):
        self.declare(Fact(add_points=('Germany','Healthcare', 12)))
        self.declare(Fact(explanation="Germany: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Germany', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def germany_business(self):
        self.declare(Fact(add_points=('Germany','Business', 10)))
        self.declare(Fact(explanation="Germany: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Germany', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def germany_hospitality(self):
        self.declare(Fact(add_points=('Germany','Hospitality', 6)))
        self.declare(Fact(explanation="Germany: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Germany', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def germany_research(self):
        self.declare(Fact(add_points=('Germany','Research', 12)))
        self.declare(Fact(explanation="Germany: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Germany', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def germany_spouse_edu(self):
        self.declare(Fact(add_points=('Germany','SpouseEducation', 15)))
        self.declare(Fact(explanation="Germany: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Germany', has_spouse=True, spouse_is_working=True))
    def germany_spouse_work(self):
        self.declare(Fact(add_points=('Germany','SpouseWorking', 10)))
        self.declare(Fact(explanation="Germany: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Germany', salary_local=P(lambda s: s is not None and s >= 50000)), salience=30)
    def germany_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Germany: reported salary meets conservative threshold (50000 EUR)."))

    @Rule(Person(preferred_country='Germany', num_children=P(lambda n: n is not None and n > 0)))
    def germany_dependent(self):
        self.declare(Fact(dependent_possible=('Germany', True)))
        self.declare(Fact(explanation="Germany: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Germany'))
    def germany_alternatives(self):
        self.declare(Fact(alternative_suggestions=['France', 'Italy', 'Netherlands', 'Latvia']))
        self.declare(Fact(explanation="Germany: suggested alternative countries based on climate/culture group."))


# end of Germany
