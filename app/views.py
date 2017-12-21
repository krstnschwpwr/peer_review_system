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
    # if current_user.is_authenticated():
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
# @login_required
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


@app.route('/mypage', methods=['GET'])
@login_required
def index():
    myreviews = Reviewer.query.filter(Reviewer.reviewer_id == current_user.id).first()
    mypapers = Paper.query.filter(Paper.id == myreviews.paper_id).all()
    if 'username' in session:
        username = session['username']
    return render_template('mypage.html', mypapers=mypapers)


# User
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


# Rating
@app.route('/mypage/rating/save', methods=['GET', 'POST'])
def save_rating():
    if request.method == 'POST':
        rating = request.form.get('rating')
        paper_id = request.form.get('paper_id')
        bl = Reviewer.query.filter_by(reviewer_id=current_user.id, paper_id=paper_id).first()
        rat = bl.rating
        bl.rating = rating
        db.session.commit()
        return render_template('thanks.html')
    return render_template('admin.html')


# Submission
@app.route('/submissions', methods=['GET', 'POST'])
def show_submissions():
    papers = []
    all_reviews = Reviewer.query.filter(Reviewer.rating != None).all()
    for a in all_reviews:
        papers.append(Paper.query.filter_by(id=a.paper_id).first())
    return render_template('submission.html', fetch=papers)


# Reviews
@app.route('/review/new', methods=['GET', 'POST'])
@login_required
def save_review():
    paper = Paper.query.all()

    form = ReviewerForm()
    users = User.query.all()

    if request.method == 'POST':
        paper_id = request.form.get('paper_id')
        review = Reviewer(paper_id=paper_id, reviewer_id=request.form.get('dropdown'), rating=10)
        db.session.add(review)
        db.session.commit()
    # return (str(user_id))  #

    return render_template('admin.html', form=form, users=users)


@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    reviewers = Reviewer.query.all()
    return jsonify(reviewers=reviewers_schema.dump(reviewers).data)


# Papers

@app.route('/paper/new', methods=['GET', 'POST'])
@login_required
def save_page():
    paper_form = PaperForm()

    if request.method == 'POST':
        if paper_form.validate_on_submit():
            # Get validated data from form
            title = paper_form.title.data
            abstract = paper_form.abstract.data
            status = request.form.get('status')
            paper = Paper(title, abstract, status="Under Review")
            db.session.add(paper)
            db.session.commit()
            flash('Paper successfully added')
        return redirect('mypage')

    return render_template('newpaper.html', form=paper_form)


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
    return redirect('/page/' + paper_id)


@app.route('/api/papers', methods=['GET'])
@login_required
def get_papers():
    papers = Paper.query.all()
    return jsonify(papers=papers_schema.dump(papers).data)


@app.route('/api/paper/<int:paper_id>', methods=['GET'])
@login_required
def get_paper(paper_id):
    paper = Paper.query.get(paper_id)
    if not paper:
        abort(404)
    return jsonify(paper_schema.dump(paper).data)


@app.route('/api/paper/delete/<int:paper_id>', methods=['GET', 'POST'])
@login_required
def delete_paper(paper_id):
    paper = Paper.query.get(paper_id)
    if not paper:
        abort(404)
    db.session.delete(paper)
    db.session.commit()
    return redirect('mypage')


def make_public_paper(paper):
    new_paper = {}
    for field in paper:
        if field == 'id':
            new_paper['uri'] = url_for('get_papers', paper_id=paper['id'], _external=True)
        else:
            new_paper[field] = paper[field]
    return new_paper


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
