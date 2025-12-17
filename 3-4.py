CREATE TABLE FACULTIES (
    faculty_id INT IDENTITY(1,1) PRIMARY KEY,
    faculty_name NVARCHAR(50) NOT NULL
)

CREATE TABLE STUDY_FORMS (
    form_id INT IDENTITY(1,1) PRIMARY KEY,
    form_name NVARCHAR(20) NOT NULL
)

CREATE TABLE GROUPS (
    group_id INT IDENTITY(1,1) PRIMARY KEY,
    group_name NVARCHAR(20) NOT NULL,
    course_number INT NOT NULL,
    faculty_id INT NOT NULL,
    form_id INT NOT NULL,
    admission_year INT NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES FACULTIES(faculty_id),
    FOREIGN KEY (form_id) REFERENCES STUDY_FORMS(form_id)
)

CREATE TABLE STUDENTS (
    student_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    middle_name NVARCHAR(50),
    birth_date DATE NOT NULL,
    group_id INT NOT NULL,
    avg_score DECIMAL(3,1),
    admission_date DATE NOT NULL,
    FOREIGN KEY (group_id) REFERENCES GROUPS(group_id)
)

CREATE TABLE TEACHERS (
    teacher_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    middle_name NVARCHAR(50),
    birth_date DATE NOT NULL,
    faculty_id INT NOT NULL,
    form_id INT NOT NULL,
    subject_name NVARCHAR(100) NOT NULL,
    hours_count INT NOT NULL,
    course_number INT NOT NULL,
    start_work_date DATE NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES FACULTIES(faculty_id),
    FOREIGN KEY (form_id) REFERENCES STUDY_FORMS(form_id)
)

INSERT INTO FACULTIES (faculty_name) VALUES
(N'ФПМ'), (N'ФПК'), (N'ФПИ')

INSERT INTO STUDY_FORMS (form_name) VALUES
(N'очная'), (N'заочная')

-- Заполнение таблицы GROUPS
INSERT INTO GROUPS (group_name, course_number, faculty_id, form_id, admission_year) VALUES
(N'ПО135', 1, 1, 1, 2015),
(N'ПО235', 2, 1, 1, 2014),
(N'ПО335', 3, 1, 1, 2013),
(N'ЗП135', 1, 2, 2, 2015),
(N'ЗП235', 2, 2, 2, 2014),
(N'ЗП335', 3, 2, 2, 2013),
(N'ПО145', 1, 3, 1, 2015),
(N'ЗП145', 1, 3, 2, 2015)

-- Заполнение таблицы STUDENTS
INSERT INTO STUDENTS (first_name, last_name, middle_name, birth_date, group_id, avg_score, admission_date) VALUES
(N'Петр', N'Федоренко', N'Романович', '1997-12-25', 1, 8.5, '2015-09-01'),
(N'Ольга', N'Зингел', NULL, '1985-12-25', 1, 7.8, '2015-09-01'),
(N'Надежда', N'Савицкаян', NULL, '1987-09-22', 2, 6.9, '2014-09-01'),
(N'Мария', N'Ковальчук', N'Евгеньевна', '1992-06-17', 2, 9.1, '2014-09-01'),
(N'Татьяна', N'Ковриго', N'Романовна', '1992-05-13', 3, 8.2, '2013-09-01'),
(N'Наталья', N'Шарапо', NULL, '1992-08-14', 3, 7.5, '2013-09-01'),
(N'Иван', N'Ковалев', N'Петрович', '1990-03-15', 4, 6.7, '2015-09-01'),
(N'Анна', N'Бойко', NULL, '1988-11-20', 5, 8.9, '2014-09-01'),
(N'Сергей', N'Остапенко', N'Васильевич', '1991-07-30', 6, 7.2, '2013-09-01'),
(N'Джон', N'Смит', NULL, '1995-04-12', 1, 7.9, '2015-09-01'),
(N'Сара', N'Джонсон', NULL, '1994-07-25', 2, 8.1, '2014-09-01'),
(N'Алексей', N'Сидоров', N'Иванович', '1996-03-15', 4, 6.5, '2015-09-01'),
(N'Елена', N'Коваленко', NULL, '1993-08-20', 5, 8.7, '2014-09-01')

