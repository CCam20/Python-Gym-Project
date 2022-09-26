from db.run_sql import run_sql
from models.member import Member
from models.Class import Class #capital C in .Class to avoid conflict
from models.enrollment import Enrollment

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

def select(id):
    value = None
    sql = "SELECT * FROM classes WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        value = Class(result['name'], result['type'], result['id'])
    return value

def members(enrollment):
    members =[]
    sql="SELECT members.* FROM members INNER JOIN enrollments ON enrollments.member_id = members.id WHERE enrollment_id = %s" 
    values = [enrollment.id]
    results = run_sql(sql,values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['membership_type'], row['id'])
        members.append(member)
    return member

def update(Class):
    sql = "UPDATE classes SET (name, type) = (%s, %s)WHERE id = %s"
    values = [Class.name, Class.type, Class.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)