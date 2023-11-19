# HOnboarding

## Frontend

```
cd frontend
npm install
npm run dev
```

## Backend

- Mac / Linux
```
cd backend
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```



- Windows
```
cd backend
py -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```