-- Заполнение таблицы TEACHERS
INSERT INTO TEACHERS (first_name, last_name, middle_name, birth_date, faculty_id, form_id, subject_name, hours_count, course_number, start_work_date) VALUES
(N'Иван', N'Петров', N'Сергеевич', '1975-03-15', 1, 1, N'Физика', 200, 1, '2010-09-01'),
(N'Мария', N'Сидорова', NULL, '1980-08-22', 1, 1, N'Математика', 120, 1, '2015-02-15'),
(N'Петр', N'Ковалев', N'Иванович', '1978-11-10', 1, 1, N'Основы алгоритмизации', 70, 2, '2012-03-20'),
(N'Ольга', N'Михайлова', N'Викторовна', '1982-05-30', 2, 2, N'Проектирование БД', 130, 2, '2018-09-01'),
(N'Андрей', N'Смирнов', NULL, '1970-12-05', 2, 2, N'Средства визуального программирования', 120, 3, '2005-01-10'),
(N'Елена', N'Козлова', N'Александровна', '1985-10-18', 1, 1, N'Объектно-ориентированное программирование', 100, 3, '2019-11-15'),
(N'Джон', N'Смит', NULL, '1983-04-12', 2, 2, N'Базы данных', 150, 2, '2020-02-01'),
(N'Сара', N'Джонсон', NULL, '1979-07-25', 1, 1, N'Веб-программирование', 110, 3, '2017-08-20')

#laba3

-- 1. 
SELECT s.first_name,  s.last_name,  f.faculty_name, g.course_number, DATEDIFF(YEAR, s.birth_date, GETDATE()) AS age
FROM STUDENTS s
JOIN GROUPS g ON s.group_id = g.group_id
JOIN FACULTIES f ON g.faculty_id = f.faculty_id
JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
WHERE sf.form_name = N'заочная' AND DATEDIFF(YEAR, s.birth_date, GETDATE()) < 37

-- 2. 
SELECT f.faculty_name, COUNT(s.student_id) AS student_count
FROM FACULTIES f
LEFT JOIN GROUPS g ON f.faculty_id = g.faculty_id
LEFT JOIN STUDENTS s ON g.group_id = s.group_id
GROUP BY f.faculty_name

-- 3. 
SELECT sf.form_name, COUNT(s.student_id) AS student_count
FROM STUDY_FORMS sf
LEFT JOIN GROUPS g ON sf.form_id = g.form_id
LEFT JOIN STUDENTS s ON g.group_id = s.group_id
GROUP BY sf.form_name

-- 4. 
SELECT f.faculty_name, AVG(DATEDIFF(YEAR, s.birth_date, DATEFROMPARTS(YEAR(GETDATE()), 12, 31))) AS avg_age
FROM STUDENTS s
JOIN GROUPS g ON s.group_id = g.group_id
JOIN FACULTIES f ON g.faculty_id = f.faculty_id
GROUP BY f.faculty_name

-- 5. 
SELECT s.first_name, s.last_name, s.admission_date, f.faculty_name, g.course_number, sf.form_name
FROM STUDENTS s
JOIN GROUPS g ON s.group_id = g.group_id
JOIN FACULTIES f ON g.faculty_id = f.faculty_id
JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
WHERE s.middle_name IS NULL

-- 6. 
SELECT TOP 1 f.faculty_name, COUNT(s.student_id) AS student_count
FROM STUDENTS s
JOIN GROUPS g ON s.group_id = g.group_id
JOIN FACULTIES f ON g.faculty_id = f.faculty_id
WHERE YEAR(s.admission_date) = 2015
GROUP BY f.faculty_name
ORDER BY student_count DESC

-- 7. 
SELECT  f.faculty_name, sf.form_name, COUNT(s.student_id) AS student_count
FROM STUDENTS s
JOIN GROUPS g ON s.group_id = g.group_id
JOIN FACULTIES f ON g.faculty_id = f.faculty_id
JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
WHERE YEAR(s.admission_date) = 2014
GROUP BY f.faculty_name, sf.form_name

