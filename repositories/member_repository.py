from db.run_sql import run_sql
from models.member import Member
from models.Class import Class #capital C in .Class to avoid conflict
from models.enrollment import Enrollment

def save(member):
    sql = "INSERT INTO members (first_name, last_name, age, membership_type) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.age, member.membership_type]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member


def select_all():
    members = []
    sql= "SELECT * FROM members"
    results=run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['membership_type'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['first_name'], result['last_name'], result['age'], result['membership_type'], result['id'])
    return member

def classes(enrollment):
    classes =[]
    sql="SELECT classes.* FROM classes INNER JOIN enrollments ON enrollments.class_id = classes.id WHERE enrollment_id = %s" 
    values = [enrollment.id]
    results = run_sql(sql,values)

    for row in results:
        classs = Class(row['first_name'], row['last_name'], row['age'], row['membership_type'], row['id'])
        classes.append(classs)
    return classes

def update(member):
    sql = "UPDATE members SET (first_name, last_name, age, membership_type) = (%s, %s, %s, %s)WHERE id = %s"
    values = [member.first_name, member.last_name, member.age, member.membership_type, member.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)