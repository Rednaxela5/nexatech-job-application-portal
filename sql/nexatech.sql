-- -- ------------------------------------------------------------------------------
-- ---------------------------- CREATE DATABASE ------------------------------------
-- ---------------------------------------------------------------------------------
CREATE SCHEMA IF NOT EXISTS nexatech;

-- Switch to the nexatech schema
USE nexatech;

-- -- ------------------------------------------------------------------------------
-- --------------------------- APPLICANT DETAILS -----------------------------------
-- ---------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS applicant_details (
    applicantNo INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    dateOfBirth DATE NOT NULL,
    SSS_ID VARCHAR(15) NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(30) NOT NULL,
    province VARCHAR(30) NOT NULL,
    zipcode INT NOT NULL,
    phoneNumber VARCHAR(12) NOT NULL,
    emailAddress VARCHAR(40) NOT NULL,
    employmentType CHAR(9) NOT NULL,
    jobPosition VARCHAR(30) NOT NULL,
    desiredSalary INT NOT NULL,
    startingDate DATE NOT NULL,
    applicationDate DATE NOT NULL
);

-- INSERT DATA INTO THE TABLE
INSERT INTO applicant_details (
    name, dateOfBirth, SSS_ID, address, city, province, zipcode, phoneNumber, emailAddress,
    employmentType, jobPosition, desiredSalary, startingDate, applicationDate
)
VALUES 
    ('John Doe', '1990-01-01', '1234567890', '123 Main Street', 'Makati', 'Metro Manila', 1234, '9123456789', 'johndoe@email.com', 'Full-time', 'IT Support Specialist', 60000, '2023-06-01', '2023-05-10'),
	('Jane Smith', '1995-05-15', '9876543210', '456 Oak Street', 'Quezon City', 'Metro Manila', 5678, '9001122334', 'janesmith@email.com', 'Part-time', 'IT Project Manager', 40000, '2023-06-15', '2023-05-04'),
	('Juan Cruz', '2000-02-03', '8792134560', '789 Wood Street', 'Imus', 'Cavite', 5319, '9123043123', 'juancruz@email.com', 'Full-time', 'Data Analyst', 50000, '2023-05-12', '2023-06-27'),
	('Mark Santos', '1972-07-07', '5693142708', '890 Birch Street', 'Caloocan', 'Metro Manila', 1478, '9313402212', 'marksantos@email.com', 'Part-time', 'IT Consultant', 45000, '2023-06-25', '2023-06-10'),
	('Mary Garcia', '1980-10-21', '6710958243', '765 Stone Street', 'Pasay', 'Metro Manila', 8426, '9412323031', 'marygarcia@email.com', 'Full-time', 'IT Support Specialist', 55000, '2023-07-30', '2023-07-15'),
	('Paul Perez', '1999-12-24', '7315894602', '268 Pilar Street', 'Malabon', 'Metro Manila', 8139, '9230131244', 'paulperez@email.com', 'Full-time', 'Web Developer', 35000, '2023-08-01', '2023-07-12'),
	('Peter Gomez', '1989-10-04', '3150742968', '645 Kamote Street', 'Valenzuela', 'Metro Manila', 3579, '9403112302', 'petergomez@email.com', 'Part-time', 'Systems Administrator', 30000, '2023-08-01', '2023-07-22');


-- -- ------------------------------------------------------------------------------
-- ----------------------------- SCHOOL DATABASE -----------------------------------
-- ---------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS school_db (
    school_id VARCHAR(8) PRIMARY KEY NOT NULL,
    school_name VARCHAR(255) NOT NULL,
    school_address VARCHAR(100) NOT NULL
);

