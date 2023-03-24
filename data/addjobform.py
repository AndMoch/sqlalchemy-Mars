from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField,SubmitField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    team_leader = IntegerField(validators=[DataRequired()])
    job = StringField(validators=[DataRequired()])
    work_size = IntegerField(validators=[DataRequired()])
    collaborators = StringField(validators=[DataRequired()])
    is_finished = BooleanField()
    submit = SubmitField()
