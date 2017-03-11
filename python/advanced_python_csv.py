import pandas as pd

facultyData = pd.read_csv('faculty.csv')
facultyData.columns =  [i.strip() for i in facultyData.columns]

facultyData.email.to_csv('emails.csv', header=None, index=False)
