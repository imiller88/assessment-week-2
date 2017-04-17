"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages that OO provides are:
        1. encapsulation - you can "encapsulate" functions, or methods, specific
        to a class of objects into the class itself.
        2. abstraction - it "abstracts" the calling of a method from the code
        behind the method itself, allowing for higher efficiency for users of 
        the code who do not need to see or understand the underlying code
        behind a method to call it.
        3. polymorphism - polymorphism allows you to apply different, object-
        specific treatments to a bunch of different objects at once, since the 
        specific treatment can be defined within the object's class. 

2. What is a class?
    A class is a defined object type with methods specific to itself. Classes
    live on a hierarchy that allows them to inherit from other classes and
    pass qualities on to sub- or child classes. There are both built-in classes, 
    or classes predefined by Python, and user-defined classes. All classes descend,
    or inherit, their fundamental properties as objects from the parent class 
    "object".

3. What is an instance attribute?
    An instance attribute is an attribute or quality that is defined to be 
    specific to a single instance, or named object, of a class. Beyond the 
    instance's name, it is what contributes to an instance's uniqueness within
    its class.

4. What is a method?
    A method is a predefined function that is specific to a certain class, i.e. 
    cannot be called on any and all classes of objects. In Python, these are
    distinguishable from regular functions, both built-in and user-defined, by
    their syntax: they are appended to the end of an object by a period,
    rather than wrapped around it with parentheses. It should be noted that 
    methods do change the object within the namespace, whereas functions 
    simply return a changed version of the object as output but leave the 
    original object untouched.

5. What is an instance in object orientation?
    An instance in object orientation is simply an individual occurrence of a 
    class, or a uniquely defined object of that class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute applies to ALL objects of a given class, while an instance
   attribute will apply only to the specific single object, or instance, within 
   which it is defined. Class attributes should be defined for qualities that
   you wish to apply broadly across, and to define, the class itself. 


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        user_answer = raw_input(self.question)
        if user_answer == self.correct_answer:
            return True
        return False

class Exam(object):

    def __init__(self, exam_name):
        self.exam_name = exam_name
        self.questions = []

    def add_question(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.questions.append((question, correct_answer))

    def administer(self):
        questions_answered = 0
        questions_correct = 0
        for self.question in self.questions:
            user_input = raw_input(self.question[0])
            if user_input == self.question[1]:
                questions_correct += 1
                questions_answered += 1
                print "Correct!"
            else:
                questions_answered += 1
                print "Sorry, wrong answer."

        score = 100 * (float(questions_correct) / questions_answered)
        return score

class StudentExam(object):
    def __init__(self, student, exam_name):
        self.student = student
        self.exam_name = exam_name
        self.student_score = "[test not yet taken]"

    def take_test(self, exam_name):
        self.student_score = exam_name.administer()
        print "Score: ", self.student_score

    def __repr__(self):
        return "Student {} has an exam score of {}".format(self.student_name, 
                                                        self.student_score)

def example(student):
    """ Creates an Exam with 3 questions, a Student, a StudentExam, and 
    administers StudentExam.take_test """

    exam = Exam("example")
    exam.add_question(
        "What is the method for adding an element to a set?",
        ".add()")
    exam.add_question(
        'What does pwd stand for?',
        'print working directory')
    exam.add_question(
        'Python lists are mutable, iterable, and what?',
        'ordered')

    example_student = Student(student.first_name, student.last_name, student.address)

    example_student_exam = StudentExam(example_student, exam)
    example_student_exam.take_test(exam)

class Quiz(Exam):
    def __init__(self, exam_name):
        super(Quiz, self).__init__(exam_name)

    def administer(self):
        score = super(Quiz, self).administer()

        if score > 50.0:
            return 1
        else:
            return 0

    def __repr__():
        return "Quiz score is {}".format(score)


