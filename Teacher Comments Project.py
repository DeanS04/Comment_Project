import csv
conferences = []

with open('teacher_comments.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    header = csvfile.readline().split(',')
    for row in data:
            conferences.append(row)