-- INSERT DATA INTO THE TABLE
INSERT INTO school_db (school_id, school_name, school_address)
VALUES 
	('SID00001', 'Abe International Business College', 'Quezon City, Metro Manila'),
    ('SID00002', 'Abra State Institute of Science and Technology', 'Lagangilang, Abra'),
    ('SID00003', 'ACLC College of Butuan', 'Butuan City, Agusan del Norte'),
    ('SID00004', 'ACTS Computer College Sta Cruz', 'Sta. Cruz, Laguna'),
    ('SID00005', 'Adamson University', 'Ermita, Manila'),
    ('SID00006', 'Adventist International Institute of Advanced Studies', 'Silang, Cavite'),
    ('SID00007', 'Adventist University of the Philippines', 'Silang, Cavite'),
    ('SID00008', 'Agusan Del Sur College', 'San Francisco, Agusan del Sur'),
    ('SID00009', 'Aklan State University', 'Banga, Aklan'),
    ('SID00010', 'Aldersgate College', 'Solano, Nueva Vizcaya'),
    ('SID00011', 'Alliance Graduate School', 'Quezon City, Metro Manila'),
    ('SID00012', 'AMA Computer College Tuguegarao', 'Tuguegarao City'),
    ('SID00013', 'AMA Computer University', 'Quezon City, Metro Manila'),
    ('SID00014', 'Angeles University Foundation', 'Angeles City, Pampanga'),
    ('SID00015', 'Araullo University', 'Cabanatuan City, Nueva Ecija'),
    ('SID00016', 'Arellano University', 'Sampaloc, Manila'),
    ('SID00017', 'Asia Pacific College', 'Makati City'),
    ('SID00018', 'Asian College of Technology', 'Cebu City, Cebu'),
    ('SID00019', 'Asian Institute of Journalism and Communication', 'Quezon City, Metro Manila'),
    ('SID00020', 'Asian Institute of Management', 'Makati City'),
    ('SID00021', 'Asian Institute of Maritime Studies', 'Pasay City, Metro Manila'),
    ('SID00022', 'Asian Social Institute Manila', 'Manila City, Metro Manila'),
    ('SID00023', 'Asian Theological Seminary Philippines', 'Quezon City, Metro Manila'),
    ('SID00024', 'Ateneo de Davao University', 'Davao City'),
    ('SID00025', 'Ateneo de Manila University', 'Katipunan Ave, Quezon City'),
    ('SID00026', 'Ateneo de Naga University', 'Naga City, Camarines Sur'),
    ('SID00027', 'Ateneo de Zamboanga University', 'Zamboanga City'),
    ('SID00028', 'Aurora State College of Technology', 'Baler, Aurora'),
    ('SID00029', 'Baguio Central University', 'Baguio City, Benguet'),
    ('SID00030', 'Baguio College of Technology', 'Baguio City, Benguet'),
    ('SID00031', 'Basilan State College', 'Isabela City, Basilan'),
    ('SID00032', 'Bataan Peninsula State University', 'Balanga City, Bataan'),
    ('SID00033', 'Batanes State College', 'Basco, Batanes'),
    ('SID00034', 'Batangas State University', 'Batangas City, Batangas'),
    ('SID00035', 'Benedicto College', 'Mandaue City, Cebu'),
    ('SID00036', 'Benguet State University', 'La Trinidad, Benguet'),
    ('SID00037', 'Bestlink College of the Philippines', 'Quezon City, Metro Manila'),
    ('SID00038', 'Bicol Christian College of Medicine AMEC BCCM', 'Legazpi City, Albay'),
    ('SID00039', 'Bicol State College of Applied Sciences and Technology', 'Naga City, Camarines Sur'),
    ('SID00040', 'Bicol University', 'Legazpi City, Albay'),
    ('SID00041', 'Biliran Province State University', 'Naval, Biliran'),
    ('SID00042', 'Binangonan Catholic College', 'Binangonan, Rizal'),
    ('SID00043', 'BIT International College', 'Tacloban City, Leyte'),
    ('SID00044', 'Bohol Island State University (Central Visayas State College of Agriculture)', 'Tagbilaran City, Bohol'),
    ('SID00045', 'Brokenshire College', 'Davao City, Davao del Sur'),
    ('SID00046', 'Bukidnon State University', 'Malaybalay City, Bukidnon'),
    ('SID00047', 'Bulacan Agricultural State College', 'San Ildefonso, Bulacan'),
    ('SID00048', 'Bulacan State University', 'Malolos City, Bulacan'),
    ('SID00049', 'Cagayan State University', 'Tuguegarao City, Cagayan'),
    ('SID00050', 'Calayan Educational Foundation', 'Lucena City, Quezon'),
    ('SID00051', 'Calayan Educational Foundation', 'Lucena City, Quezon'),
    ('SID00052', 'Camarines Norte State College', 'Daet, Camarines Norte'),
    ('SID00053', 'Camarines Sur Polytechnic Colleges', 'Naga City, Camarines Sur'),
	('SID00054', 'CAP College Foundation', 'Dasmariñas, Cavite'),
    ('SID00055', 'Capitol University', 'Cagayan de Oro City, Misamis Oriental'),
    ('SID00056', 'Capiz State University', 'Roxas City, Capiz'),
    ('SID00057', 'Caraga State University', 'Butuan City'),
    ('SID00058', 'Carlos Hilado Memorial State College', 'Talisay City, Negros Occidental'),
    ('SID00059', 'Catanduanes State University', 'Virac, Catanduanes'),
    ('SID00060', 'Cavite State University', 'Indang, Cavite'),
    ('SID00061', 'Cebu Aeronautical Technical School (Computer Arts and Technological College Legazpi City)', 'Legazpi City, Albay'),
    ('SID00062', 'Cebu Doctors’ University', 'Mandaue City, Cebu'),
    ('SID00063', 'Cebu Institute of Medicine', 'Cebu City, Cebu'),
    ('SID00064', 'Cebu Institute of Technology', 'Cebu City'),
    ('SID00065', 'Cebu Normal University', 'Cebu City'),
    ('SID00066', 'Cebu Technological University', 'Cebu City'),
    ('SID00067', 'Center for Industrial Technology and Enterprise', 'San Isidro, Nueva Ecija'),
    ('SID00068', 'Central Bicol State University of Agriculture', 'Pili, Camarines Sur'),
    ('SID00069', 'Central Colleges of the Philippines', 'Quezon City, Metro Manila'),
    ('SID00070', 'Central Luzon State University', 'Science City of Muñoz, Nueva Ecija'),
    ('SID00071', 'Central Mindanao University', 'Musuan, Bukidnon'),
    ('SID00072', 'Central Philippine Adventist College', 'Murcia, Negros Occidental'),
    ('SID00073', 'Central Philippine University', 'Jaro, Iloilo City'),
    ('SID00074', 'Centro Escolar University Manila Mendiola', 'San Miguel, Manila'),
    ('SID00075', 'Chiang Kai Shek College', 'Manila City, Metro Manila'),
    ('SID00076', 'City College of Angeles', 'Angeles City, Pampanga'),
    ('SID00077', 'Colegio de Dagupan', 'Dagupan City, Pangasinan'),
    ('SID00078', 'Colegio de San Juan de Letran', 'Manila City, Metro Manila'),
    ('SID00079', 'Colegio de San Pedro', 'San Pedro City, Laguna'),
    ('SID00080', 'Colegio de Sta Catalina de Alejandria', 'Pamplona, Camarines Sur'),
    ('SID00081', 'Colegio San Agustin Bacolod', 'Bacolod City, Negros Occidental'),
    ('SID00082', 'College of Development Communication', 'Los Baños, Laguna'),
    ('SID00083', 'College of Technological Sciences Cebu', 'Cebu City, Cebu'),
    ('SID00084', 'College of the Holy Spirit', 'Manila City, Metro Manila'),
    ('SID00085', 'Columban College', 'Olongapo City, Zambales'),
    ('SID00086', 'Computer Arts and Technology CAT College Polangui', 'Polangui, Albay'),
    ('SID00087', 'Comteq Computer and Business College', 'Iligan City, Lanao del Norte'),
	('SID00088', 'Cotabato Foundation College of Science and Technology', 'Datu Odin Sinsuat, Maguindanao'),
    ('SID00089', 'Davao del Norte State College', 'Panabo City, Davao del Norte'),
    ('SID00090', 'Davao del Sur State College', 'Digos City, Davao del Sur'),
    ('SID00091', 'Davao Doctors College', 'Davao City, Davao del Sur'),
    ('SID00092', 'Davao Medical School Foundation', 'Davao City, Davao del Sur'),
    ('SID00093', 'De La Salle Araneta University:', 'Malabon City'),
    ('SID00094', 'De La Salle College of Saint Benilde', 'Malate, Manila'),
    ('SID00095', 'De La Salle Health Sciences Institute', 'Dasmariñas City, Cavite'),
    ('SID00096', 'De La Salle Lipa', 'Lipa City, Batangas'),
    ('SID00097', 'De La Salle University Dasmariñas', 'Dasmariñas City, Cavite'),
    ('SID00098', 'De La Salle University Manila', 'Malate, Manila'),
    ('SID00099', 'Dipolog Medical Center College Foundation', 'Dipolog City, Zamboanga del Norte'),
    ('SID00100', 'Divine Word College of Legazpi', 'Legazpi City, Albay'),
    ('SID00101', 'DMMA College of Southern Philippines', 'Davao City, Davao del Sur'),
    ('SID00102', 'Don Bosco College', 'Canlubang, Calamba City, Laguna'),
    ('SID00103', 'Don Honorio Ventura State University DHVSU', 'Bacolor, Pampanga'),
    ('SID00104', 'Don Honorio Ventura Technological State University', 'Bacolor, Pampanga'),
    ('SID00105', 'Don Mariano Marcos Memorial State University', 'San Fernando City, La Union'),
    ('SID00106', 'Dr Aurelio Mendoza Memorial College', 'Ozamiz City, Misamis Occidental'),
    ('SID00107', 'Eastern Samar State University', 'Borongan City, Eastern Samar'),
    ('SID00108', 'Eastern Visayas State University', 'Tacloban City, Leyte'),
    ('SID00109', 'Emilio Aguinaldo College', 'Ermita, Manila'),
    ('SID00110', 'Eulogio Amang Rodríguez Institute of Science and Technology', 'Manila City, Metro Manila'),
	('SID00111', 'F L Vargas College', 'Pamplona, Cagayan'),
    ('SID00112', 'Far Eastern University Cavite', 'Silang, Cavite'),
    ('SID00113', 'Far Eastern University East Asia College', 'Sampaloc, Manila'),
    ('SID00114', 'Far Eastern University Institute of Medicine', 'Sampaloc, Manila'),
    ('SID00115', 'Far Eastern University Philippines', 'Sampaloc, Manila'),
    ('SID00116', 'Father Saturnino Urios University', 'Butuan City, Agusan del Norte'),
    ('SID00117', 'Fatima University', 'Valenzuela City'),
    ('SID00118', 'Feati University', 'Manila City, Metro Manila'),
    ('SID00119', 'Fernandez College of Arts and Technology', 'Baliuag, Bulacan'),
    ('SID00120', 'Filamer Christian University', 'Roxas City, Capiz'),
    ('SID00121', 'First Asia Institute of Technology and Humanities', 'Batangas'),
    ('SID00122', 'Foundation University', 'Dumaguete City, Negros Oriental'),
    ('SID00123', 'Gingoog City Colleges', 'Gingoog City, Misamis Oriental'),
    ('SID00124', 'Guagua National Colleges Pampanga', 'Guagua, Pampanga'),
    ('SID00125', 'Guimaras State College', 'Jordan, Guimaras'),
    ('SID00126', 'Holy Angel University', 'Angeles City, Pampanga'),
    ('SID00127', 'Holy Child Colleges of Butuan', 'Butuan City, Agusan del Norte'),
    ('SID00128', 'Holy Cross of Davao College', 'Davao City, Davao del Sur'),
    ('SID00129', 'Holy Name University', 'Tagbilaran City, Bohol'),
    ('SID00130', 'Holy Trinity University Philippines', 'Puerto Princesa City, Palawan'),
    ('SID00131', 'ICCT Colleges', 'San Mateo, Rizal'),
    ('SID00132', 'Ifugao State University', 'Nayon, Lamut, Ifugao'),
    ('SID00133', 'Iligan Computer Institute', 'Iligan City, Lanao del Norte'),
    ('SID00134', 'Iligan Medical Center College', 'Iligan City, Lanao del Norte'),
    ('SID00135', 'Ilocos Sur Community College', 'Candon City, Ilocos Sur'),
    ('SID00136', 'Ilocos Sur Polytechnic State College', 'Ilocos Sur'),
    ('SID00137', 'Iloilo Doctors’ College', 'Iloilo City, Iloilo'),
    ('SID00138', 'Iloilo Science and Technology University (Western Visayas College of Science & Technology)', 'Iloilo City, Iloilo'),
    ('SID00139', 'Informatics Computer Institute', 'Quezon City, Metro Manila'),
    ('SID00140', 'Information and Communications Technology Academy', 'Bacolod City, Negros Occidental'),
    ('SID00141', 'Inspire Sports Academy', 'Calamba City, Laguna'),
    ('SID00142', 'International Graduate School of Leadership (International School of Theology Asia)', 'Quezon City, Metro Manila'),
    ('SID00143', 'Isabela State University', 'Cauayan City, Isabela'),
    ('SID00144', 'Je Mondejar Computer College', 'Tagbilaran City, Bohol'),
    ('SID00145', 'John B Lacson Foundation Maritime University', 'Iloilo City, Iloilo'),
    ('SID00146', 'Jose Maria College', 'Davao City, Davao del Sur'),
    ('SID00147', 'Jose Rizal Memorial State University', 'Dapitan City, Zamboanga del Norte'),
    ('SID00148', 'Jose Rizal University', 'Mandaluyong City'),
    ('SID00149', 'Kalayaan College', 'Quezon City, Metro Manila'),
    ('SID00150', 'La Consolacion College Bacolod', 'Bacolod City, Negros Occidental'),
    ('SID00151', 'La Consolacion University Philippines', 'Malolos City, Bulacan'),
    ('SID00152', 'La Patria College', 'Batac City, Ilocos Norte'),
    ('SID00153', 'La Salle University Ozamiz', 'Ozamiz City, Misamis Occidental'),
    ('SID00154', 'Laguna State Polytechnic University', 'Santa Cruz, Laguna'),
    ('SID00155', 'Leyte Normal University', 'Tacloban City, Leyte'),
    ('SID00156', 'Liceo de Cagayan University', 'Cagayan de Oro City'),
    ('SID00157', 'Lipa City Colleges', 'Lipa City, Batangas'),
    ('SID00158', 'Lorma Colleges MacArthur', 'Carlatan, San Fernando City, La Union'),
    ('SID00159', 'Lyceum Northwestern University', 'Dagupan City, Pangasinan'),
    ('SID00160', 'Lyceum of the Philippines University Batangas', 'Batangas City, Batangas'),
    ('SID00161', 'Lyceum of the Philippines University', 'Intramuros, Manila'),
    ('SID00162', 'Malayan Colleges Laguna', 'Cabuyao, Laguna'),
    ('SID00163', 'Manila Business College', 'Quezon City, Metro Manila'),
    ('SID00164', 'Manila Central University', 'Caloocan City'),
    ('SID00165', 'Manuel L Quezon University', 'Quiapo, Manila City, Metro Manila'),
    ('SID00166', 'Manuel S Enverga University', 'Lucena City, Quezon'),
    ('SID00167', 'Mapua Institute of Technology', 'Intramuros, Manila'),
    ('SID00168', 'Marian College', 'Tagum City, Davao del Norte'),
    ('SID00169', 'Mariano Marcos State University', 'Batac City, Ilocos Norte'),
    ('SID00170', 'Maritime Academy of Asia and the Pacific Kamaya Point', 'Mariveles, Bataan'),
    ('SID00171', 'Mater Dei College Bohol', 'Tubigon, Bohol'),
    ('SID00172', 'Metro Dumaguete College', 'Dumaguete City, Negros Oriental'),
    ('SID00173', 'MHAM College of Medicine', 'Cebu City, Cebu'),
    ('SID00174', 'Microcity College of Business and Technology', 'San Fernando City, La Union'),
    ('SID00175', 'Mindanao State University at Naawan', 'Naawan, Misamis Oriental'),
    ('SID00176', 'Mindanao State University General Santos', 'General Santos City'),
    ('SID00177', 'Mindanao State University Iligan Institute of Technology', 'Iligan City, Lanao del Norte'),
    ('SID00178', 'Mindanao State University Marawi City', 'Marawi City, Lanao del Sur'),
    ('SID00179', 'Mindanao State University Tawi-Tawi College of Technology and Oceanography', 'Bongao, Tawi-Tawi'),
    ('SID00180', 'Mindanao State University', 'Marawi City, Lanao del Sur'),
    ('SID00181', 'Mindoro State University', 'Calapan City, Oriental Mindoro'),
    ('SID00182', 'Miriam College', 'Quezon City'),
    ('SID00183', 'Misamis University', 'Ozamiz City, Misamis Occidental'),
    ('SID00184', 'Mountain Province State Polytechnic College', 'Bontoc, Mountain Province'),
    ('SID00185', 'Mountain View College Philippines', 'Bukidnon'),
    ('SID00186', 'MSC Institute of Technology', 'Cainta, Rizal'),
    ('SID00187', 'Naga College Foundation', 'Naga City, Camarines Sur'),
    ('SID00188', 'National College of Business and Arts NCBA', 'Quezon City, Metro Manila'),
    ('SID00189', 'National College of Science and Technology', 'Dasmariñas, Cavite'),
    ('SID00190', 'National Defense College of the Philippines', 'Quezon City'),
    ('SID00191', 'National Teachers College Philippines', 'Manila City, Metro Manila'),
    ('SID00192', 'National University Philippines', 'Sampaloc, Manila'),
    ('SID00193', 'Negros College', 'Kabankalan City, Negros Occidental'),
    ('SID00194', 'Negros Oriental State University (Central Visayas Polytechnic College)', 'Dumaguete City, Negros Oriental'),
    ('SID00195', 'New Era University', 'Quezon City, Metro Manila'),
    ('SID00196', 'Northeastern college', 'Santiago City, Isabela'),
    ('SID00197', 'Northern Luzon Adventist College', 'Artacho, Sison, Pangasinan'),
    ('SID00198', 'Northern Negros State College of Science & Technology', 'Sagay City, Negros Occidental'),
    ('SID00199', 'Northwest Samar State University', 'Calbayog City, Samar'),
    ('SID00200', 'Northwestern University Laoag City', 'Laoag City, Ilocos Norte'),
    ('SID00201', 'Norzagaray College', 'Norzagaray, Bulacan'),
    ('SID00202', 'Notre Dame of Dadiangas University', 'General Santos City, South Cotabato'),
    ('SID00203', 'Notre Dame of Kidapawan College', 'Kidapawan City, Cotabato'),
    ('SID00204', 'Notre Dame of Marbel University', 'Koronadal City, South Cotabato'),
    ('SID00205', 'Notre Dame University Cotabato', 'Cotabato City, Maguindanao'),
    ('SID00206', 'Nueva Ecija University of Science and Technology', 'Cabanatuan City, Nueva Ecija'),
    ('SID00207', 'Nueva Vizcaya State University', 'Bayombong, Nueva Vizcaya'),
    ('SID00208', 'NYK-TDG Maritime Academy', 'Canlubang, Calamba City, Laguna'),
    ('SID00209', 'Occidental Mindoro State College', 'San Jose, Occidental Mindoro'),
    ('SID00210', 'Our Lady of the Pillar College Cauayan', 'Cauayan City, Isabela'),
    ('SID00211', 'Palawan State University', 'Puerto Princesa'),
    ('SID00212', 'Palompon Institute of Technology', 'Palompon, Leyte'),
    ('SID00213', 'Pampanga State Agricultural University', 'Magalang, Pampanga'),
    ('SID00214', 'Pangasinan State University', 'Lingayen, Pangasinan'),
    ('SID00215', 'PanPacific University North Philippines', 'Urdaneta City, Pangasinan'),
    ('SID00216', 'Partido State University', 'Camarines Sur'),
    ('SID00217', 'Pasig Catholic College', 'Pasig City, Metro Manila'),
    ('SID00218', 'PATTS College of Aeronautics', 'Pasay City, Metro Manila'),
    ('SID00219', 'Philippine Christian University', 'Manila City'),
    ('SID00220', 'Philippine College of Criminology', 'Manila City, Metro Manila'),
    ('SID00221', 'Philippine College of Ministry', 'Quezon City, Metro Manila'),
    ('SID00222', 'Philippine Merchant Marine Academy', 'San Narciso, Zambales'),
    ('SID00223', 'Philippine Military Academy', 'Baguio City, Benguet'),
    ('SID00224', 'Philippine National Police Academy', 'Silang, Cavite'),
    ('SID00225', 'Philippine Normal University', 'Manila City'),
    ('SID00226', 'Philippine School of Business Administration', 'Quezon City, Metro Manila'),
    ('SID00227', 'Philippine Women’s University', 'Malate, Manila'),
    ('SID00228', 'PLT College', 'Butuan City, Agusan del Norte'),
    ('SID00229', 'Polytechnic University of the Philippines', 'Sta. Mesa, Manila'),
    ('SID00230', 'President Ramon Magsaysay State University', 'Iba, Zambales'),
    ('SID00231', 'Quirino State University', 'Diffun, Quirino'),
    ('SID00232', 'Republic Central Colleges', 'Quezon City, Metro Manila'),
    ('SID00233', 'Riverside College', 'Bacolod City, Negros Occidental'),
    ('SID00234', 'Rizal Technological University', 'Mandaluyong City'),
    ('SID00235', 'Rogationist College', 'Tagaytay City, Cavite'),
    ('SID00236', 'Romblon State University', 'Odiongan, Romblon'),
    ('SID00237', 'Sacred Heart College Lucena City', 'Lucena City, Quezon'),
    ('SID00238', 'Saint Ferdinand College', 'Urdaneta City, Pangasinan'),
    ('SID00239', 'Saint Francis of Assisi College Cavite', 'Dasmariñas, Cavite'),
    ('SID00240', 'Saint Joseph College Maasin', 'Maasin City, Southern Leyte'),
    ('SID00241', 'Saint Joseph Institute of Technology', 'Butuan City, Agusan del Norte'),
    ('SID00242', 'Saint Jude College', 'Manila City, Metro Manila'),
    ('SID00243', 'Saint Louis College', 'San Fernando City, La Union'),
    ('SID00244', 'Saint Louis University Baguio City', 'Baguio City'),
    ('SID00245', 'Saint Luke’s College of Medicine', 'Quezon City, Metro Manila'),
    ('SID00246', 'Saint Mary’s University of Bayombong', 'Bayombong, Nueva Vizcaya'),
	('SID00247', 'Saint Michael’s College of Laguna', 'Laguna'),
	('SID00248', 'Saint Paul University Dumaguete', 'Dumaguete City, Negros Oriental'),
	('SID00249', 'Saint Paul University Manila', 'Manila City, Metro Manila'),
	('SID00250', 'Saint Paul University Pasig', 'Pasig City, Metro Manila'),
	('SID00251', 'Saint Paul University Philippines', 'Tuguegarao City, Cagayan'),
	('SID00252', 'Salazar Colleges of Science and Institute of Technology', 'Zamboanga City, Zamboanga del Sur'),
	('SID00253', 'Samar State University', 'Catbalogan City, Samar'),
	('SID00254', 'Samson College of Science and Technology', 'Calamba City, Laguna'),
	('SID00255', 'San Antonio de Padua College', 'Roxas City, Capiz'),
	('SID00256', 'San Beda University', 'Mendiola, Manila'),
	('SID00257', 'San Carlos College', 'San Carlos City, Pangasinan'),
	('SID00258', 'San Isidro College', 'Malaybalay City, Bukidnon'),
	('SID00259', 'San Pablo Colleges San Pablo City Laguna', 'San Pablo City, Laguna'),
	('SID00260', 'San Pedro College of Business Administration', 'San Pedro City, Laguna'),
	('SID00261', 'San Sebastian College Manila', 'Manila City, Metro Manila'),
	('SID00262', 'San Sebastian College Recoletos de Cavite', 'Cavite City, Cavite'),
	('SID00263', 'Siena College of Taytay', 'Taytay, Rizal'),
	('SID00264', 'Silliman University', 'Dumaguete City, Negros Oriental'),
	('SID00265', 'Siquijor State College', 'Siquijor, Siquijor'),
	('SID00266', 'Sorsogon State College', 'Sorsogon City, Sorsogon'),
	('SID00267', 'Southeast Asia Interdisciplinary Development Institute', 'Quezon City, Metro Manila'),
	('SID00268', 'Southern City Colleges', 'Zamboanga City, Zamboanga del Sur'),
	('SID00269', 'Southern Leyte State University', 'Sogod, Southern Leyte'),
	('SID00270', 'Southern Luzon State University (Polytechnic College)', 'Lucban, Quezon'),
	('SID00271', 'Southern Philippines Agri Business and Marine and Aquatic School of Technology', 'Malita, Davao Occidental'),
	('SID00272', 'Southville SISFU', 'Las Piñas City, Metro Manila'),
	('SID00273', 'Southway College of Technology', 'San Fernando City, La Union'),
	('SID00274', 'Southwestern University Cebu Philippines', 'Cebu City, Cebu'),
	('SID00275', 'Southwestern University PHINMA', 'Cebu City, Cebu'),
	('SID00276', 'St Augustine School of Nursing', 'Quezon City, Metro Manila'),
	('SID00277', 'St Cecilia’s College Cebu', 'Cebu City, Cebu'),
	('SID00278', 'St Joseph’s College Quezon City', 'Quezon City, Metro Manila'),
	('SID00279', 'St Louis College Valenzuela', 'Valenzuela City, Metro Manila'),
	('SID00280', 'St Marys College', 'Tagum City, Davao del Norte'),
	('SID00281', 'St Nicolas College of Business and Technology', 'San Nicolas, Ilocos Norte'),
	('SID00282', 'St Paul College of Ilocos Sur', 'Bantay, Ilocos Sur'),
	('SID00283', 'St Paul University Iloilo', 'Iloilo City, Iloilo'),
	('SID00284', 'St Paul University Surigao', 'Surigao City, Surigao del Norte'),
	('SID00285', 'St Scholastica’s College', 'Malate, Manila'),
	('SID00286', 'St Vincent’s College', 'Dipolog City, Zamboanga del Norte'),
	('SID00287', 'St. Paul University Quezon City', 'Quezon City, Metro Manila'),
	('SID00288', 'Sultan Kudarat State University', 'Tacurong City, Sultan Kudarat'),
	('SID00289', 'Surigao del Sur State University', 'Tandag City, Surigao del Sur'),
	('SID00290', 'Surigao State College of Technology', 'Surigao City'),
	('SID00291', 'System Technology Institute', 'Cubao, Quezon City'),
	('SID00292', 'Systems Plus Computer College Quezon City', 'Quezon City, Metro Manila'),
	('SID00293', 'Tanchuling College', 'Tagum City, Davao del Norte'),
	('SID00294', 'Tarlac Agricultural University', 'Camarines Norte'),
	('SID00295', 'Tarlac Agricultural University', 'Camarines Norte'),
	('SID00296', 'Tarlac State University','Tarlac City, Tarlac'),
	('SID00297', 'Technological Institute of the Philippines', 'Cubao, Quezon City'),
	('SID00298', 'Technological Research for Advanced Computer Education College', 'San Juan, Metro Manila'),
	('SID00299', 'Technological University of the Philippines', 'Ermita, Manila'),
	('SID00300', 'The Lewis College', 'Sorsogon City, Sorsogon'),
	('SID00301', 'Trinity University of Asia (Trinity College of Quezon City)', 'Quezon City, Metro Manila'),
	('SID00302', 'Universidad Aldersgate', 'Solano, Nueva Vizcaya'),
	('SID00303', 'Universidad de Santa Isabel', 'Naga City, Camarines Sur'),
	('SID00304', 'Universidad de Zamboanga', 'Zamboanga City'),
	('SID00305', 'University of Antique (Polytechnic State College of Antique)', 'Sibalom, Antique'),
	('SID00306', 'University of Asia and the Pacific', 'Pasig City'),
	('SID00307', 'University of Baguio', 'Baguio City'),
	('SID00308', 'University of Batangas', 'Batangas City, Batangas'),
	('SID00309', 'University of Bohol', 'Tagbilaran City, Bohol'),
	('SID00310', 'University of Cagayan Valley', 'Tuguegarao City, Cagayan'),
	('SID00311', 'University of Caloocan City', 'Caloocan City, Metro Manila'),
	('SID00312', 'University of Cebu', 'Cebu City, Cebu'),
	('SID00313', 'University of Cebu', 'Cebu City, Cebu'),
	('SID00314', 'University of Eastern Philippines,', 'Catarman, Northern Samar'),
	('SID00315', 'University of Iloilo', 'Iloilo City, Iloilo'),
	('SID00316', 'University of La Salette', 'Santiago City, Isabela'),
	('SID00317', 'University of Luzon', 'Dagupan City, Pangasinan'),
	('SID00318', 'University of Makati', 'Makati City, Metro Manila'),
	('SID00319', 'University of Manila', 'Manila City, Metro Manila'),
	('SID00320', 'University of Mindanao', 'Davao City'),
	('SID00321', 'University of Negros Occidental Recoletos', 'Bacolod City'),
	('SID00322', 'University of Northeastern Philippines', 'Iriga City, Camarines Sur'),
	('SID00323', 'University of Northern Philippines', 'Vigan City, Ilocos Sur'),
	('SID00324', 'University of Nueva Caceres', 'Naga City, Camarines Sur'),
	('SID00325', 'University of Pangasinan', 'Dagupan City, Pangasinan'),
	('SID00326', 'University of Perpetual Help System Dalta', 'Las Piñas City'),
	('SID00327', 'University of Perpetual Help System Laguna', 'Biñan City, Laguna'),
	('SID00328', 'University of Rizal System', 'Morong, Rizal'),
	('SID00329', 'University of Saint Anthony Iriga City', 'Iriga City, Camarines Sur'),
	('SID00330', 'University of Saint La Salle Bacolod', 'Bacolod City, Negros Occidental'),
	('SID00331', 'University of Saint Louis Tuguegarao', 'Tuguegarao City, Cagayan'),
	('SID00332', 'University of San Agustin', 'Iloilo City'),
	('SID00333', 'University of San Carlos', 'Cebu City'),
	('SID00334', 'University of San Jose Recoletos', 'Cebu City'),
	('SID00335', 'University of Santo Tomas', 'Sampaloc, Manila'),
	('SID00336', 'University of Science and Technology of Southern Philippines USTP', 'Cagayan de Oro City'),
	('SID00337', 'University of Southeastern Philippines', 'Davao City'),
	('SID00338', 'University of Southern Mindanao', 'Kabacan, Cotabato'),
	('SID00339', 'University of Sto Tomas Legazpi Bicol Dominican University', 'Legazpi City, Albay'),
	('SID00340', 'University of the Assumption', 'San Fernando City, Pampanga'),
	('SID00341', 'University of the City of Manila', 'Intramuros, Manila'),
	('SID00342', 'University of the Cordilleras (Baguio Colleges Foundation)', 'Baguio City'),
	('SID00343', 'University of the East Ramon Magsaysay', 'Quezon City, Metro Manila'),
	('SID00344', 'University of the East', 'Sampaloc, Manila'),
	('SID00345', 'University of the Immaculate Conception', 'Davao City'),
	('SID00346', 'University of the Philippines Diliman', 'Diliman, Quezon City'),
	('SID00347', 'University of the Philippines Baguio', 'Baguio City'),
	('SID00348', 'University of the Philippines Cebu', 'Cebu City'),
	('SID00349', 'University of the Philippines Manila', 'Ermita, Manila'),
	('SID00350', 'University of the Philippines Mindanao', 'Mintal, Davao City'),
	('SID00351', 'University of the Philippines Visayas', 'Iloilo City, Iloilo'),
	('SID00352', 'University of the Philippines', 'Ermita, Manila'),
	('SID00353', 'University of the Visayas', 'Cebu City, Cebu'),
	('SID00354', 'Urdaneta City University', 'Urdaneta City, Pangasinan'),
	('SID00355', 'Virgen Milagrosa University Foundation', 'San Carlos City, Pangasinan'),
	('SID00356', 'Visayas State University', 'Baybay City, Leyte'),
	('SID00357', 'Wesleyan University Philippines', 'Cabanatuan City, Nueva Ecija'),
	('SID00358', 'West Visayas State University', 'La Paz, Iloilo City'),
	('SID00359', 'Western Institute of Technology', 'Iloilo City, Iloilo'),
	('SID00360', 'Western Leyte College of Ormoc City', 'Ormoc City, Leyte'),
	('SID00361', 'Western Mindanao State University', 'Zamboanga City'),
	('SID00362', 'Western Philippines University', 'Aborlan, Palawan'),
	('SID00363', 'Xavier University Ateneo de Cagayan', 'Cagayan de Oro City'),
	('SID00364', 'Zamboanga Peninsula Polytechnic State University', 'Dipolog City, Zamboanga del Norte'),
	('SID00365', 'Zamboanga State College of Marine Sciences and Technology', 'Zamboanga City, Zamboanga del Sur'),
    ('SID00366', 'St. Vincent College of Cabuyao', 'Cabuyao City, Laguna'),
	('SID00367', 'Pulo National High School', 'Cabuyao City, Laguna'),
	('SID00368', 'Philippine Science High School', 'Diliman, Quezon City'),
	('SID00369', 'University of the East', 'Sampaloc, Manila City'),
	('SID00370', 'Japan-Philippines Institute of Technology - Plaridel Campus',	'Plaridel, Bulacan');

