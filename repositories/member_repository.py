from db.run_sql import run_sql
from models.member import Member
from models.Class import Class #capital C in .Class to avoid conflict
from models.enrollment import enrollment

def save(member):
    sql = "INSERT INTO members (first_name, last_name, age, membership_type) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.age, member.membership_type]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member





def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)