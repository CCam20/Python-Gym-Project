from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member

import repositories.member_repository as member_repository

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)

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