-- -- ------------------------------------------------------------------------------
-- ------------------------------ SCHOOL DETAILS -----------------------------------
-- ---------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS school (
    applicantNo INT NOT NULL,
    school_ID VARCHAR(8) NOT NULL,
    schoolName VARCHAR(255) NOT NULL,
    schoolAddress VARCHAR(255) NOT NULL,
    dateGraduated DATE NOT NULL,
    educationAttainment CHAR(3) NOT NULL,
    PRIMARY KEY (applicantNo, school_ID),
    FOREIGN KEY (applicantNo) REFERENCES applicant_details(applicantNo) ON DELETE CASCADE
);

-- INSERT DATA INTO THE TABLE
INSERT INTO school (applicantNo, school_ID, schoolName, schoolAddress, dateGraduated, educationAttainment)
VALUES 
	(1, 'SID00368', 'Philippine Science High School', 'Diliman, Quezon City', '2011-05-09', 'SHS'),
	(1, 'SID00346', 'University of the Philippines Diliman', 'Diliman, Quezon City,', '2015-01-06', 'CO'),
	(2, 'SID00370', 'Japan-Philippines Institute of Technology - Plaridel Campus', 'Plaridel, Bulacan', '2013-03-23', 'SHS'),
	(3, 'SID00229', 'Polytechnic University of the Philippines', 'Sta. Mesa, Manila', '1994-05-27', 'CO'),
	(4, 'SID00229', 'Polytechnic University of the Philippines', 'Sta. Mesa, Manila', '2019-07-26', 'CO'),
	(5, 'SID00297', 'Technological Institute of the Philippines', 'Cubao, Quezon City', '1994-05-27', 'CO'),
	(6, 'SID00025', 'Ateneo de Manila University', 'Katipunan Ave, Quezon City', '2002-04-24', 'SHS'),
	(6, 'SID00115', 'Far Eastern University', 'Sampaloc, Manila', '2018-04-19', 'CO'),
	(7, 'SID00229', 'Polytechnic University of the Philippines', 'Sta. Mesa, Manila', '2023-05-29', 'CO');

