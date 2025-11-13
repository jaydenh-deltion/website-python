from flask import Blueprint,render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # Define the login route
def login():
    return render_template("login.html", boolean=True)


@auth.route('/logout')# Define the logout route
def logout():
    return "<p>Logout Page</p>"

@auth.route('/sign-up', methods=['GET', 'POST']) # Define the sign-up route
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error') ## flash message for error. if success use category='success'
        elif len(firstName) < 2:
            flash('First name must be grater than 1 character', category='error') 
        elif password1 != password2:
            flash('password must be at least 7 characters.', category='error') 
        elif len(password1) < 7:
            flash('password must be at least 7 characters.', category='error') 
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")