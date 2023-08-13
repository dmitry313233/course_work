import requests
from pprint import pprint


class Pars:

    def get_vacansions(self, name_companies: list[str], key_word: list[str]):
        lst = []
        words = '+'.join(key_word)
        employeers_id = self.get_employeers(name_companies)
        for i in employeers_id:
            URL = f'https://api.hh.ru/vacancies?per_page=15&employer_id={i["id"]}&text={words}'
            responce = requests.get(URL).json()
            if responce['items']:
                pprint(responce['items'])
                for j in responce['items']:
                    lst.append(self.pars_vanshions(j, i['company']))
        return lst

    def get_employeers(self, name_companies: list[str]):
        employeer_id = []
        for name in name_companies:
            URL = f'https://api.hh.ru/employers?text={name}&only_with_vacancies=True'
            responce = requests.get(URL).json()
            for id_company in responce['items']:
                employeer_id.append({'company': name, 'id': id_company['id']})
        return employeer_id

    def pars_vanshions(self, vacansi: dict, company: str):
        employeer = company
        description = vacansi['name']  # it is j
        url = vacansi['alternate_url'] # j
        salary = self.get_salary(vacansi['salary']) #j
        experience = vacansi['experience']['name']
        vacanci = {'employeer': employeer,
                   'description': description, 'url': url,
                   'experience': experience, 'salary': salary}
        return vacanci

    def get_salary(self, salary: dict | None):
        if salary:
            if salary['from'] and salary['to']:
                return (salary['from'] + salary['to']) // 2
            elif salary['from']:
                return salary['from']
            elif salary['to']:
                return salary['to']
        else:
            return 0


# URL = 'https://api.hh.ru/vacancies'
# responce = requests.get(URL).json()
# employer = []
# print(responce)
# for i in responce['items']:
#     employer.append(i['premium'])
#     #print(i['salary'])
#     print(employer)


#pars = Pars()
#pprint(pars.get_vacansions(['МТС'], []))
# print(pars.get_employeers(['ozon', 'avito']))