-- 8. 
SELECT DISTINCT  f.faculty_name
FROM FACULTIES f
JOIN GROUPS g ON f.faculty_id = g.faculty_id
JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
WHERE sf.form_name = N'заочная'

-- 9. 
SELECT DISTINCT f.faculty_name, sf.form_name, g.course_number
FROM FACULTIES f
JOIN GROUPS g ON f.faculty_id = g.faculty_id
JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
ORDER BY f.faculty_name, sf.form_name, g.course_number

-- 10. 
SELECT  f.faculty_name, sf.form_name, COUNT(s.student_id) AS student_count
FROM FACULTIES f
JOIN GROUPS g ON f.faculty_id = g.faculty_id
JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
LEFT JOIN STUDENTS s ON g.group_id = s.group_id
GROUP BY f.faculty_name, sf.form_name
ORDER BY f.faculty_name, sf.form_name

-- 11. 
SELECT  f.faculty_name, sf.form_name, COUNT(s.student_id) AS student_count
FROM FACULTIES f
JOIN GROUPS g ON f.faculty_id = g.faculty_id
JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
LEFT JOIN STUDENTS s ON g.group_id = s.group_id
WHERE g.course_number IN (1, 3)
GROUP BY f.faculty_name, sf.form_name

-- 12.
SELECT  f.faculty_name, g.course_number, COUNT(s.student_id) AS foreign_student_count
FROM FACULTIES f
JOIN GROUPS g ON f.faculty_id = g.faculty_id
LEFT JOIN STUDENTS s ON g.group_id = s.group_id AND s.middle_name IS NULL
GROUP BY f.faculty_name, g.course_number
ORDER BY f.faculty_name, g.course_number

-- 13. 
SELECT  f.faculty_name, g.course_number, COUNT(s.student_id) AS student_count
FROM FACULTIES f
JOIN GROUPS g ON f.faculty_id = g.faculty_id
JOIN STUDENTS s ON g.group_id = s.group_id
WHERE s.avg_score > 7.5
GROUP BY f.faculty_name, g.course_number
ORDER BY f.faculty_name, g.course_number

-- 14. 
SELECT  f.faculty_name, sf.form_name, COUNT(s.student_id) AS student_count
FROM FACULTIES f
JOIN GROUPS g ON f.faculty_id = g.faculty_id
JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
JOIN STUDENTS s ON g.group_id = s.group_id
WHERE DATEDIFF(YEAR, s.birth_date, GETDATE()) > 45
GROUP BY f.faculty_name, sf.form_name
ORDER BY f.faculty_name, sf.form_name

-- 15. 
SELECT  f.faculty_name, sf.form_name, g.course_number, COUNT(s.student_id) AS student_count
FROM FACULTIES f
JOIN GROUPS g ON f.faculty_id = g.faculty_id
JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
JOIN STUDENTS s ON g.group_id = s.group_id
WHERE DATEDIFF(YEAR, s.birth_date, GETDATE()) < 27
GROUP BY f.faculty_name, sf.form_name, g.course_number
ORDER BY f.faculty_name, sf.form_name, g.course_number

-- 16. 
SELECT  f.faculty_name, COUNT(s.student_id) AS student_count
FROM FACULTIES f
JOIN GROUPS g ON f.faculty_id = g.faculty_id
JOIN STUDENTS s ON g.group_id = s.group_id
WHERE s.last_name LIKE N'С%'
GROUP BY f.faculty_name
ORDER BY student_count ASC

#laba4
-- 1. 
CREATE PROCEDURE NUM_ST_FACUL_TUP_OB
    @FACULT_NAME NVARCHAR(50),
    @TUP_OB_NAME NVARCHAR(20)
AS
BEGIN
    SET NOCOUNT ON
    DECLARE @NUM_ST INT
    
    SELECT @NUM_ST = COUNT(s.student_id)
    FROM STUDENTS s
    JOIN GROUPS g ON s.group_id = g.group_id
    JOIN FACULTIES f ON g.faculty_id = f.faculty_id
    JOIN STUDY_FORMS sf ON g.form_id = sf.form_id
    WHERE f.faculty_name = @FACULT_NAME AND sf.form_name = @TUP_OB_NAME

    PRINT N'Факультет: ' + @FACULT_NAME
    PRINT N'Форма обучения: ' + @TUP_OB_NAME
    PRINT N'Количество студентов: ' + CAST(@NUM_ST AS NVARCHAR(10))
