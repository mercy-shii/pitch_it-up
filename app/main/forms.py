from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch a Title')
    category = SelectField(u'Pitch Category',choices=[('life','life'),('coding','coding'),('love','love'),('Happiness','Happiness')])
    pitch = TextAreaField('pitch')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')    