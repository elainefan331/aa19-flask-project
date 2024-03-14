from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, URL, NumberRange

class ItemForm(FlaskForm):
    id = IntegerField("id", validators=[DataRequired(), NumberRange(min=0)])
    happiness = IntegerField("happiness", validators=[DataRequired(), Length(min=0, max=100)])
    imageUrl = StringField("imageUrl", validators=[DataRequired(), URL()])
    name = StringField("name", validators=[DataRequired()])
    prince = FloatField("price")
    pokemonId = IntegerField("pokemonId")
