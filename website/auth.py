# ------------------------------
# Imports
# ------------------------------
from flask import Blueprint, render_template, request, flash, redirect, url_for
import re

# ------------------------------
# Blueprint setup
# ------------------------------
# 'auth' blueprint handles authentication routes (login, logout, sign-up)
auth = Blueprint('auth', __name__)

# ------------------------------
# Login route
# ------------------------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Handle both GET (show page) and POST (form submit)
    data = request.form
    print(data)  # Debug: print submitted form data to the console

    # Render login page
    return render_template('login.html')

# ------------------------------
# Logout route
# ------------------------------
@auth.route('/logout')
def logout():
    # Placeholder logout page (will later clear session, etc.)
    return "logout page"

# ------------------------------
# Sign-Up route
# ------------------------------
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # Check if form is submitted (POST request)
    if request.method == 'POST':
        # Get data from form fields
        email = request.form.get('email')
        fname = request.form.get('fname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Regular expression for validating email format
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        # ------------------------------
        # Input Validation
        # ------------------------------
        if not email:
            flash('Email is required.', category='error')
        elif not fname:
            flash('First name is required.', category='error')
        elif not password:
            flash('Password is required.', category='error')
        elif not confirm_password:
            flash('Please confirm your password.', category='error')
        elif not re.match(email_pattern, email):
            flash('Please enter a valid email address.', category='error')
        elif len(fname) < 3:
            flash('First name must be greater than 2 characters.', category='error')
        elif password != confirm_password:
            flash('Passwords do not match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters long.', category='error')
        else:
            # If all validations pass
            flash('Account created successfully!', category='success')
            
            # Redirect user to login page after successful sign-up
            return redirect(url_for('auth.login'))
    
    # Render the sign-up page (for GET requests)
    return render_template('sign_up.html')
