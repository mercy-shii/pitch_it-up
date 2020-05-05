from flask import Flask,render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
from .forms import PitchForm
from .. import db
from ..models import Pitches,User,Comments

@main.route('/')
def index():
    '''
    my index page
    '''
    title = 'Pitch It UP'
    return render_template('index.html',title = title)

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch= form.pitch.data
        

        # Updated pitchinstance
        new_pitch = Pitches(category= category,pitch= pitch,user=current_user)

        db.session.add(new_pitch)
        db.session.commit()

        title='New Pitch'


        return redirect(url_for('main.index'))

    return render_template('pitch.html',pitch_entry= form)

@main.route('/categories/<cate>')
def category(cate):
    '''
    function to return the pitches by category
    '''
    pitches = Pitches.query.filter_by(category=cate).all()
    print(category)
    title = f'{cate}'
    return render_template('categories.html',title = title, pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        

        return redirect(url_for('.profile',uname=user.author))

    return render_template('profile/update.html',form =form)


@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    comm =Comments.get_comment(id)
    print(comm)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title)

@main.route('/new_comment/<int:pitches_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitches_id):
    pitches = Pitches.query.filter_by(id = pitches_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment=comment,user_id=current_user.id, pitches_id=pitches_id)


        new_comment.save_comment()


        return redirect(url_for('main.index'))
    title='New Pitch'
    return render_template('new_comment.html',title=title,comment_form = form,pitches_id=pitches_id)
  
     