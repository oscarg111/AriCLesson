# classes and inheritance

"""

A way to simplify items that you will call later on in the
program

    - Students in your school
        - GPA
        - Name
        - ID num
    - A class for a student would organize this easier

"""


class Student:
    # called every time you make an object of student
    def __init__(self, gpa, name, id, **kwargs):
        self.gpa1 = gpa
        self.name1 = name
        self.id1 = id
        try:
            self.food = kwargs["food"]
        except:
            pass
        try:
            self.pet = kwargs["pet"]
        except:
            pass
        try:
            self.age = kwargs["age"]
        except:
            pass
        print(kwargs)

    def print_val(self):
        print(self.gpa1, self.id1, self.name1)

    def new_gpa(self, grades):
        """
        set the gpa as the average of the grades being passed in
        """
        sum_grade = 0
        for grade in grades:
            sum_grade += grade
        self.gpa1 = sum_grade / len(grades)


class CollegeStudent(Student):
    def __init__(self, gpa, name, id, major):
        Student.__init__(self, gpa, name, id)
        self.major = major

    def test_method(self):
        print("only college students can use this method")

    def survey_student(self):
        """

        use the input() function to ask questions to college
        students.  Include a question to ask what their major is,
        what their name is, and what their GPA is.  Compare their
        answers to the variables in the class, and print if they are
        lying or not.

        """
        print(f"Welcome to the survey, {self.name1}")
        name = input("What is your name?\n").lower()
        gpa = float(input("What is your gpa?\n"))
        if name == self.name1:
            print("You are telling the truth about your name!")
        else:
            print("You are lying about your name!!!")

        if gpa == self.gpa1:
            print("You are telling the truth about your gpa!")
        else:
            print("You are lying about your gpa!!!")


# create two student objects
ari = Student(3.5, "ari", "111")
eli = Student(3.5, "eli", "112", age=12, sport="soccer", likes_coding=True)

oscar = CollegeStudent(3.5, "oscar", 113, "Computer Science")
oscar.print_val()
oscar.test_method()

ari.print_val()
eli.print_val()

grades = [3.4, 3.7, 2.8, 3.2, 4.0]
eli.new_gpa(grades)
eli.print_val()

oscar.survey_student()