-- ------------------------------------------------------------------------------
-- -------------------------- MAJOR SKILLS DB------------------------------------
-- ------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS skills_db (
	skillcode VARCHAR(7) PRIMARY KEY NOT NULL,
    skillName VARCHAR(100) NOT NULL
);

-- INSERT DATA INTO THE TABLE
INSERT INTO skills_db (skillcode, skillName)
VALUES
	('SC00001', 'Adaptability'),
	('SC00002', 'Agile'),
	('SC00003', 'Analytical'),
	('SC00004', 'Backend'),
	('SC00005', 'Client-focused'),
	('SC00006', 'Cloud Computing'),
	('SC00007', 'Collaboration'),
	('SC00008', 'Communication'),
	('SC00009', 'Creativity'),
	('SC00010', 'Critical Thinking'),
	('SC00011', 'Customer Service'),
	('SC00012', 'DevOps'),
	('SC00013', 'Documentation'),
	('SC00014', 'Languages and Frameworks'),
	('SC00015', 'Leadership'),
	('SC00016', 'Maintenance'),
	('SC00017', 'Networking'),
	('SC00018', 'Optimization'),
	('SC00019', 'Problem Solving'),
	('SC00020', 'Programming'),
	('SC00021', 'Project Management'),
	('SC00022', 'Quality Assurance'),
	('SC00023', 'Security'),
	('SC00024', 'Self-Motivation'),
	('SC00025', 'Technical Support'),
	('SC00026', 'Testing'),
	('SC00027', 'Time Management'),
	('SC00028', 'Troubleshooting'),
	('SC00029', 'UX/UI Design'),
	('SC00030', 'Version Control');

