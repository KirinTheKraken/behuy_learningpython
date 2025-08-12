person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill?", has_python)

skills = person.get('skills', [])

if set(skills) == {'JavaScript', 'React'}:
    title = "He is a front end developer"
elif all(lang in skills for lang in ('Node', 'Python', 'MongoDB')):
    title = "He is a backend developer"
elif all(item in skills for item in ('React', 'Node', 'MongoDB')):
    title = "He is a fullstack developer"
else:
    title = "Unknown title"

print(title)

if person.get('is_marred') and person.get('country') == 'Finland':
    fn = person.get('first_name', '')
    ln = person.get('last_name', '')
    print(f"{fn} {ln} lives in Finland. He is married.")
