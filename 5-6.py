-- Создание базы
CREATE DATABASE Lol;

-- Использование базы
USE Lol;

-- Таблица факультетов
CREATE TABLE Faculties (
    faculty_id INT IDENTITY(1,1) PRIMARY KEY,
    faculty_title NVARCHAR(60) NOT NULL
);

-- Таблица форм обучения
CREATE TABLE Forms (
    form_id INT IDENTITY(1,1) PRIMARY KEY,
    form_title NVARCHAR(30) NOT NULL
);

-- Таблица учебных групп
CREATE TABLE GroupsStudy (
    group_id INT IDENTITY(1,1) PRIMARY KEY,
    group_code NVARCHAR(25) NOT NULL,
    course INT NOT NULL,
    faculty_id INT NOT NULL,
    form_id INT NOT NULL,
    year_start INT NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES Faculties(faculty_id),
    FOREIGN KEY (form_id) REFERENCES Forms(form_id)
);

-- Таблица студентов
CREATE TABLE Students (
    student_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    patronymic NVARCHAR(50),
    birth_date DATE NOT NULL,
    group_id INT NOT NULL,
    avg_mark DECIMAL(3,1),
    admission_date DATE NOT NULL,
    FOREIGN KEY (group_id) REFERENCES GroupsStudy(group_id)
);

-- Таблица преподавателей
CREATE TABLE Teachers (
    teacher_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    patronymic NVARCHAR(50),
    birth_date DATE NOT NULL,
    faculty_id INT NOT NULL,
    form_id INT NOT NULL,
    subject NVARCHAR(120) NOT NULL,
    hours INT NOT NULL,
    course INT NOT NULL,
    hire_date DATE NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES Faculties(faculty_id),
    FOREIGN KEY (form_id) REFERENCES Forms(form_id)
);

-- Наполнение справочников
INSERT INTO Faculties (faculty_title) VALUES
(N'ФМ'), (N'ФКН'), (N'ФИ');

INSERT INTO Forms (form_title) VALUES
(N'очная'), (N'заочная');

INSERT INTO GroupsStudy (group_code, course, faculty_id, form_id, year_start) VALUES
(N'CS101', 1, 1, 1, 2015),
(N'CS201', 2, 1, 1, 2014),
(N'CS301', 3, 1, 1, 2013),
(N'IT101', 1, 2, 2, 2015),
(N'IT201', 2, 2, 2, 2014),
(N'IT301', 3, 2, 2, 2013),
(N'MATH101', 1, 3, 1, 2015),
(N'MATH201', 1, 3, 2, 2015);

-- Пример студентов
INSERT INTO Students (first_name, last_name, patronymic, birth_date, group_id, avg_mark, admission_date) VALUES
(N'Петр', N'Федоренко', N'Романович', '1997-12-25', 1, 8.5, '2015-09-01'),
(N'Ольга', N'Зингел', NULL, '1985-12-25', 1, 7.8, '2015-09-01');

-- Пример преподавателей
INSERT INTO Teachers (first_name, last_name, patronymic, birth_date, faculty_id, form_id, subject, hours, course, hire_date) VALUES
(N'Иван', N'Петров', N'Сергеевич', '1975-03-15', 1, 1, N'Физика', 200, 1, '2010-09-01'),
(N'Мария', N'Сидорова', NULL, '1980-08-22', 1, 1, N'Математика', 120, 1, '2015-02-15');

-- Функция гражданства
CREATE FUNCTION fnCitizenship(@patronymic NVARCHAR(100))
RETURNS NVARCHAR(20)
AS
BEGIN
    RETURN (
        CASE 
            WHEN @patronymic IS NULL OR LTRIM(RTRIM(@patronymic)) = '' THEN N'иностранец'
            ELSE N'гражданин'
        END
    )
END;

-- Функция нагрузки преподавателей
CREATE FUNCTION fnTeacherLoad()
RETURNS TABLE
AS RETURN(
    SELECT 
        first_name, 
        last_name, 
        faculty_title,
        SUM(hours) AS TotalHours
    FROM Teachers t
    JOIN Faculties f ON t.faculty_id = f.faculty_id
    GROUP BY first_name, last_name, faculty_title
);

-- Таблица статистики
CREATE TABLE Stats (
    forms_count INT,
    students_count INT
);

INSERT INTO Stats (forms_count, students_count)
VALUES (
    (SELECT COUNT(*) FROM Forms),
    (SELECT COUNT(*) FROM Students)
);

-- Триггер на обновление среднего балла
CREATE TRIGGER trg_StudentAvgUpdate
ON Students
AFTER UPDATE
AS
BEGIN
    IF UPDATE(avg_mark)
    BEGIN
        DECLARE @old DECIMAL(3,1), @new DECIMAL(3,1), @faculty NVARCHAR(60);
        SELECT @old = avg_mark FROM deleted;
        SELECT @new = avg_mark FROM inserted;
        SELECT @faculty = f.faculty_title
        FROM inserted i
        JOIN GroupsStudy g ON i.group_id = g.group_id
        JOIN Faculties f ON g.faculty_id = f.faculty_id;

        IF @new > @old
            PRINT N'Средний балл на факультете ' + @faculty + N' повысился';
        ELSE IF @new < @old
            PRINT N'Средний балл на факультете ' + @faculty + N' снизился';
        ELSE
            PRINT N'Средний балл на факультете ' + @faculty + N' остался прежним';
    END
END;

