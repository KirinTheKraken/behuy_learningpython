#1
dog = {}

# 2
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

#3
student = {
    'first_name': 'Huy',
    'last_name': 'Nguyen',
    'gender': 'Male',
    'age': 17,
    'marital_status': 'Single',
    'skills': ['Python', 'HTML'],
    'country': 'Vietnam',
    'city': 'Hanoi',
    'address': '123 Main Street'
}

#4
print(len(student))

#5
print(student['skills'])
print(type(student['skills']))

#6
student['skills'].extend(['CSS', 'JavaScript'])

#8
print(list(student.values()))

#9
print(list(student.items()))

#10
del student['marital_status']

#11
del dog