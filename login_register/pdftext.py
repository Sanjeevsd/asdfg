import csv
import re
from io import StringIO
import pdftotext


def pdf_to_txt(f):
    all_data = [['Title', 'Content']]
    reading = pdftotext.PDF(f)
    project_data=StringIO()
    for pages in reading:
        project_data.write(pages)
    project_data_content=project_data.getvalue()
    reading=project_data_content.split("\n")
    title = reading[0].strip()
    body = project_data_content.strip()
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
    return (title,filtered_data)

