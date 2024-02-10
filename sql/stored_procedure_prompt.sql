-- CALL the procedure to count total applicants
CALL CountTotalApplicants();

-- CALL the procedure to count full-time applicants
CALL CountFullTimeApplicants();

-- CALL the procedure to count part-time applicants
CALL CountPartTimeApplicants();

-- CALL the procedure to compute the average desired salary
CALL AverageDesiredSalary();

-- CALL the procedure to count the total number of each job position
CALL CountJobPos();

-- CALL the procedure to count the total number of each skill
CALL CountCommonSkill();

-- CALL the procedure to display the applicants
CALL DisplayApplicants();

-- CALL the procedure to display the applicants by name
CALL DisplayApplicantsByName(filter_name);

-- CALL the procedure to display the applicants by applicant ID
CALL GetApplicantDetails(2);

-- CALL the procedure to display the applicants details by applicant no
CALL UpdateApplicantDetails(
    2,  -- d_id
    'John Doe',  -- d_name
    '1990-05-15',  -- d_dateOfBirth
    '123456789',  -- d_SSS_ID
    '123 Main St',  -- d_address
    'Anytown',  -- d_city
    'Some Province',  -- d_province
    12345,  -- d_zipcode
    '555-123-4567',  -- d_phoneNumber
    'john@example.com'  -- d_emailAddress
);

-- CALL the procedure to delete the applicant by applicant no
CALL DeleteApplicantInfo(6);