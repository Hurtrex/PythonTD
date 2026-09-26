from src.TD1.Data import MockDB


class CategoryDAO:

    def __init__(self):
        self.datastore = MockDB.get_instance()

    def get_category(self, bmi):
        for category in self.datastore.categories:
            if category.min <= bmi < category.max:
                return category
        return None