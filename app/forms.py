from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    tittle = StringField("tittle", validators=[DataRequired()]),
    author = StringField("author", validators=[DataRequired()]),
    status = SelectField('status', choices=[('available', 'available'), ('not_available', 'not_available')], validators=[DataRequired()])

class ShoppingForm(FlaskForm):
    product = StringField("product", validators=[DataRequired()]),
    quantity = IntegerField("quantity", validators=[DataRequired()])
