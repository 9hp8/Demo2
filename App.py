print('Hello World HP')

print ("*" * 10)

#Varibales in Python
price = 10;
print("price", price)

rating = 4.9
name = "Josh"
is_published = True


# TASK1: Simple case for variables
# Check in John Smith into the hospital. He is 20 years old and is a new patient.
patient_name = "John Smith"
patient_age = 25
is_new_patient = True

# Taking Input from user
inputName = input('What is your name? ')
print('Hi ' + inputName)

# TASK2: Ask Two Questions - Persons name and favorite color
personName = input('Please enter your name?')
color = input('Enter your favourite color')
print(personName + " likes " + color)

# Calculating Age
birth_year = input("Enter your birth year: ")
#checking type of birth year
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)


# TASK 3: Ask a user their weight in pounds, convert it into kilogram and give it back to user.
weight = input('Enter your weight in pounds: ')
convertedWeight = (int(weight)/2.2)
print('Weight in Kilogram: ' + str(convertedWeight))

# Adding Quotes
course = "Python's course for Beginners"
print(course)

course1 = 'Python course for "Beginners"'
print(course1)

#For a big message to be added or sent in a email we use ''' quotes
course2 = '''
Hii John,

    Thank you for your support,

    Regards
    Priya

    '''
print(course2)

Indexing for the String
course = "Python's course for Beginners"
#Prints the first element
print(course[0])

#Prints the last element
print(course[-1])

#Prints from first element to index 3
print(course[0:4])

# printing index from certain point
print(course[2:])

#Coping everythin into another varliable
another = course[:]
print(another)

value = "Jennifer"
print(value[1:-1])

# Formatted Strings
firstname="John"
lastname ="Smith"
message = firstname +' ['+ lastname + '] ' + 'is a coder'
print(message)
msg = f'{firstname} [{lastname}] is a coder'
print(msg)

#String Methods
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('y'))
print(course.replace('Beginners', 'Absolute Beginners'))

# check existence of a character or string
print('Python' in course)