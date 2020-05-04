from .import auth
from flask import render_template,redirect,url_for,flash,request
from .forms import RegistrationForm

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
         author = form.author.data,
         password = form.password.data)

        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to Pitch It Up!","email/welcome_user",user.email,user=user)

        title = "New Account"

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html',registration_form = form)
