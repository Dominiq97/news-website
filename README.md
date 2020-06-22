# news-website<br>
Django==3.0.7<br>
bootstrap4==0.1.0<br>
Pillow==7.1.2<br>
psycopg2-binary==2.8.5<br>
Python 3.8.2


## Instalare
- clone de pe github
- in directorul creat generam un virtualenv python3
```bash
python3 -m venv .
```

- activam virtualenv
```bash
source bin/activate
```

- instalam requirements
```bash
pip install -r requirements.txt
```

- runserver
```bash
python manage.py runserver
```

## Nota:
Daca nu avem la dispozitie si baza de date (sqlite sau PostgreSQL):
- rulam migrate pt a popula baza de date cu "models"
```bash
python manage.py migrate
```
