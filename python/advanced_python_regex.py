# Part I - Regular Expressions
#### Q1
import pandas as pd
from pprint import pprint

facultyData = pd.read_csv('faculty.csv')
facultyData.columns =  [i.strip() for i in facultyData.columns]

degrees = []
[degrees.extend(d) for d in facultyData.degree.apply(lambda x: x.split())];

degrees =  [d for d in degrees if  not d.isdigit()]

degreesDict = {}
for d in degrees:
    if d in degreesDict:
        degreesDict[d] += 1
    else:
        degreesDict[d] = 1

pprint(degreesDict)

# output:
# {'B.S.Ed.': 1,
# 'JD': 1,
# 'M.S.': 1,
# 'MA': 1,
# 'MD': 1,
# 'MPH': 2,
# 'MS': 1,
# 'Ph.D': 5,
# 'Ph.D.': 17,
# 'PhD': 9,
# 'Sc.D.': 4,
# 'ScD': 2}

#### Q2
facultyData.title.apply(lambda x: x.replace(' of Biostatistics','').replace(' is Biostatistics','')).value_counts()

# output:
# Professor 13
# Associate Professor 12
# Assistant Professor 12

#### Q3
emails = facultyData.email

# output:
# ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu',
# 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']

#### Q4
import re

facultyData.email.apply(lambda x: re.search("@[\w.]+", x).group()).value_counts()

# output:
# @mail.med.upenn.edu 23
# @upenn.edu 12
# @cceb.med.upenn.edu 1
# @email.chop.edu 1

# Part II
