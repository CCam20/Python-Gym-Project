from db.run_sql import run_sql
from models.member import Member
from models.Class import Class #capital C in .Class to avoid conflict
from models.enrollment import Enrollment

def save(enrollments):
    sql = "INSERT INTO enrollments (member_id, class_id) VALUES (%s, %s) RETURNING id"
    values = [enrollments.member.id, enrollments.Class.id]
    results = run_sql(sql, values)
    enrollments.id = results[0]['id']
    return enrollments


def select_all():
    enrollments = []
    sql= "SELECT * FROM enrollments"
    results=run_sql(sql)

    for row in results:
        enrollment = Enrollment(row['member_id'], row['class_id'], row['id'])
        enrollments.append(enrollment)
    return enrollments

def select(id):
    enrollment = None
    sql = "SELECT * FROM enrollments WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        enrollment = Enrollment(result['member_id'], result['class_id'], result['id'])
    return enrollment

def delete(id):
    sql = "DELETE FROM enrollments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM enrollments"
    run_sql(sql)