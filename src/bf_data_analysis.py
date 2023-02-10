import json

with open('../json/my-basic-fit-data.json') as my_file:
    data = json.load(my_file)

member = data['member']
membership = data['memberships']
friends = data['friends']
articles = data['articles']
transactions = data['transactions']
visits = data['visits']

# Print some member's infos
print('Hello '+member['first_name']+'!')
birth_date = member['birth_date'].split('-')
birth_date[2] = birth_date[2][:2]
print('You were born on '+birth_date[1]+'/'+birth_date[2]+'/'+birth_date[0])

join_date = membership[0]['join_date_g'].split('-')
join_date[2] = join_date[2][:2]
print('You have been a basic fit member since '+join_date[1]+'/'+join_date[2]+'/'+join_date[0])

print('Number of workouts done : '+str(len(visits)))

# Visited Clubs
clubs = set()
for visit in visits:
    clubs.add(visit['club'])

print(clubs)
print('Number of clubs visited : '+str(len(clubs)))
