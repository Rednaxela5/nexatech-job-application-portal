import mysql.connector
from storage import applicant_data as ad, school_data_1 as sd1, school_data_2 as sd2, school_data_3 as sd3, work_data_1 as wd1, work_data_2 as wd2, work_data_3 as wd3
from storage import skill_data_1 as sn1, skill_data_2 as sn2, skill_data_3 as sn3, skill_data_4 as sn4, skill_data_5 as sn5, skill_data_6 as sn6

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'P@ssw0rd2023!'
MYSQL_DATABASE = 'nexatech'

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
    

    
# def get_next_school_id(school_name, school_address):

#     conn = connect_to_mysql()
#     try:
#         cursor = conn.cursor()
#         query = "SELECT school_ID FROM school WHERE schoolName = %s AND schoolAddress = %s"
#         values = (school_name, school_address)
#         cursor.execute(query, values)
#         result = cursor.fetchone()
        
        
    
#         if cursor.rowcount > 0:
#             result = cursor.fetchone()
#             school_id = result[0]
#             return school_id
#         else:
#             cursor = conn.cursor()
#             query = "SELECT MAX(dump_id) FROM school"
#             cursor.execute(query)
#             result = cursor.fetchone()
#             max_dump_id = result[0]
#             if max_dump_id:
#                 next_school_id = max_dump_id + 1
#             else:
#                 next_school_id = 1
#             school_id = "SID" + str(next_school_id).zfill(5)
#             return school_id
#     except mysql.connector.Error as err:
#         print("Error getting next school ID:", err)
#         return None
#     finally:
#         cursor.close()
        
