from app import app, db, lm
from flask import render_template, request, redirect, g, url_for, flash, jsonify, json, abort
from flask_login import login_user, login_required, logout_user, current_user, session
from app.forms import RegisterForm, LoginForm
from app.models import User, bcrypt
from app.schema import users_schema, user_schema





@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/api/user/add', methods=['POST', 'GET'])
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
            return redirect(url_for('home'))

            flash_errors(user_form)

    return render_template('register.html', form=user_form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    #if current_user.is_authenticated():
     #   return redirect(url_for('home'))
    form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and bcrypt.check_password_hash(
                    user.password, request.form['password']
            ):
                login_user(user)
                flash('Hi' + 'You just signed up')
                session['logged_in'] = True
                return render_template('mypage.html')

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@app.route("/logout")
def logout():
    logout_user()
    session['logged_in'] = False
    return home()

#API

@app.route('/api/users', methods=['GET'])
def get_users():
  users = User.query.all()
  return jsonify(users=users_schema.dump(users).data)

@app.route('/api/user/<int:id>', methods=['GET'])
def get_space(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    return jsonify(user_schema.dump(user).data)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
