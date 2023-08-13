from DBManager import DBManager
from hh import Pars

dbmanager = DBManager()
pars = Pars()
print(dbmanager.safe_vacancy(pars.get_vacansions(['Билайн'], [])))

