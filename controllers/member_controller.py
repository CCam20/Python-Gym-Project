from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.enrollment_controller import enrollment
from models.member import Member
import repositories.class_repository as class_repository
import repositories.member_repository as member_repository
import repositories.enrollment_repository as enrollment_repository

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)

@members_blueprint.route("/member/<id>")
def show_member(id):
    member = member_repository.select(id)
    classes = member_repository.classes(member)
    enrollments = enrollment_repository.select_all()
    return render_template("/members/member.html", member = member, classes=classes ,enrollments=enrollments)

@members_blueprint.route('/members/new')
def new():
    return render_template('members/new.html')

@members_blueprint.route('/members/add_member', methods=['POST'])
def new_member():
    first_name= request.form['first_name']
    last_name= request.form['last_name']
    age= request.form['age']
    membership_type= request.form['membership_type']
    new_member= Member(first_name, last_name, age, membership_type)
    member_repository.save(new_member)
    return redirect('/members')

@members_blueprint.route('/members/delete/<id>', methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members')

@members_blueprint.route("/class/edit/<id>", methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    # classes = class_repository.select_all()
    return render_template('members/edit.html', member=member)

@members_blueprint.route('/class/update/<id>', methods=['POST'])
def update_member(id):
    first_name= request.form['first_name']
    last_name= request.form['last_name']
    age= request.form['age']
    membership_type= request.form['membership_type']
    updated_member= Member(first_name, last_name, age, membership_type, id)
    member_repository.update(updated_member)
    return redirect('/members')