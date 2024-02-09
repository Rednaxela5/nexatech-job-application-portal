import mysql.connector
import os

# Login Page
USERNAME = "admin"
PASSWORD = "password"

# Modify this depending on your MySQL configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'P@ssw0rd2023!'
MYSQL_DATABASE = 'nexatech'


# Connet to MySQL
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None

def tot_applicant():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("CALL CountTotalApplicants();")
    result = cursor.fetchall()
    cursor.close()
    return result


def full_time():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("CALL CountFullTimeApplicants();")
    result = cursor.fetchall()
    cursor.close()
    return result


def part_time():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("CALL CountPartTimeApplicants();")
    result = cursor.fetchall()
    cursor.close()
    return result

def avg_des_sal():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("CALL AverageDesiredSalary();")
    result = cursor.fetchall()
    cursor.close()
    # Extracting the average salary from the result set
    average_salary = result[0][0] if result else 0.0
    return average_salary

def count_common_job_pos():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("CALL CountJobPos();")
    result = cursor.fetchall()
    cursor.close()
    return result

def count_common_skills():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("CALL CountCommonSkill();")
    result = cursor.fetchall()
    cursor.close()
    return result

def display_applicant_details():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("CALL DisplayApplicantsByName('filter_name');")
    result = cursor.fetchall()
    cursor.close()
    return result

def search_applicant_details(search_key):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("CALL DisplayApplicantsByName(filter_name);")
    result = cursor.fetchall()
    cursor.close()
    return result