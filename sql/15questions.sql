-- ============================================================================================================
-- =============================================== EASY =======================================================
-- ============================================================================================================
-- 1 Display applicantNo, name, SSS_ID, emailAddress, and desired salary of applicants. Sort with desiredSalary in ascending order.
SELECT applicantNo, name, SSS_ID, emailAddress, desiredSalary
FROM applicant_details
ORDER BY desiredSalary ASC;

-- 2 Select and list applicantNo,name of applicant who chose Full-time as their employment type
SELECT applicantNo, name
FROM applicant_details
WHERE employmentType = 'Full-time';

-- 3 Select and list applicantNo,name of applicant who chose Part-time as their employment type
SELECT applicantNo, name
FROM applicant_details
WHERE employmentType = 'Part-time';

-- 4 List all applicants who have a job position with “IT Support Specialist”. Display their applicantNo, name, employmentType and desiredSalary
SELECT applicantNo, name, employmentType, desiredSalary
FROM applicant_details
WHERE jobPosition = 'IT Support Specialist';

-- 5 Get the total count of applicants who are living in Manila.
SELECT COUNT(*) AS 'Living in Manila'
FROM applicant_details
WHERE province LIKE '%Manila';

-- ============================================================================================================
-- ============================================== MEDIUM ======================================================
-- ============================================================================================================

-- 1 Count the number of applicants in each school entry and display their school_ID and schoolName.
SELECT school_ID AS 'School ID', schoolName AS 'School Name', COUNT(applicantNo) AS 'Number'
FROM school
GROUP BY school_ID, schoolName;

-- 2 Display the number of applicant who have work experience in each Company. Display also the company name.
SELECT companyName, COUNT(*) AS 'Number'
FROM work_experience
GROUP BY companyName;

-- 3 Display the total count of each skill and group them by skillCode and skillName. You should display the skillCode and skillName first.
SELECT skillCode, skillName, COUNT(*)
FROM major_skill
GROUP BY skillCode, skillName;

-- 4 Count the number of applicants graduated from each school or university. Display also the educational attaintment. 
SELECT school_ID, schoolName, educationAttainment, COUNT(*)
FROM school
GROUP BY school_ID, schoolName, educationAttainment;

-- 5 Count the applicants that selected full-time and part-time and group them by employment type.
SELECT employmentType, COUNT(*) AS 'Applicants'
FROM applicant_details
GROUP BY employmentType;

-- ============================================================================================================
-- =============================================== HARD =======================================================
-- ============================================================================================================
-- 1 Display the applicantNo, name of applicants, and years worked of those who graduated from Polytechnic University of the Philippines  and have 3 or more years of work experience.
SELECT A.applicantNo, A.name, S.schoolName, TIMESTAMPDIFF(YEAR, E.workStarted, E.workEnded) AS 'Years Worked'
FROM applicant_details AS A
JOIN school AS S ON A.applicantNo = S.applicantNo
JOIN work_experience AS E ON S.applicantNo = E.applicantNo
WHERE S.schoolName = 'Polytechnic University of the Philippines' 
  AND TIMESTAMPDIFF(YEAR, E.workStarted, E.workEnded) >= 3;

-- 2 List the applicants with have 30 years or older and have a skill or “Networking” and “Troubleshooting” and is graduated for PUP or UP. Display the applicantNo, name, and age.
SELECT A.applicantNo, A.name, TIMESTAMPDIFF(YEAR, A.dateOfBirth, CURDATE()) AS Age
FROM applicant_details AS A
JOIN major_skill AS M ON A.applicantNo = M.applicantNo
JOIN school AS S ON A.applicantNo = S.applicantNo
WHERE TIMESTAMPDIFF(YEAR, A.dateOfBirth, CURDATE()) >= 30
  AND M.skillName IN ('Networking', 'Troubleshooting')
  AND S.schoolName IN ('Polytechnic University of the Philippines', 'University of the Philippines Diliman')
GROUP BY A.applicantNo, A.name;

-- 3 List down applicants who is 40 years or older then count each school and work experience. Display applicantName, age, distinct school count and work count.
SELECT A.applicantNo, 
       TIMESTAMPDIFF(YEAR, A.dateOfBirth, CURDATE()) AS Age, 
       COUNT(DISTINCT S.school_ID) AS SchoolCount, 
       COUNT(DISTINCT E.employmentHistory_ID) AS EmploymentHistoryCount
FROM applicant_details AS A
JOIN school AS S ON A.applicantNo = S.applicantNo
JOIN work_experience AS E ON S.applicantNo = E.applicantNo
WHERE TIMESTAMPDIFF(YEAR, A.dateOfBirth, CURDATE()) >= 40
GROUP BY A.applicantNo;

-- 4 Display the applicantNo, name, jobPosition of applicant that has 3 or more years of work experience and specialized in Networking and Troubleshooting
SELECT A.applicantNo, A.name, A.jobPosition
FROM applicant_details AS A
JOIN work_experience AS E ON A.applicantNo = E.applicantNo
JOIN major_skill AS M ON E.applicantNo = M.applicantNo
WHERE TIMESTAMPDIFF(YEAR, E.workStarted, E.workEnded) >= 3 AND skillName IN ('Networking', 'Troubleshooting')
GROUP BY applicantNo;

-- 5 Count the applicants that has Maintenance skill and is graduated from Polytechnic University of the Philippines and University of the Philippines Diliman. Group them by their school name.
SELECT S.schoolName,COUNT(*) AS 'Applicant'
FROM school AS S
JOIN major_skill AS M ON S.applicantNo = M.applicantNo
WHERE skillName = 'Maintenance' AND schoolName IN ('Polytechnic University of the Philippines', 'University of the Philippines Diliman')
GROUP BY S.schoolName;




-- DUMP
-- 1 Display the average desired salary of college graduate applicants.
SELECT AVG(desiredSalary)
FROM applicant_details AS A, school AS S
WHERE A.applicantNo = S.applicantNo AND S.educationAttainment = 'CO';

-- 2 Retrieve the applicantNo, and company of applicants who have worked in a company for more than 3 years.
SELECT applicantNo, companyName, COUNT(*)
FROM work_experience
WHERE TIMESTAMPDIFF(year, workStarted, workEnded) >= 3
GROUP BY applicantNo, companyName;
