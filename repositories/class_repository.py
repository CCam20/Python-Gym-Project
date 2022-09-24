from db.run_sql import run_sql
from models.member import Member
from models.Class import Class #capital C in .Class to avoid conflict
from models.enrollment import enrollment

def save(Class):
    sql = 'INSERT INTO classes (name, type) VALUES (%s, %s) RETURNING id'
    values = [Class.name, Class.type]
    results = run_sql(sql, values)
    Class.id = results[0]['id']
    return Class

def select_all():
    classes = []
    sql= "SELECT * FROM classes"
    results=run_sql(sql)

    for row in results:
        result = Class(row['name'], row['type'], row['id'])
        classes.append(result)
    return classes




def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)