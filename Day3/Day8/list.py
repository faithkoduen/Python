dog={}
#Add name, color, breed, legs, age to the dog dictionary
dog['name']='Kenzo'
dog['color']='Brown'
dog['breed']='Bulldog'
dog['leg']=4
dog['age']=3

#Create a student dictionary and add first_name, last_name, gender, age, marital status, 
# skills, country, city and address as keys for the dictionary
student={
    'first_name':'Faith',
    'last_name':'Koduen',
    'gender':'female',
    'age':21,
    'marital_status':'single',
    'skills':['Python','Data Analysis'],
    'country':'Kenya',
    'city':'Naiobi',
    'address':'616 Korongo Road'
}

# length of the student dictionary
print(len(student))

#the value of skills and check the data type, it should be a list
skills=student['skills']
print(skills)
print(type(skills))

# #skills values by adding one or two skills
# student['skill'].extend(['UX Research','Product Management'])

keys_list=list(student.keys())
print(keys_list)

values_lists=list(student.values())
print(values_lists)

items_list=(student.items())
print(items_list)

del student['address']
print(student)

del dog
print(dog)