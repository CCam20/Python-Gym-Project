from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.Class import Class
import repositories.class_repository as class_repository

class_blueprint = Blueprint('class', __name__)

@class_blueprint.route('/classes')
def classes():
        classes = class_repository.select_all()
        return render_template('/classes/index.html', classes = classes)

@class_blueprint.route('/classes/new')
def new():
    return render_template('classes/new.html')

@class_blueprint.route('/classes/add_class', methods=['POST'])
def new_class():
    name= request.form['class_name']
    type= request.form['class_type']
    new_class= Class(name, type)
    class_repository.save(new_class)
    return redirect('/classes')