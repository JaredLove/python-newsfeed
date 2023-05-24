# importing the functions blueprint and render_template from the flask module
from flask import Blueprint, render_template

# setting the blueprint function to the object of bp
# This time, using the url_prefix argument, we prefix every route in the blueprint with /dashboard. 
# The routes thus become /dashboard and /dashboard/edit/<id> when registered with the app
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# blueprint route for the dashboard
@bp.route('/')
def dash():
    return render_template('dashboard.html')

# blueprint route for editing a post with the parameter of id
@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')