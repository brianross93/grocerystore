from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, DateField, SelectField, SubmitField, PasswordField, FloatField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem, User




class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # Adding the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button

    title = StringField("Title", validators=[DataRequired(), Length(min=3, max=80)])
    address = TextAreaField("Address", validators=[DataRequired(), Length(min=3, max=80) ])
    submit = SubmitField('Submit')
    

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # Adding the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField("Price", validators=[DataRequired()])
    photo_url = StringField("PhotoUrl", validators=[URL(), Length(min=3)])
    category = SelectField('Category', choices=[('DELI', 'Deli'), ('BAKERY', 'Bakery'), ('PANTRY', 'Pantry'), ('FROZEN', 'Frozen'), ('OTHER', 'Other')])
    store = QuerySelectField(query_factory=lambda:GroceryStore.query, allow_blank=False, get_label='title')
    submit = SubmitField('Submit')

    class SignUpForm(FlaskForm):
        username = StringField('User Name',validators=[DataRequired(), Length(min=3, max=50)])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Sign Up')

        def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')


    class LoginForm(FlaskForm):
        username = StringField('User Name',validators=[DataRequired(), Length(min=3, max=50)])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Log In')

