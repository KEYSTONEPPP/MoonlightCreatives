from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)
@auth.route('/auth', methods =['GET', 'POST'])
def code():
    return render_template('code.html')
