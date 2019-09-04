import csv
from os import getcwd

# gets file paths
csv_file = getcwd() + "\\" + 'INPUT.csv'
xml_file = getcwd() + "\\" + 'INPUT.xml'


# reads the .csv file and writes a new .xml file
with open(csv_file) as csv_open:
    csvData = csv.reader(csv_open)
    with open(xml_file, 'w', encoding='utf-8') as xml_data:
        xml_data.write('<?xml version="1.0"?>' + "\n")
        # only one top-level tag
        xml_data.write('\t' + '<csv_data>' + "\n")

        for row in csvData:
            xml_data.write('\t'*2 + '<row>' + "\n")
            xml_data.write('\t'*3 + '<topic>' +
                           row[0] + '</topic>' + "\n")
            xml_data.write('\t'*3 + '<keywords>' +
                           row[1].replace('’', '\'') + '</keywords>' + "\n")
            xml_data.write('\t'*2 + '</row>' + "\n")

        xml_data.write('</csv_data>')
