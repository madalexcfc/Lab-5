import re
import codecs
import csv

with open('task1-en.txt') as file1:
    task1 = file1.read()
    print('Слова после которых стоит точка:')
    print(re.findall(r"\b[A-Za-z]+[.]", task1))
    print('Дробные числа:')
    print(re.findall(r"\b[0-9]+[.][0-9]+", task1))

with codecs.open('task2.html', 'r', 'utf-8') as file2:
    task2 = file2.read()
    print('Все значения пикселей:')
    print(re.findall(r"\b\d+px", task2))

with open('result.csv', 'w') as file:

    writer = csv.writer(file, delimiter=' ', quotechar=" ")
    writer.writerow(['ID', 'Name', 'Email', 'Date of Registration', 'Website'])

    with open('task3.txt') as text:
        text = text.read()
        text = re.sub(r' ', r'   ', text)
        text = ' ' + text
        IDs = re.findall(r' \d{1,3} ', text)
        Emails = re.findall(r' [^ ]+@[^ ]+ ', text)
        Names = re.findall(r' [A-Za-z]+ ', text)
        Dates = re.findall(r' [0-9]*-[0-9]*-[0-9]* ', text)
        Sites = re.findall(r' https?:[\/.@a-zA-Z-]+ ', text)
        
    for i in range(len(IDs)):
        writer.writerow([f'{IDs[i]}', f'{Names[i]}', f'{Emails[i]}',\
                         f'{Dates[i]}', f'{Sites[i]}'])



    