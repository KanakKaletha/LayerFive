# LayerFive Assignment
### Hotel Booking System
This is a Django Layer Five Assignment for web application for managing hotel bookings.

###Features
View the number of available rooms by category for a specific date
View the number of available rooms by category for a date range
View guest details for a specific room
###Setup
Install the required dependencies by running pip install -r requirements.txt.
Run the Django migrations to set up the database by running python manage.py migrate.
Create an API key for accessing the views by creating an instance of the APIKey model in the Django admin interface.
Include the API key in the request headers when making requests to the views.
###Usage
The application provides several views for managing hotel bookings:

index: The main view of the application.
room_count_by_category: View the number of available rooms by category for a specific date.
room_count_by_category_range: View the number of available rooms by category for a date range.
guest_details: View guest details for a specific room.
All views require an API key to be included in the request headers in order to access them.

###Code Structure
The code is organized into several Django apps:

booking: Contains the models and views for managing hotel bookings.
customauth: Contains the models and views for managing API keys.
The backend.py file contains a function for authenticating requests using API keys.

###Security
The application uses API keys to authenticate requests to the views. Only requests that include a valid API key in the request headers are allowed to access the views.

###Password
All the required password are store in enviro.env
