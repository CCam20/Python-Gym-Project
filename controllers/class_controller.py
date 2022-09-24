from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.Class import Class
import reposirories.class_repository as class_reposttory

class_blueprint = Blueprint('class', __name__)

