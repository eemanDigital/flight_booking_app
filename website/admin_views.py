from flask_admin.contrib.sqla import ModelView
from flask_admin.model import typefmt

# Show null values instead of empty strings.
MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({type(None): typefmt.null_formatter})

class UserView(ModelView):
    # Customize the form columns for User model.
    form_columns = (
        'username',
        'email',
        'password',
        'phone_number',
    )
    # Make certain columns editable in the list view.
    column_editable_list = ('username', 'email', 'phone_number')
    # Enable searching on specified columns.
    column_searchable_list = ('username', 'email')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class CompanyView(ModelView):
    # Exclude 'employees' column from the form view.
    form_excluded_columns = ('employees')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class CountryView(ModelView):
    # Exclude 'cities' and 'passports' columns from the form view.
    form_excluded_columns = ('cities', 'passports')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class CityView(ModelView):
    # Customize the form columns for City model.
    form_columns = ('name', 'country')
    # Specify the columns to be displayed in the list view.
    column_list = ('name', 'country')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class PassportView(ModelView):
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class FlightView(ModelView):
    # Specify the columns to be displayed in the list view.
    column_list = ('name', 'departure_city', 'arrival_city', 'departure', 'arrival')
    # Customize the form columns for Flight model.
    form_columns = ('name', 'departure_city', 'arrival_city', 'departure', 'arrival')
    # Customize the column labels for better readability.
    column_labels = dict(departure_city='From', arrival_city='To', departure='Departure Time', arrival='Arrival Time')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class EmploymentView(ModelView):
    # Exclude 'bookings' column from the form view.
    form_excluded_columns = ('bookings')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class BookingView(ModelView):
    # Specify the columns to be displayed in the list view.
    column_list = ('user', 'flight', 'employment', 'date_issued', 'cancellation_fee', 'cancellation_deadline')
    # Customize the form columns for Booking model.
    form_columns = ('user', 'flight', 'employment', 'date_issued', 'cancellation_fee', 'cancellation_deadline')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS
from flask_admin.contrib.sqla import ModelView
from flask_admin.model import typefmt

# Show null values instead of empty strings.
MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({type(None): typefmt.null_formatter})

class UserView(ModelView):
    # Customize the form columns for User model.
    form_columns = (
        'username',
        'email',
        'password',
        'phone_number',
    )
    # Make certain columns editable in the list view.
    column_editable_list = ('username', 'email', 'phone_number')
    # Enable searching on specified columns.
    column_searchable_list = ('username', 'email')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class CompanyView(ModelView):
    # Exclude 'employees' column from the form view.
    form_excluded_columns = ('employees')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class CountryView(ModelView):
    # Exclude 'cities' and 'passports' columns from the form view.
    form_excluded_columns = ('cities', 'passports')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class CityView(ModelView):
    # Customize the form columns for City model.
    form_columns = ('name', 'country')
    # Specify the columns to be displayed in the list view.
    column_list = ('name', 'country')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class PassportView(ModelView):
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class FlightView(ModelView):
    # Specify the columns to be displayed in the list view.
    column_list = ('name', 'departure_city', 'arrival_city', 'departure', 'arrival')
    # Customize the form columns for Flight model.
    form_columns = ('name', 'departure_city', 'arrival_city', 'departure', 'arrival')
    # Customize the column labels for better readability.
    column_labels = dict(departure_city='From', arrival_city='To', departure='Departure Time', arrival='Arrival Time')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class EmploymentView(ModelView):
    # Exclude 'bookings' column from the form view.
    form_excluded_columns = ('bookings')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS

class BookingView(ModelView):
    # Specify the columns to be displayed in the list view.
    column_list = ('user', 'flight', 'employment', 'date_issued', 'cancellation_fee', 'cancellation_deadline')
    # Customize the form columns for Booking model.
    form_columns = ('user', 'flight', 'employment', 'date_issued', 'cancellation_fee', 'cancellation_deadline')
    # Use custom formatters for column types.
    column_type_formatters = MY_DEFAULT_FORMATTERS
