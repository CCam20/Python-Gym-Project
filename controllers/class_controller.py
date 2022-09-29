from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.enrollment_controller import enrollment
from models.Class import Class
import repositories.class_repository as class_repository
import repositories.member_repository as member_repository
import repositories.enrollment_repository as enrollment_repository

class_blueprint = Blueprint('class', __name__)

@class_blueprint.route('/classes')
def classes():
        classes = class_repository.select_all()
        return render_template('/classes/index.html', classes = classes)


@class_blueprint.route("/class/<id>")
def show_class(id):
    Class = class_repository.select(id)
    members =class_repository.members(Class)
    enrollments = enrollment_repository.enrollments(Class)
    return render_template('/classes/class.html', Class=Class, members=members, enrollments=enrollments)

@class_blueprint.route('/classes/new')
def new():
    return render_template('/classes/new.html')

@class_blueprint.route('/classes/add_class', methods=['POST'])
def new_class():
    name= request.form['class_name']
    type= request.form['class_type']
    date= request.form['class_date']
    capacity = request.form['class_capacity']
    i = date.split("-")
    date = i[1]+'-'+i[2]+'-'+i[0]
    new_class= Class(name, type, date, capacity)
    class_repository.save(new_class)
    return redirect('/classes')

@class_blueprint.route('/class/delete/<id>', methods=['POST'])
def delete(id):
    class_repository.delete(id)
    return redirect("/classes")

@class_blueprint.route('/class/delete_from_member/<id>', methods=['POST'])
def delete_from_member(id):
    class_repository.delete(id)
    return redirect("/members")

@class_blueprint.route("/class/edit/<id>", methods=['GET'])
def edit_member(id):
    Class = class_repository.select(id)
    return render_template('classes/edit.html', Class=Class)

@class_blueprint.route('/class/update/<id>', methods=['POST'])
def update_member(id):
    name= request.form['name']
    type= request.form['type']
    date = request.form['date']
    capacity = request.form['capacity']
    updated_member= Class(name, type, date, capacity, id)
    class_repository.update(updated_member)
    return redirect('/classes')