# Funnel Server REST API

Authenticated REST API for Server IP Address synchronization

### Virtual Environment

```
virtualenv -p python3 env && source env/bin/activate
```

### Requirements

```
pip3 install django
pip3 install djangorestframework
```

### Creation

```
django-admin startproject funnel . && cd funnel
django-admin.py startapp server && cd ..
```

### Migration

```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Authentication

```
python3 manage.py createsuperuser
```

### Admin User

```
admin:admin5150;
```

### Endpoint

- http://hostname:8000/admin/
- http://hostname:8000/api/server/
