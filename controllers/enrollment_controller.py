from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.enrollment import Enrollment
import repositories.enrollment_repository as enrollment_repository
import repositories.class_repository as class_repository
import repositories.member_repository as member_repository


enrollment_blueprint = Blueprint('enrollment', __name__)

@enrollment_blueprint.route('/enrollments')
def enrollment():
    enrollments = enrollment_repository.select_all()
    return render_template('/enrollments/index.html' ,enrollments = enrollments)

# @enrollment_blueprint.route('/enrollment/<id>')
# def enrollment_show(id):
#     enrollment = enrollment_repository.select(id)
#     return render_template('/enrollments/enrollment.html' ,enrollment=enrollment)

@enrollment_blueprint.route('/enrollment/new')
def new_enrollment():
    members = member_repository.select_all()
    classes = class_repository.select_all()
    return render_template('/enrollments/new.html', members=members, classes=classes)

@enrollment_blueprint.route('/enrollment/signup', methods=['POST'])
def signup():
    member_id = request.form['member_id']
    class_id = request.form['class_id']
    member = member_repository.select(member_id)
    Class = class_repository.select(class_id)
    signup = Enrollment(member, Class)
    enrollment_repository.save(signup)
    return redirect('/enrollments')