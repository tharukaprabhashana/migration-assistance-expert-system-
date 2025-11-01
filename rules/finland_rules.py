# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class FinlandRules:
    """Rules for Finland"""
    @Rule(Person(preferred_country='Finland', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def finland_strong(self):
        self.declare(Fact(eligibility=('Finland', 'TopPath', 0.95)))
        self.declare(Fact(points=('Finland', 80)))
        self.declare(Fact(explanation="Finland: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Finland', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def finland_medium(self):
        self.declare(Fact(eligibility=('Finland', 'MidPath', 0.85)))
        self.declare(Fact(points=('Finland', 65)))
        self.declare(Fact(explanation="Finland: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Finland', role='student'), salience=60)
    def finland_student(self):
        self.declare(Fact(eligibility=('Finland', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Finland', 35)))
        self.declare(Fact(explanation="Finland: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Finland', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def finland_it(self):
        self.declare(Fact(add_points=('Finland','IT', 11)))
        self.declare(Fact(explanation="Finland: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Finland', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def finland_engineering(self):
        self.declare(Fact(add_points=('Finland','Engineering', 11)))
        self.declare(Fact(explanation="Finland: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Finland', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def finland_healthcare(self):
        self.declare(Fact(add_points=('Finland','Healthcare', 10)))
        self.declare(Fact(explanation="Finland: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Finland', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def finland_business(self):
        self.declare(Fact(add_points=('Finland','Business', 10)))
        self.declare(Fact(explanation="Finland: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Finland', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def finland_hospitality(self):
        self.declare(Fact(add_points=('Finland','Hospitality', 6)))
        self.declare(Fact(explanation="Finland: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Finland', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def finland_research(self):
        self.declare(Fact(add_points=('Finland','Research', 12)))
        self.declare(Fact(explanation="Finland: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Finland', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def finland_spouse_edu(self):
        self.declare(Fact(add_points=('Finland','SpouseEducation', 15)))
        self.declare(Fact(explanation="Finland: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Finland', has_spouse=True, spouse_is_working=True))
    def finland_spouse_work(self):
        self.declare(Fact(add_points=('Finland','SpouseWorking', 10)))
        self.declare(Fact(explanation="Finland: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Finland', salary_local=P(lambda s: s is not None and s >= 35000)), salience=30)
    def finland_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Finland: reported salary meets conservative threshold (35000 EUR)."))

    @Rule(Person(preferred_country='Finland', num_children=P(lambda n: n is not None and n > 0)))
    def finland_dependent(self):
        self.declare(Fact(dependent_possible=('Finland', True)))
        self.declare(Fact(explanation="Finland: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Finland'))
    def finland_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Norway', 'Sweden', 'Denmark']))
        self.declare(Fact(explanation="Finland: suggested alternative countries based on climate/culture group."))


# end of Finland
