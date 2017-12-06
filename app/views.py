from app import app, db, lm
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from app.forms import RegisterForm, LoginForm
from app.models import User, bcrypt

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    user_form = RegisterForm()

    if request.method == 'POST':
        if user_form.validate_on_submit():
            # Get validated data from form
            name = user_form.name.data
            email = user_form.email.data
            password = user_form.password.data

            # save user to database
            user = User(name, email, password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('User successfully added')
            return redirect(url_for('show_users'))

    flash_errors(user_form)

    return render_template('register.html', form=user_form)

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and bcrypt.check_password_hash(
                    user.password, request.form['password']
            ):
                login_user(user)
                flash('You were logged in. Go Crazy.')
                return render_template('mypage.html')

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)

@app.route('/users')
def show_users():
    users = db.session.query(User).all() # or you could have used User.query.all()

    return render_template('show_users.html', users=users)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
