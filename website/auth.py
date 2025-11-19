from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user# Import necessary functions from flask_login



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # Define the login route
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) # Log the user in
                return redirect(url_for('views.home'))                
            else:
                flash('Incorrect password, try again.', category='error')
        else:
             flash('email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout') # Define the logout route
@login_required # Ensure the user is logged in to access this route
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST']) # Define the sign-up route
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error') ## flash message for error. if success use category='success'
        elif len(first_name) < 2:
            flash('First name must be grater than 1 character', category='error') 
        elif password1 != password2:
            flash('password must be at least 7 characters.', category='error') 
        elif len(password1) < 7:
            flash('password must be at least 7 characters.', category='error') 
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)