# Part III
#### Q6
print('#### Q6 ####')
print('')

faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}

counter = 0

for (key, val) in faculty_dict.items():
    print('key: %s' % key)

    for v in val:
        print('  value: %s' % ', '.join(v))

    print('')

    counter += 1
    if counter >=3:
        break

print('')

#### Q7
print('#### Q7 ####')
print('')

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],
('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }

counter = 0

for (key, val) in professor_dict.items():
    print('key: %18s   value: %s' % (', '.join(key) , ', '.join(val)))

    counter += 1
    if counter >=3:
        break

print('')

#### Q8
print('#### Q8 ####')
print('')

keylist = sorted(professor_dict.keys(), key = lambda x: x[1])

for k in keylist:
    print('key: %18s   value: %s' % (', '.join(k), ', '.join(professor_dict[k])))
