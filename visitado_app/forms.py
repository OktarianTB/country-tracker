from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired


class AddCountry(FlaskForm):
    new_country = SelectField(coerce=str, validators=[InputRequired()])
    submit = SubmitField("Add")
