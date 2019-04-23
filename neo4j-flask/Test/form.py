from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange, AnyOf


class information(FlaskForm):
    answers = ["yes", "Yes", "YEs", "YES", "yEs", "yES", "yeS", "no", "No", "NO", "nO"]
    
    studentName = StringField('Name (Optional)')
    toeflScore = FloatField('TOEFL Score (Out of 120)', validators=[InputRequired(), NumberRange(min=0, max=120)])
    sopScore = FloatField('Statement of Purpose (Out of 5)', validators=[InputRequired(), NumberRange(min=0, max=5)])
    lorScore = FloatField('Letter(s) of Recommendation (Out of 5)', validators=[InputRequired(), NumberRange(min=0, max=5)])
    cgpaScore = FloatField('CGPA Score (Out of 10)', validators=[InputRequired(), NumberRange(min=0, max=10)])
    greScore = FloatField('GRE Score (Out of 340)', validators=[InputRequired(), NumberRange(min=0, max=340)])
    research = StringField('Research Experience (Yes/ No)', validators=[InputRequired(), AnyOf(answers, message="Yes or No only, please check your spelling")])
    uniRating = IntegerField('University Rating (From 1 to 5)', validators=[InputRequired(), NumberRange(min=1, max=5)])    
    calculate = SubmitField('Calculate')
