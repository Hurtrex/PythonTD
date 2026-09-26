
from src.TD1.Dao import CategoryDAO
from src.TD1.Service import BodyMassIndexService
from src.TD1.UI import ConsoleUI

categoryDAO = CategoryDAO()
service = BodyMassIndexService(categoryDAO)
ui = ConsoleUI(service)
ui.run()