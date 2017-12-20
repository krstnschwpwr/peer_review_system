from app import app, db
from flask import render_template, request, redirect, g, url_for, flash, jsonify, json, abort, make_response
from flask_login import login_user, login_required, logout_user, current_user, session
from app.forms import RegisterForm, LoginForm, PaperForm, ReviewerForm
from app.models import User, bcrypt, Paper, Reviewer
from app.schema import users_schema, user_schema, paper_schema, papers_schema, reviewers_schema



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
                user.authenticated = True
                login_user(user)
                session['logged_in'] = True
                if user.email == 'admin@admin.com':
                    return redirect('/admin')
                else:
                    return redirect('/mypage')

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@app.route("/admin")
#@login_required
def admin():
    paper = Paper.query.all()

    form = ReviewerForm()
    users = User.query.all()
    user_id = request.form.get('dropdown')


   # form.all_users.choices = users.i
    return render_template('admin.html', user_id=user_id, form=form, paper=paper, users=users)


@app.route("/logout")
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    session['logged_in'] = False
    return home()
#
# #CRUD
# @app.route('/paper/new')
# #@auth.login_required
# def new_page():
#     return render_template('newpaper.html')


@app.route('/mypage')
@login_required
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"
    return render_template('mypage.html')


@app.route('/api/users', methods=['GET'])
@login_required
def get_users():
  users = User.query.all()
  return jsonify(users=users_schema.dump(users).data)

@app.route('/api/user/<int:id>', methods=['GET'])
@login_required
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    return jsonify(user_schema.dump(user).data)


@app.route('/review/new', methods=['GET', 'POST'])
@login_required
def save_review():
    paper = Paper.query.all()

    form = ReviewerForm()
    users = User.query.all()

    if request.method == 'POST':
        paper_id = request.form.get('paper_id')
        review = Reviewer(paper_id=paper_id, reviewer_id=request.form.get('dropdown'), rating=1)
        db.session.add(review)
        db.session.commit()
    #return (str(user_id))  #

    return render_template('admin.html', form=form, users = users)
##Papers

@app.route('/paper/new', methods=['GET', 'POST'])
@login_required
def save_page():
    paper_form = PaperForm()

    if request.method == 'POST':
        if paper_form.validate_on_submit():
            # Get validated data from form
            title = paper_form.title.data
            abstract = paper_form.abstract.data
            status = paper_form.status.data
            paper = Paper(title, abstract, reviewer_id=1, status="Under Review")
            db.session.add(paper)
            db.session.commit()
            flash('Paper successfully added')
        return redirect('mypage')

    return render_template('newpaper.html', form=paper_form)


def make_public_paper(paper):
	new_paper = {}
	for field in paper:
		if field == 'id':
			new_paper['uri'] = url_for('get_papers', paper_id = paper['id'], _external = True)
		else:
			new_paper[field] = paper[field]
	return new_paper


# @app.route('/paper/<int:paper_id>/delete', methods=['DELETE'])
# #@auth.login_required
# def delete_paper(paper_id):
#     qry = db.session.query(Paper).filter(
#         Paper.id == id)
#     paper = qry.first()
#
#     if paper:
#         form = PaperForm(formdata=request.form, obj=paper)
#         if request.method == 'POST' and form.validate():
#             # delete the item from the database
#             db.session.delete(z)
#             db_session.commit()
#
#             flash('Album deleted successfully!')
#             return redirect('/')
#         return render_template('delete_album.html', form=form)
#     else:
#         return 'Error deleting #{id}'.format(id=id)
#
#     db.session.query(Paper).filter_by(id=paper_id).delete()
#     db.session.commit()
#     return redirect('/mypage')


@app.route('/paper/<int:paper_id>/update', methods=['POST'])
@login_required
def update_page(paper_id):
    paper_id = request.form['id']
    title = request.form['title']
    abstract = request.form['abstract']
    status = request.form['status']
    db.session.query(Paper).filter_by(id=paper_id).update({'title': title,
                                                          'abstract': abstract,
                                                           'status': status})
    db.session.commit()
    return redirect('/page/'+paper_id)


@app.route('/api/papers', methods=['GET'])
@login_required
def get_papers():
  papers = Paper.query.all()
  return jsonify(papers=papers_schema.dump(papers).data)

# @app.route('/api/reviews', methods=['GET', 'POST'])
# def save_review():

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
  reviewers = Reviewer.query.all()
  return jsonify(reviewers=reviewers_schema.dump(reviewers).data)


@app.route('/api/paper/<int:paper_id>', methods=['GET'])
@login_required
def get_paper(paper_id):
    paper = Paper.query.get(paper_id)
    if not paper:
        abort(404)
    return jsonify(paper_schema.dump(paper).data)


@app.route('/api/paper/delete/<int:paper_id>', methods=['GET', 'POST'])
def delete_paper(paper_id):
    paper = Paper.query.get(paper_id)
    if not paper:
        abort(404)
    db.session.delete(paper)
    db.session.commit()
    return redirect('mypage')




# @app.route('/api/user/<int:id>/paper/<int:id>', methods=['GET'])
# def get_users_paper(id):
#     user = User.query.get(id)
#     if not user:
#         abort(404)
#     return jsonify(user_schema.dump(user).data)

# @app.errorhandler(404)
# def not_found(error):
# 	return make_response(jsonify({ 'error' : 'Not Found' }), 404)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
