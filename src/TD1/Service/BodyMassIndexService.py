
class BodyMassIndexService:

    def __init__(self, catdao):
        self.catdao = catdao

    def get_bmi(self, unit, weight, height):
        if height <= 0:
            raise ValueError("Height must be greater than 0.")
        if unit.lower() == "metric":
            return weight / (height ** 2)
        elif unit.lower() == "imperial":
            return 703 * weight / (height ** 2)
        else:
            raise ValueError("Invalid unit.")

    def get_category(self, bmi):
        category = self.catdao.get_category(bmi)
        if category is not None:
            return category.name
        return "Unknown"