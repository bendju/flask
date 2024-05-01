from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class EmailForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)], render_kw={"placeholder": "Enter your first name"})
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)], render_kw={"placeholder": "Enter your last name"})
    address = StringField('Your address', validators=[DataRequired(), Length(min=1, max=30)], render_kw={"placeholder": "Enter your address"})
    email = StringField('E-Mail', validators=[DataRequired(), Length(min=1, max=30), Email()], render_kw={"placeholder": "E-Mail"})
    submit = SubmitField('mentes')
