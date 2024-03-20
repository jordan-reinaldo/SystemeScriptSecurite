import csv

data = [
    ['Name','Age','City'],
    ['Jean','25','Paris'],
    ['Marie','30','Lyon'],
    ['Pierre','22','Marseille'],
    ['Sophie','35','Toulouse']
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data)
    

print('File created successfully')

