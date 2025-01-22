# Rental Car Platform
This is a rental car platform that allows users to rent cars. The platform is built using Django and Django Framework. The platform has the following features:
- User can login to the platform.
- User can manage the Customers.
- User can manage the Employees.
- User can manage the Vehicle Inventory.
- User can manage the Rental Orders.
- User can manage the Rental Inspections.

## Installation
1. Clone the repository
2. Create a virtual environment
   1. `python3 -m venv venv`
   2. `source venv/bin/activate`
3. Install the requirements
   1. `pip install -r requirements.txt`
4. Run the migrations
   1. `python manage.py migrate`
5. Create a superuser
   1. `python manage.py createsuperuser`
6. Run the server
   1. `python manage.py runserver`
7. Open the browser and go to `http://localhost:8000/admin/`
