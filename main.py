from threading import local

from pyscript import display, document

class student:
    def __init__(self, name, section, favoritesubject):
        self.name = name
        self.section = section
        self.favoritesubject = favoritesubject

student1 = student('De Mata', '10-Emerald', 'Social Studies')
student2 = student('Banaag', '10-Emerald', 'Math')
student3 = student('Dellejero', '10-Emerald', 'PE')
student4 = student('Mamauag', '10-Emerald', 'English')
student5 = student('Lim', '10-Emerald', 'VE')

def add(e):
    document.getElementById('output').innerHTML = ""

    name = document.getElementById('name').value
    section = document.getElementById('section').value
    favoritesubject = document.getElementById('favoritesubject').value

    global student67 # SIX SEVENNN
    student67 = student(name, section, favoritesubject)

    display(f'{student67.name} is in {student67.section}. Their favorite subject is {student67.favoritesubject}.', target='output')

def introduce(e):
    document.getElementById('output').innerHTML = ""

    global student1, student2, student3, student4, student5, student6

    display(f'{student1.name} is in {student1.section}. Their favorite subject is {student1.subject}.', target='output')
    display(f'{student2.name} is in {student2.section}. Their favorite subject is {student2.subject}.', target='output')
    display(f'{student3.name} is in {student3.section}. Their favorite subject is {student3.subject}.', target='output')
    display(f'{student4.name} is in {student4.section}. Their favorite subject is {student4.subject}.', target='output')
    display(f'{student5.name} is in {student5.section}. Their favorite subject is {student5.subject}.', target='output')
    display(f'{student67.name} is in {student67.section}. Their favorite subject is {student67.subject}.', target='output')

    student1 = student1
    student2 = student2
    student3 = student3
    student4 = student4
    student5 = student5
    student67 = student67