import psycopg2


class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(host='localhost',
                                     database='vacancy',
                                     user='postgres',
                                     password='qwerty')

    def safe_vacancy(self, vacancies: list[dict]):
        employeers = []
        with self.conn.cursor() as cursor:
            for vacancy in vacancies:
                cursor.execute(
                    f'insert into vacancies(description, employer, experience, salary, url)'
                    f'values (%s, %s, %s, %s, %s)',
                    (vacancy.get('description'), vacancy['employeer'].lower(), vacancy['experience'], vacancy['salary'],
                     vacancy['url']))
                if vacancy['employeer'] not in employeers:
                    employeers.append(vacancy['employeer'])
        self.conn.commit()
        self.safe_employeers(employeers)  # Связка двух методов

    def safe_employeers(self, employeers: list[str]):
        with self.conn.cursor() as cursor:
            for employer in employeers:
                cursor.execute('select id from employers where company_name = %s', [employer.lower()])
                if not cursor.fetchall():
                    cursor.execute('insert into employers(company_name) values(%s)', [employer])
            self.conn.commit()

    def get_companies_and_vacancies_count(self):
        with self.conn.cursor() as cursor:
            cursor.execute('select count(id), employer from vacancies group by employer')
            #print(cursor.fetchall())
            for company_name, count in cursor.fetchall():
                print(f"company: {count}, count: {company_name}")

    def get_all_vacancies(self):
        with self.conn.cursor() as cursor:
            cursor.execute('select * from vacancies')
            for vacancy in cursor.fetchall():
                print(f"discription: {vacancy[1]}, employeer: {vacancy[2]}, experience: {vacancy[3]},"
                      f" salary: {vacancy[4]}, url: {vacancy[-1]}")


    def get_avg_salary(self):
        with self.conn.cursor() as cursor:
            cursor.execute('select avg(salary) from vacancies')
            print(round(cursor.fetchall()[0][0]))

    def get_vacancies_with_higher_salary(self):
        with self.conn.cursor() as cursor:
            cursor.execute(f'select * from vacancies where salary > {self.get_avg_salary()}')
            for vacancy in cursor.fetchall():
                print(vacancy[1])
            #print(cursor.fetchall())
            #print(self.get_avg_salary()


    def get_vacancies_with_keyword(self, *keyword: str):
        with self.conn.cursor() as cursor:
            cursor.execute(f"select * from vacancies where position(%s in description)>0", keyword)
            for vacancy in cursor.fetchall():
                print((vacancy[1]))


manager = DBManager()
#manager.safe_vacancy()
#print(manager.get_all_vacancies())
#print(manager.get_companies_and_vacancies_count())
#print(manager.get_vacancies_with_keyword('Спец'))
#print(manager.get_avg_salary())

