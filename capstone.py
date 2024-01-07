from flask import Blueprint, render_template, request
from database import get_database_connection

capstone_bp = Blueprint('capstone', __name__)

@capstone_bp.route('/createCapstone', methods=['GET', 'POST'])
def feature1():
    pass

@capstone_bp.route('/queryCapstone', methods=['GET', 'POST'])
def queryCapstone():
    if request.method == "POST":
        # Get academic year and keyword inputs
        academic_year = request.form['academic-year']
        keyword = request.form['keyword']

        # Validation: Check if academic_year is a valid year (4-digit number)
        if academic_year and (not academic_year.isdigit() or len(academic_year) != 4):
            return render_template('queryCapstone.html', error='Invalid Year Format')

        # Connect to database
        connection = get_database_connection()
        cursor = connection.cursor()

        #SQL Query base
        query = "SELECT * FROM capstone_projects WHERE 1=1"

        # Check if academic year and/or keyword are provided
        if academic_year:
            query += f" AND academic_year = '{academic_year}'"
        if keyword:
            query += f" AND capstone_title LIKE '%{keyword}%' OR project_description LIKE '%{keyword}%'"

        # Add sorting by descending year
        query += " ORDER BY academic_year DESC"

        # Execute the SQL Query
        cursor.execute(query)
        capstone_projects = cursor.fetchall()

        return render_template('queryResults.html', capstone_projects=capstone_projects)
    else:
        return render_template('queryCapstone.html')
    