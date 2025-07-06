from flask import Blueprint, render_template

view_bp = Blueprint('view', __name__)

@view_bp.route('/')
def index():
    return render_template('index.html')

@view_bp.route('/iris')
def iris():
    return render_template('iris.html')

@view_bp.route('/create-user')
def create_user():
    return render_template('create-user.html')