-- -- ------------------------------------------------------------------------------
-- ------------------------------- MAJOR SKILLS ------------------------------------
-- ---------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS major_skill (
	applicantNo INT NOT NULL,
    skillcode VARCHAR(7) NOT NULL,
    PRIMARY KEY (applicantNo, skillcode),
    FOREIGN KEY (applicantNo) REFERENCES applicant_details(applicantNo) ON DELETE CASCADE,
    FOREIGN KEY (skillcode) REFERENCES skills_db(skillcode)
);

-- INSERT DATA INTO THE TABLE
INSERT INTO major_skill (applicantNo, skillcode)
VALUES
	(1, 'SC00025'),
	(1, 'SC00028'),
	(1, 'SC00017'),
	(2, 'SC00017'),
	(2, 'SC00021'),
	(2, 'SC00002'),
	(3, 'SC00028'),
	(3, 'SC00016'),
	(3, 'SC00018'),
	(4, 'SC00025'),
	(4, 'SC00028'),
	(4, 'SC00016'),
	(4, 'SC00023'),
	(4, 'SC00007'),
	(4, 'SC00005'),
	(5, 'SC00025'),
	(5, 'SC00028'),
	(5, 'SC00020'),
	(6, 'SC00028'),
	(6, 'SC00018'),
	(6, 'SC00004'),
	(6, 'SC00026'),
	(7, 'SC00028'),
	(7, 'SC00002'),
	(7, 'SC00007'),
	(7, 'SC00003'),
	(7, 'SC00009');


