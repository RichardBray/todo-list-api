# Creating a basic REST api with Tornado

The title pretty much explains it.


## Install

`pip install -r requirements.txt`

`python app.py`

## Extra Stuff

### Save pip packages to requirements file

`pip freeze > requirements.txt`

### MySQLdb

`pip install mysqlclient`


### List comprehension

```py
# result = list(filter(lambda item: item['id'] == int(id), items))
result = [item for item in items if item['id'] == int(id)]
```

## SQL Queries

Create Schema or Database
```sql
CREATE SCHEMA `<schema_name>`;
CREATE DATABASE `<database_name>`;
```

Choose database
```sql
USE <database_name>
```

Show all tables in database

```sql
SHOW tables;
```

```py
cursor.execute("SELECT VERSION()")  # Test database connected
```
