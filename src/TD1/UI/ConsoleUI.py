

class ConsoleUI:

    def __init__(self, service):
        self.service = service

    def run(self):
        print("BMI Calculator")

        unit = input("Unit (metric/imperial): ")
        weight = float(input("Weight: "))
        height = float(input("Height: "))

        bmi = self.service.get_bmi(unit, weight, height)
        category = self.service.get_category(bmi)

        print("BMI:", round(bmi, 2))
        print("Category:", category)