-- ------------------------------------------------------------------------------
-- -------------------------- WORK EXPERIENCE -----------------------------------
-- ------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS work_experience (
    w_dump_id INT AUTO_INCREMENT,
    applicantNo INT NOT NULL,
    employmentHistory_ID VARCHAR(7) NOT NULL,
    companyName VARCHAR(50) NOT NULL,
    workStarted DATE NOT NULL,
    workEnded DATE NOT NULL,
    workPosition VARCHAR(30) NOT NULL,
    reasonForLeaving VARCHAR(200) NOT NULL,
    PRIMARY KEY (w_dump_id, applicantNo, employmentHistory_ID),
    FOREIGN KEY (applicantNo) REFERENCES applicant_details(applicantNo) ON DELETE CASCADE
);

-- INSERT DATA INTO THE TABLE
INSERT INTO work_experience (applicantNo, employmentHistory_ID, companyName, workStarted, workEnded, workPosition, reasonForLeaving)
VALUES 
	(1, 'EH00001',' DBZ Solutions', '2015-05-05', '2016-11-25', 'Technical Support Specialist', 'Contract ended'),
	(1, 'EH00002',' ABC Corporation', '2017-01-01', '2023-05-25', 'IT Support Analyst', 'Resigned'),
	(2, 'EH00003',' JKL Systems', '2017-08-10', '2018-06-10', 'IT Project Coordinator', 'Contract ended'),
	(2, 'EH00004',' XYZ Corporation', '2019-01-01', '2023-02-13', 'IT Security Specialist', 'Relocation'),
	(3, 'EH00005',' QWE Company', '2019-12-11', '2023-05-16', 'Data Administrator', 'Contract ended'),
	(4, 'EH00006',' ABC Corporation', '2012-01-23', '2023-06-01', 'IT Support Specialist', 'Burnout'),
	(4, 'EH00007',' ASD Enterprise', '1995-01-28', '2000-07-23', 'Network Administrator', 'Contract ended'),
	(4, 'EH00008',' YUP Intelligence', '2000-08-01', '2012-01-15', 'Cloud Engineer', 'Relocation'),
	(5, 'EH00009',' DBZ Solutions', '2020-03-28', '2023-06-07', 'Quality Assurance', 'Contract ended'),
	(5, 'EH00010',' XYZ Corporation', '2003-05-20', '2010-11-01', 'Software Developer', 'Contract ended'),
	(5, 'EH00011',' YES Enterprise', '2011-03-19', '2020-02-09', 'IT Project Manager', 'Bankrupt'),
	(6, 'EH00012',' ABC Corporation', '2020-02-20', '2022-08-19', 'Network Engineer', 'Contract ended'),
	(6, 'EH00013',' QWE Company', '2011-05-15', '2019-10-03', 'Data Analyst', 'Contract ended'),
	(6, 'EH00014',' YES Enterprise', '2019-10-15', '2020-02-09', 'UI/UX Designer', 'Bankrupt'),
	(7, 'EH00015',' ABC Corporation', '2012-01-23', '2018-06-10', 'Data Administrator', 'Relocation');


