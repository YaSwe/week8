from flask import Blueprint, render_template, request
from database import get_database_connection

capstone_bp = Blueprint('capstone', __name__)

@capstone_bp.route('/createCapstone', methods=['GET', 'POST'])
def feature1():
    if request.method == "POST":
        cp_name = request.form['cp-name']
        cp_title = request.form['cp-title']
        cp_noOfStudents = request.form['cp-noOfStudents']
        cp_academicYear = request.form['cp-academicYear']
        cp_companyName = request.form['cp-companyName']
        cp_pointOfContract = request.form['cp-pointOfContact']
        cp_desc = request.form['cp-description']

        # Get radio input value
        cp_roleOfContact = request.form.get('cp-roleOfContact')
        print(cp_roleOfContact)

        # Connect to database
        connection = get_database_connection()
        cursor = connection.cursor()

        #SQL Query base
        query = """INSERT INTO capstone_projects (person_in_charge, role_of_contact, num_students, academic_year, capstone_title, company_name, company_contact, project_description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        
        cursor.execute(query, (cp_name, cp_roleOfContact, cp_noOfStudents, cp_academicYear, cp_title, cp_companyName, cp_pointOfContract, cp_desc))
        connection.commit()

        return render_template('createCapstone.html', message="Successful Capstone Creation")
    else:
        return render_template('createCapstone.html')

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
    