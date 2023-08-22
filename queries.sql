create table vacancies (id serial PRIMARY KEY,
                        description text,
                        employer varchar(50),
                        experience varchar(30),
                        salary int,
                        url varchar(100));



create table employers(id serial PRIMARY KEY,
                        company_name varchar(200));