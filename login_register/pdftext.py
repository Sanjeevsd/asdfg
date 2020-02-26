import csv
import re
from io import StringIO
import pdftotext


def pdf_to_txt(f):
    all_data = [['Title', 'Content']]
    reading = pdftotext.PDF(f)
    with open('../project.txt', 'w') as f:
        f.write("\n\n".join(reading))
        print(f)
    with open("../project.txt", 'r') as fls:
        reading=fls.readlines()
        listToStr = ' '.join([str(elem) for elem in reading])
        title = reading[0].strip()
        body = listToStr.strip()

        '''removes spaces, newlines and tabs'''
        tab_removed = re.sub('\s+', ' ', body)

        '''removes numbers'''
        data_withoutnum = re.sub('\d+', '', tab_removed)

        '''remove_unwanted_strings'''
        new_data = data_withoutnum.replace('.', '').replace('\'', '').replace(',', '').replace('"', '').replace('[',
                                                                                                                '').replace(
            ']', '').replace('(', '').replace(')', '').replace('  ', '').replace('-', '')

        '''removes words whose length <3'''
        removed_words = re.sub(r'\b\w{1,3}\b', ' ', new_data)
        filtered_data = removed_words.replace('  ', '')
        all_data.append([title, filtered_data])
    with open('../project_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(all_data)
    return (title,filtered_data)

