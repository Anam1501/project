from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, TelField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError, InputRequired, NumberRange
from datetime import datetime, timedelta

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ChangePasswordForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    old_password = PasswordField('Old Password', validators=[InputRequired()])
    new_password = PasswordField('New Password', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('new_password')])
    submitChange = SubmitField('SUBMIT')

class RegistrationForm(FlaskForm):
    user_name = StringField('Username', validators=[
        InputRequired(),
        Regexp(r'[A-Za-z]+$'),
        Length(min=10, max=20)
    ])
    email = StringField('Email', validators=[
        InputRequired(), 
        Email(message='Incorrect email address')
    ])
    mobile_number = TelField('Mobile Number', validators=[
        InputRequired(),
        Length(min=10, max=10, message='Incorrect mobile number')
    ])
    date_of_birth = DateField('Date of Birth (MM-DD-YYYY)', validators=[
        InputRequired(), 
        ])

    password = PasswordField('Password', validators=[
        InputRequired(),
        Length(min=8),
    ])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password', message="Passwords must match.")])
    security_question = SelectField('Security Question', choices=['What is your favorite book?', 'What was the name of your favorite pet?', 'What is your favorite food?'], validators=[InputRequired()])
    security_answer = StringField('Security Answer', validators=[
        InputRequired(),
    ])
    submitRegisteration = SubmitField('SIGNUP')
    


class BookingForm(FlaskForm):
    # Movie name (non-editable)
    movie_name = StringField('Movie Name', validators=[DataRequired()])
    
    # Theater name (non-editable)
    theater_name = StringField('Theater Name', validators=[DataRequired()])
    
    # Language (non-editable)
    language = StringField('Language', validators=[DataRequired()])
    
    # Category (non-editable)
    category = StringField('Category', validators=[DataRequired()])
    
    # Seat capacity (non-editable)
    seat_capacity = IntegerField('Seat Capacity', validators=[DataRequired()])
    
    # Price (non-editable)
    price_per_ticket = IntegerField('Price per Ticket', validators=[DataRequired()])
    
    # Booking Date (editable)
    date_of_booking = DateField('Date of Booking', validators=[DataRequired()])
    
    # Time of Booking (editable)
    time_of_booking = SelectField('Select Time', choices=[
        ('10AM to 1PM', '10AM to 1PM'),
        ('2PM to 5PM', '2PM to 5PM'),
        ('6PM to 9PM', '6PM to 9PM')
    ], validators=[DataRequired()])
    
    # No. of tickets (editable)
    no_of_tickets_required = IntegerField('No. of Tickets', validators=[
        DataRequired(),
        NumberRange(min=1, max=100)
    ])
    
    # Submit button
    submitBook = SubmitField('Book Now')
    
    def validate_date(self):
        # Booking date must be greater than the current date and within a span of 3 days
        current_date = datetime.now().date()
        if self.date_of_booking.data <= current_date:
            return 0
        
        if self.date_of_booking.data > current_date + timedelta(days=3):
            return 1
    
    def validate_ticket_availability(self, seat_capacity, booked_tickets):
        # Seat capacity check
        available_seats = seat_capacity - booked_tickets
        if self.no_of_tickets_required.data > available_seats:
            return 1