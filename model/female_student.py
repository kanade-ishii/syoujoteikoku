class FemaleStudent:
    def __init__(
        self,
        base_calorie_requirement,
        daily_water_requirement,
        survival_ability,
        sickness_probability,
        injury_probability,
    ):
        self.food = base_calorie_requirement
        self.water = daily_water_requirement
        self.base_calorie_requirement = base_calorie_requirement
        self.daily_water_requirement = daily_water_requirement
        self.survival_ability = survival_ability
        self.sickness_probability = sickness_probability
        self.injury_probability = injury_probability
        self.current_health = 100
        self.injury = 0
        self.stress = 0
        self.is_dead = False