def insert_applicant_details():
    conn = connect_to_mysql()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO applicant_details (name, dateOfBirth, SSS_ID, address, city, province, zipcode, phoneNumber, emailAddress, employmentType, jobPosition, desiredSalary, startingDate, applicationDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (ad.name, ad.birthdate, ad.sss_id, ad.address, ad.city, ad.province, ad.zipcode, ad.phoneNumber, ad.emailaddress, ad.employment_type, ad.job_pos, ad.desired_salary, ad.desired_start_date, ad.application_date)
            cursor.execute(query, values)
            conn.commit()
            print("Applicant details inserted successfully.")
            # Get the applicantNo after insertion
            ad.applicantNo = cursor.lastrowid
        except mysql.connector.Error as err:
            print("Error inserting applicant details:", err)
        finally:
            cursor.close()
            conn.close()
    return None


def get_next_school_id(school_name, school_address, cursor):
    try:
        query = "SELECT MAX(school_id) FROM school_db"
        cursor.execute(query)
        result = cursor.fetchone()
        max_school_id = result[0]
        if max_school_id:
            # Split the 'SID' and the integer part
            prefix, max_number = max_school_id.split('SID')
            next_number = int(max_number) + 1
            next_school_id = f"SID{next_number:05d}"  # Format with leading zeros
        else:
            next_school_id = "SID00001"
        
        sdb_query = "INSERT into school_db (school_id, school_name, school_address) VALUES (%s, %s, %s)"
        sdb_values = (next_school_id, school_name, school_address)
        cursor.execute(sdb_query, sdb_values)

        return next_school_id
    except mysql.connector.Error as err:
        print("Error getting next school ID:", err)
        return None

def get_school_id(school_name, school_address, cursor):
    query = "SELECT school_id FROM school_db WHERE school_name = %s"
    values = (school_name,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    
    if result:
        return result[0]
    else:
        return None

def get_or_create_school_id(school_name, school_address, cursor):
    school_id = get_school_id(school_name, school_address, cursor)
    
    if school_id:
        return school_id
    else:
        return get_next_school_id(school_name, school_address, cursor)
    
def insert_school_details_1():
    conn = connect_to_mysql()
    if conn is not None:
        try:
            cursor = conn.cursor()
            school_id = get_or_create_school_id(sd1.school_name, sd1.school_address, cursor)

            query = "INSERT INTO school (applicantNo, school_ID, schoolName, schoolAddress, dateGraduated, educationAttainment) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (ad.applicantNo, school_id, sd1.school_name, sd1.school_address, sd1.date_graduated, sd1.educ_attainment)
            cursor.execute(query, values)
            conn.commit()
            print("School details inserted successfully.")

        except mysql.connector.Error as err:
            print("Error inserting school details:", err)
        finally:
            cursor.close()
            conn.close()

    
def insert_school_details_2():
    conn = connect_to_mysql()
    if conn is not None:
        try:
            cursor = conn.cursor()
            school_id = get_or_create_school_id(sd2.school_name, sd2.school_address, cursor)

            query = "INSERT INTO school (applicantNo, school_ID, schoolName, schoolAddress, dateGraduated, educationAttainment) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (ad.applicantNo, school_id, sd2.school_name, sd2.school_address, sd2.date_graduated, sd2.educ_attainment)
            cursor.execute(query, values)
            conn.commit()
            print("School details inserted successfully.")

        except mysql.connector.Error as err:
            print("Error inserting school details:", err)
        finally:
            cursor.close()
            conn.close()
        
def insert_school_details_3():
    conn = connect_to_mysql()
    if conn is not None:
        try:
            cursor = conn.cursor()
            school_id = get_or_create_school_id(sd3.school_name, sd3.school_address, cursor)

            query = "INSERT INTO school (applicantNo, school_ID, schoolName, schoolAddress, dateGraduated, educationAttainment) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (None, ad.applicantNo, school_id, sd3.school_name, sd3.school_address, sd3.date_graduated, sd3.educ_attainment)
            cursor.execute(query, values)
            conn.commit()
            print("School details inserted successfully.")

        except mysql.connector.Error as err:
            print("Error inserting school details:", err)
        finally:
            cursor.close()
            conn.close()


def insert_work_experience_1():
    conn = connect_to_mysql()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Assuming that work_experience_id is auto-generated as "EH" followed by 5 digits
            query = "SELECT MAX(w_dump_id) FROM work_experience"
            cursor.execute(query)
            result = cursor.fetchone()
            max_dump_id = result[0]

            if max_dump_id:
                next_work_dump_id = max_dump_id + 1
            else:
                next_work_dump_id = 1

            # Using string formatting to add leading zeros to make it 5 digits
            work_experience_id = "EH" + str(next_work_dump_id).zfill(5)

            query = "INSERT INTO work_experience (w_dump_id, applicantNo, employmentHistory_ID, companyName, workStarted, workEnded, workPosition, reasonForLeaving) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (None, ad.applicantNo, work_experience_id, wd1.prev_company, wd1.work_date_started, wd1.work_date_ended, wd1.work_position, wd1.reason_for_leaving)
            cursor.execute(query, values)
            conn.commit()
            print("Work experience details inserted successfully.")
        except mysql.connector.Error as err:
            print("Error inserting work experience details:", err)
        finally:
            cursor.close()
            conn.close()
    
def insert_work_experience_2():
    conn = connect_to_mysql()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Assuming that work_experience_id is auto-generated as "EH" followed by 5 digits
            query = "SELECT MAX(w_dump_id) FROM work_experience"
            cursor.execute(query)
            result = cursor.fetchone()
            max_dump_id = result[0]

            if max_dump_id:
                next_work_dump_id = max_dump_id + 1
            else:
                next_work_dump_id = 1

            # Using string formatting to add leading zeros to make it 5 digits
            work_experience_id = "EH" + str(next_work_dump_id).zfill(5)

            query = "INSERT INTO work_experience (w_dump_id, applicantNo, employmentHistory_ID, companyName, workStarted, workEnded, workPosition, reasonForLeaving) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (None, ad.applicantNo, work_experience_id, wd2.prev_company, wd2.work_date_started, wd2.work_date_ended, wd2.work_position, wd2.reason_for_leaving)
            cursor.execute(query, values)
            conn.commit()
            print("Work experience details inserted successfully.")
        except mysql.connector.Error as err:
            print("Error inserting work experience details:", err)
        finally:
            cursor.close()
            conn.close()
    
def insert_work_experience_3():
    conn = connect_to_mysql()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Assuming that work_experience_id is auto-generated as "EH" followed by 5 digits
            query = "SELECT MAX(w_dump_id) FROM work_experience"
            cursor.execute(query)
            result = cursor.fetchone()
            max_dump_id = result[0]

            if max_dump_id:
                next_work_dump_id = max_dump_id + 1
            else:
                next_work_dump_id = 1

            # Using string formatting to add leading zeros to make it 5 digits
            work_experience_id = "EH" + str(next_work_dump_id).zfill(5)

            query = "INSERT INTO work_experience (w_dump_id, applicantNo, employmentHistory_ID, companyName, workStarted, workEnded, workPosition, reasonForLeaving) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (None, ad.applicantNo, work_experience_id, wd3.prev_company, wd3.work_date_started, wd3.work_date_ended, wd3.work_position, wd3.reason_for_leaving)
            cursor.execute(query, values)
            conn.commit()
            print("Work experience details inserted successfully.")
        except mysql.connector.Error as err:
            print("Error inserting work experience details:", err)
        finally:
            cursor.close()
            conn.close()
    

def insert_major_skill(skill_name):
    skill_name_var = skill_name
    conn = connect_to_mysql()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # # Check if the skillName already exists in the major_skill table
            # query = "SELECT skillCode FROM major_skill WHERE skillName = %s"
            # values = (skill_name_var,)
            # cursor.execute(query, values)
            # result = cursor.fetchone()

            # if result:
            #     # Skill already exists, just return the skillCode
            #     skill_code = result[0]
            # else:

            # Assuming that s_dump_code is auto-generated as "SC" followed by 5 digits
            query = "SELECT MAX(s_dump_code) FROM major_skill"
            cursor.execute(query)
            result = cursor.fetchone()
            max_dump_code = result[0]

            if max_dump_code:
                next_s_dump_code = max_dump_code + 1
            else:
                next_s_dump_code = 1

            # Using string formatting to add leading zeros to make it 5 digits
            skill_code = "SC" + str(next_s_dump_code).zfill(5)

            # Insert the new skill into the major_skill table
            query = "INSERT INTO major_skill (s_dump_code, applicantNo, skillCode, skillName) VALUES (%s, %s, %s, %s)"
            values = (None, ad.applicantNo, skill_code, skill_name_var)
            cursor.execute(query, values)
            conn.commit()
            print("Skill details inserted successfully.")

            return skill_code

        except mysql.connector.Error as err:
            print("Error inserting skill details:", err)
        finally:
            cursor.close()
            conn.close()

def connection_database():

    insert_applicant_details()
    
    if sd1.cur_educ_list == 1:
        insert_school_details_1()
    elif sd1.cur_educ_list == 2:
        insert_school_details_1()
        insert_school_details_2()
    elif sd1.cur_educ_list == 3:
        insert_school_details_1()
        insert_school_details_2()
        insert_school_details_3()
   
    if wd1.cur_work_exp == 1:
        insert_work_experience_1()
    elif wd1.cur_work_exp == 2:
        insert_work_experience_1()
        insert_work_experience_2()
    elif wd1.cur_work_exp == 3:
        insert_work_experience_1()
        insert_work_experience_2()
        insert_work_experience_3()

    # Insert major skills (you can call this function multiple times for different skills)
    if sn1.cur_major_skills == 3:
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
    elif sn1.cur_major_skills == 4:
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn4.skill_name)
    elif sn1.cur_major_skills == 5:
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn4.skill_name)
        insert_major_skill(sn5.skill_name)
    elif sn1.cur_major_skills == 6:
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn4.skill_name)
        insert_major_skill(sn5.skill_name)
        insert_major_skill(sn6.skill_name)

    d_skill_1_entry = "Enter Skill Name 1"
    d_skill_2_entry = "Enter Skill Name 2"
    d_skill_3_entry = "Enter Skill Name 3"
    d_skill_4_entry = "Enter Skill Name 4"
    d_skill_5_entry = "Enter Skill Name 5"
    d_skill_6_entry = "Enter Skill Name 6"


    if (sn4.skill_name == "" and sn5.skill_name == "" and sn6.skill_name == "") or (sn4.skill_name == d_skill_4_entry and sn5.skill_name == d_skill_5_entry and sn6.skill_name == d_skill_6_entry):
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
    elif (sn5.skill_name == "" and sn6.skill_name == "") or (sn5.skill_name == d_skill_5_entry and sn6.skill_name == d_skill_6_entry):
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn4.skill_name)
    elif (sn6.skill_name == "") or (sn4.skill_name == d_skill_4_entry and sn6.skill_name == d_skill_6_entry):
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn5.skill_name)
    elif (sn4.skill_name == "" and sn5.skill_name == "") or (sn4.skill_name == d_skill_4_entry and sn5.skill_name == d_skill_5_entry):
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn6.skill_name)
    elif sn4.skill_name == "" or sn4.skill_name == d_skill_4_entry:
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn5.skill_name)
        insert_major_skill(sn6.skill_name)
    elif sn5.skill_name == "" or sn5.skill_name == d_skill_5_entry:
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn4.skill_name)
        insert_major_skill(sn6.skill_name)
    elif sn6.skill_name == "" or sn6.skill_name == d_skill_6_entry:
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn4.skill_name)
        insert_major_skill(sn5.skill_name)
    else:
        insert_major_skill(sn1.skill_name)
        insert_major_skill(sn2.skill_name)
        insert_major_skill(sn3.skill_name)
        insert_major_skill(sn4.skill_name)
        insert_major_skill(sn5.skill_name)
        insert_major_skill(sn6.skill_name)


if __name__ == "__main__":
    connection_database()
