# print('Hello World')

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
lookup(MyNames, 'middle', 'Lie')
print lookup(MyNames, 'middle', 'Lie')

store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
lookup(MyNames, 'first', 'Robin')
print lookup(MyNames, 'first', 'Robin')

store(MyNames, 'Mr. Gumby')
lookup(MyNames, 'middle', '')
print lookup(MyNames, 'middle', '')

store(MyNames, 'Luke Skywalker', 'Anakin Skywalker')
lookup(MyNames, 'last', 'Skywalker')
print lookup(MyNames, 'last', 'Skywalker')