END
GO


-- 2. 
CREATE PROCEDURE NUM_ST_PREDMET_FACULTET
AS
BEGIN
    SET NOCOUNT ON

    DECLARE @PRED_FPK INT, @PRED_FPM INT, @PRED_FPI INT,  @NUM_PREDMET INT, @NUM_PREDMET_FACULT INT

    -- Количество предметов на ФПК 
    SELECT @PRED_FPK = COUNT(DISTINCT subject_name)
    FROM TEACHERS t
    JOIN FACULTIES f ON t.faculty_id = f.faculty_id
    WHERE f.faculty_name = N'ФПК'

    -- Количество предметов на ФПМ
    SELECT @PRED_FPM = COUNT(DISTINCT subject_name)
    FROM TEACHERS t
    JOIN FACULTIES f ON t.faculty_id = f.faculty_id
    WHERE f.faculty_name = N'ФПМ'

    -- Количество предметов на ФПИ
    SELECT @PRED_FPI = COUNT(DISTINCT subject_name)
    FROM TEACHERS t
    JOIN FACULTIES f ON t.faculty_id = f.faculty_id
    WHERE f.faculty_name = N'ФПИ'

    -- Общее количество уникальных предметов
    SELECT @NUM_PREDMET = COUNT(DISTINCT subject_name)
    FROM TEACHERS

    -- Количество дублирующихся названий предметов 
    SELECT @NUM_PREDMET_FACULT = COUNT(*)
    FROM (
        SELECT subject_name
        FROM TEACHERS
        GROUP BY subject_name
        HAVING COUNT(*) > 1
    ) AS Duplicates

    PRINT N'Для ФПК читается ' + CAST(@PRED_FPK AS NVARCHAR(10)) + ' предметов'
    PRINT N'Для ФПМ читается ' + CAST(@PRED_FPM AS NVARCHAR(10)) + ' предметов'
    PRINT N'Для ФПИ читается ' + CAST(@PRED_FPI AS NVARCHAR(10)) + ' предметов'
    PRINT N'Всего ' + CAST(@NUM_PREDMET AS NVARCHAR(10)) + ' предметов (' + CAST(@NUM_PREDMET_FACULT AS NVARCHAR(10)) + ' из которых идентичны)'
END
GO

-- 3. 
CREATE PROCEDURE ADD_STUDENT_FAC_TUP_OB
    @FACULT_NAME NVARCHAR(50),
    @TUP_OB_NAME NVARCHAR(20),
    @BIRTH_DATE DATE,
    @WORK_DATE DATE,
    @NAME_ST_3 NVARCHAR(100),
    @SURNAME_ST_3 NVARCHAR(100),
    @T_NAME_ST_3 NVARCHAR(100) = NULL
AS
BEGIN
    SET NOCOUNT ON

    DECLARE @group_id INT, @faculty_id INT, @form_id INT

    -- Находим faculty_id и form_id
    SELECT @faculty_id = faculty_id FROM FACULTIES WHERE faculty_name = @FACULT_NAME
    SELECT @form_id = form_id FROM STUDY_FORMS WHERE form_name = @TUP_OB_NAME

    -- Проверяем существование группы с указанным факультетом и формой обучения на 1 курсе
    SELECT @group_id = group_id
    FROM GROUPS
    WHERE faculty_id = @faculty_id AND form_id = @form_id AND course_number = 1

    IF @group_id IS NULL
    BEGIN
        PRINT N'Ошибка: указанная комбинация факультета и формы обучения не существует.'
        RETURN
    END

    -- Добавляем студента в таблицу STUDENTS
    INSERT INTO STUDENTS (first_name, last_name, middle_name, birth_date, group_id, admission_date)
    VALUES (@NAME_ST_3, @SURNAME_ST_3, @T_NAME_ST_3, @BIRTH_DATE, @group_id, @WORK_DATE)

    PRINT N'Студент успешно зачислен на 1 курс'
END
GO
