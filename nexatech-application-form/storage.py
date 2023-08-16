class applicant_details():
    def __init__(self):
        self.applicantNo = ""
        self.name = ""
        self.birthdate = ""
        self.sss_id = ""
        self.address = ""
        self.city = ""
        self.province = ""
        self.zipcode = ""
        self.phoneNumber = ""
        self.emailaddress = ""
        self.employment_type = ""
        self.job_pos = ""
        self.desired_salary = ""
        self.desired_start_date = ""
        self.application_date = ""

applicant_data = applicant_details()

class school_details():
    def __init__(self):
        self.school_name = ""
        self.school_address = ""
        self.date_graduated = ""
        self.educ_attainment = ""
        self.cur_educ_list = 1

school_data_1 = school_details()
school_data_2 = school_details()
school_data_3 = school_details()

class work_experience():
    def __init__(self):
        self.cur_work_exp = 1
        self.prev_company = ""
        self.work_position = ""
        self.work_date_started = ""
        self.work_date_ended = ""
        self.reason_for_leaving = ""

work_data_1 = work_experience()
work_data_2 = work_experience()
work_data_3 = work_experience()


class major_skills():
    def __init__(self):
        self.cur_major_skills = 1
        self.skill_name = ""

skill_data_1 = major_skills()
skill_data_2 = major_skills()
skill_data_3 = major_skills()
skill_data_4 = major_skills()
skill_data_5 = major_skills()
skill_data_6 = major_skills()
