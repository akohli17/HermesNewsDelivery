from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, redirect, request, url_for, flash, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from dnd.models import User, Interest, Article
from dnd.forms import RegisterForm, LoginForm, UpdateUserInterestsForm
from dnd.news import getNews
from dnd import app, db
from flask_bootstrap import Bootstrap
from json import load
from .interests import dataTree

bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    session['logged_in'] = False
    return render_template('indexnew.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dropdown', methods=['GET', 'POST'])
def tryForm():

    dropdown_html = dropdownGenerator()

    return render_template('dropdown.html', dropdown_html=dropdown_html)

def dropdownGenerator():
    resultsStr = ''
    for i in dataTree:

        resultsStr += '<li><a class="toggle" href="javascript:void(0);" value="' \
            + i + '">' + i + '</a><ul class="inner">'
        resultsStr += recursiveDropdown(dataTree[i])
        resultsStr += '</ul></li>'
    return resultsStr


def recursiveDropdown(dictTree):

    resultsStr = ''
    for i in dictTree:

        resultsStr += '<li><a class="toggle" href="#" value="' \
            + i + '">' + i + '</a><ul class="inner">'
        resultsStr += recursiveDropdown(dictTree[i])
        resultsStr += '</ul></li>'
    return resultsStr

@app.route('/storeinitialinterests', methods=['GET', 'POST'])
def storeinitialinterests():
    interest1 = request.args['interest1']
    interest2 = request.args['interest2']
    interest3 = request.args['interest3']

    print(interest1)
    print(interest2)
    print(interest3)
    return redirect(url_for('dashboard'))



@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route('/searchresults', methods=['GET', 'POST'])
def searchResults():
    # # store clicks in a database
    # url_link = request.args.get('parameters')

    # if url_link:
    #     t = float(request.args.get('t'))/1000.0
    #     interest = request.args.get('interest')
    #     title = request.args.get('title')
    #     print(url_link, ' ', t, ' ', interest)
    #     if not Article.query.filter_by(id=url_link).count():
    #         article = Article(id=url_link, t=t, user=current_user, interest=interest, title=title)
    #         db.session.add(article)
    #         db.session.commit()
    #     else:
    #         Article.query.filter_by(id=url_link).first().t += t
    #         db.session.commit()
    query = request.args.get('Query')
    dict_news = {}
    dict_news = getNews(query)
    return render_template('searchresults2.html', name=current_user.username, dict_news=dict_news, session=session)

@app.route('/setinterests', methods=['GET', 'POST'])
@login_required
def setinterests():

    dropdown_html = dropdownGenerator()

    return render_template('setinterestsModal.html', dropdown_html=dropdown_html)

@app.route('/userstats')
def userstats():
    return render_template('userstats.html', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        session['logged_in'] = True
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=form.remember.data)
        session['logged_in'] = True
        flash('Congratulations! Your account has been created!', 'success')
        return redirect(url_for('setinterests_old'))
        #return '<h1>New user has been created!</h1>'

    return render_template('signup.html', form=form)

@app.route('/setinterests_old', methods=['GET', 'POST'])
@login_required
def setinterests_old():
    form = UpdateUserInterestsForm()

    if form.is_submitted():
        interest_1 = Interest(interest=form.interest_1.data, user=current_user)
        db.session.add(interest_1)
        interest_2 = Interest(interest=form.interest_2.data, user=current_user)
        db.session.add(interest_2)
        interest_3 = Interest(interest=form.interest_3.data, user=current_user)
        db.session.add(interest_3)
        db.session.commit()
        flash('Update successful!', 'success')
        return redirect(url_for('dashboard'))
    # elif request.method == 'GET':
    #     form.interest.data = Interest.query.filter_by(userWithInterest=current_user).first()
    return render_template('setinterests.html', form=form)

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    formInterests = UpdateUserInterestsForm()

    if formInterests.is_submitted():
        Interest.query.filter_by(user=current_user).delete()
        interest_1 = Interest(interest=formInterests.interest_1.data, user=current_user)
        db.session.add(interest_1)
        interest_2 = Interest(interest=formInterests.interest_2.data, user=current_user)
        db.session.add(interest_2)
        interest_3 = Interest(interest=formInterests.interest_3.data, user=current_user)
        db.session.add(interest_3)
        db.session.commit()
        flash('Update successful!', 'success')
        return redirect(url_for('dashboard'))
    # elif request.method == 'GET':
    #     form.interest.data = Interest.query.filter_by(userWithInterest=current_user).first()
    return render_template('settings.html', user=current_user, form=formInterests)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():

    # store clicks in a database
    url_link = request.args.get('parameters')

    if url_link:
        t = float(request.args.get('t'))/1000.0
        interest = request.args.get('interest')
        title = request.args.get('title')
        print(url_link, ' ', t, ' ', interest)
        if not Article.query.filter_by(id=url_link).count():
            article = Article(id=url_link, t=t, user=current_user, interest=interest, title=title)
            db.session.add(article)
            db.session.commit()
        else:
            Article.query.filter_by(id=url_link).first().t += t
            db.session.commit()

    dict_news = {}
    interests = []
    for interest in [userInterest.interest for userInterest in Interest.query.with_parent(current_user).order_by(Interest.id.desc())]:
        interests.append(interest)
        dict_news[interest] = getNews(interest)
    return render_template('dashnewTemplate.html', name=current_user.username, dict_news=dict_news, interests=interests, session=session)
@app.route('/bookmarks', methods=['GET', 'POST'])
@login_required
def bookmarks():
    return render_template('bookmarks.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session['logged_in'] = False
    return redirect(url_for('index'))