-- ------------------------------------------------------------------------------
-- ------------------------- STORE PROCEDURES -----------------------------------
-- ------------------------------------------------------------------------------

-- STORED PROCEDURE TO COUNT TOTAL APPLICANTS
DELIMITER //

CREATE PROCEDURE CountTotalApplicants()
BEGIN
	-- Declare variables
    DECLARE totalApplicants INT;
    
    -- Count total applicants
    SELECT COUNT(*) INTO totalApplicants
    FROM applicant_details;
    
    SELECT totalApplicants AS Total_Applicants;
END//

DELIMITER ;


-- STORED PROCEDURE TO COUNT FULL-TIME APPLICANTS
DELIMITER //

CREATE PROCEDURE CountFullTimeApplicants()
BEGIN
	-- Declare variables
    DECLARE fullTimeApplicants INT;
	
    -- Count full-time applicants
    SELECT COUNT(*) INTO fullTimeApplicants
    FROM applicant_details
    WHERE employmentType = 'Full-time';

    -- Return full-time applicants
    SELECT fullTimeApplicants AS Full_Time;
END//

DELIMITER ;



-- STORED PROCEDURE TO COUNT FULL-TIME APPLICANTS
DELIMITER //

CREATE PROCEDURE CountPartTimeApplicants()
BEGIN
	-- Declare variables
    DECLARE partTimeApplicants INT;
	
    -- Count full-time applicants
    SELECT COUNT(*) INTO partTimeApplicants
    FROM applicant_details
    WHERE employmentType = 'Part-time';

    -- Return full-time applicants
    SELECT partTimeApplicants AS Part_Time;
