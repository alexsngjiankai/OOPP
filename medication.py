from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required


class medForm(FlaskForm):
    medName = StringField(u'Enter name of prescription', validators=[data_required])
    medAmt = StringField(u'Enter the amount of tablet(e.g. 400ml/2tablets)', validators=[data_required])
    medDesc = StringField(u'Enter medicine description(e.g. After meals, 2times a day, may cause cause drowsiness)', validators=[data_required])
    submit = SubmitField(u'Submit')
