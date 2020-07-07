from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    search_param = StringField('Search Topic', validator = [Required()])
    submit = SubmitField('Submit')