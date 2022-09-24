from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.Class import Class
import repositories.class_repository as class_repository

class_blueprint = Blueprint('class', __name__)