END//

DELIMITER ;



-- STORED PROCEDURE TO GET THE AVERAGE DESIRED SALARY OF THE APPLICANTS
DELIMITER //

CREATE PROCEDURE AverageDesiredSalary()
BEGIN
    SELECT AVG(desiredSalary) AS Desired_Salary
    FROM applicant_details;
END //

DELIMITER ;



-- STORED PROCEDURE TO COUNT THE MOST COMMON JOB POSITION IN THE APPLICATION
DELIMITER //

CREATE PROCEDURE CountJobPos()
BEGIN
	SELECT jobPosition, COUNT(*) AS Total_Count
	FROM applicant_details
	GROUP BY jobPosition;
END //

DELIMITER ;


-- STORED PROCEDURE TO DISPLAY THE TOTAL COUNT IN EACH COMMON SKILL LIMITED TO 8
DELIMITER //

CREATE PROCEDURE CountCommonSkill()
BEGIN
	SELECT sdb.skillName, COUNT(*) AS Total
	FROM major_skill AS ms 
	JOIN skills_db AS sdb ON ms.skillcode = sdb.skillcode
	GROUP BY sdb.skillName
	ORDER BY COUNT(*) desc
	LIMIT 8;
END //

DELIMITER ;


-- STORED PROCEDURE TO DISPLAY THE APPLICANT DETAILS
DELIMITER //

CREATE PROCEDURE DisplayApplicants()
BEGIN
	SELECT applicantNo, name, dateOfBirth, SSS_ID, CONCAT_WS(', ', address, city, province, zipcode) AS Address
	FROM applicant_details
	ORDER BY applicantNo ASC;
END //

DELIMITER ;



-- STORED PROCEDURE TO DISPLAY THE APPLICANT DETAILS BY NAME
DELIMITER //

CREATE PROCEDURE DisplayApplicantsByName(
    IN filter_name VARCHAR(50) -- Parameter to specify the name for filtering
)
BEGIN
    -- Execute the query with filtering by name
    SELECT applicantNo, name, dateOfBirth, SSS_ID, CONCAT_WS(', ', address, city, province, zipcode) AS Address
    FROM applicant_details
    WHERE name LIKE CONCAT('%', filter_name, '%')
    ORDER BY applicantNo ASC;
END //

DELIMITER ;



-- STORED PROCEDURE TO DISPLAY THE APPLICANT DETAILS IN THE FIRST PAGE
DELIMITER //

CREATE PROCEDURE GetApplicantDetails(IN applicantNumber INT)
BEGIN
    SELECT 
        name, dateOfBirth, SSS_ID, address, city, province, zipcode, phoneNumber, emailAddress
    FROM 
        applicant_details
    WHERE 
        applicantNo = applicantNumber;
END //

DELIMITER ;



-- STORED PROCEDURE TO UPDATE THE APPLICANT DETAILS
DELIMITER //
CREATE PROCEDURE UpdateApplicantDetails(d_id INT, d_name VARCHAR(50), d_dateOfBirth DATE, d_SSS_ID VARCHAR(15), d_address VARCHAR(100), d_city VARCHAR(30), d_province VARCHAR(30), d_zipcode INT, d_phoneNumber VARCHAR(12), d_emailAddress VARCHAR(40))
BEGIN
    UPDATE applicant_details SET 
        name = d_name, 
        dateOfBirth = d_dateOfBirth, 
        SSS_ID = d_SSS_ID, 
        address = d_address, 
        city = d_city, 
        province = d_province, 
        zipcode = d_zipcode, 
        phoneNumber = d_phoneNumber, 
        emailAddress = d_emailAddress 
    WHERE applicantNO = d_id;
END //
DELIMITER ;

-- STORED PROCEDURE TO DELETE APPLICANT INFO
DELIMITER //
CREATE PROCEDURE DeleteApplicantInfo(IN applicantNoToDelete INT)
BEGIN
	DELETE FROM applicant_details WHERE applicantNo = applicantNoToDelete;
END //
DELIMITER ;








