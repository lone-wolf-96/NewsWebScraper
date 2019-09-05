from bs4 import BeautifulSoup
from excel_writer import ExcelWriter


class App:

    @staticmethod
    def print_results(engine_dictionary, search_dictionaries, length_engines):
        # executes the search_class and retrives the link
        # then prints the result on an excel file
        # splits search_dictionaries depending on begin_from_index
        search_dict_length = (len(search_dictionaries) // length_engines)
        begin_from_index = engine_dictionary['index'] * search_dict_length

        search_class = engine_dictionary['search_engine']

        search_restricted_dict = search_dictionaries[begin_from_index:(
            begin_from_index + search_dict_length)]

        links = []
        for search_dict in search_restricted_dict:
            # dynamic polymorphism
            links.append(search_class(search_dict).get_link())

        class_name = search_class.__name__.upper()
        ExcelWriter.write_excel(class_name, search_restricted_dict, links)

    @staticmethod
    def read_xml_file(results_limit):
        # reads the INPUT.xml file and saves array of
        # dictionaries (topic, keywords)
        try:
            with open("INPUT.xml", "r", encoding='utf-8') as infile:
                contents = infile.read()
                soup = BeautifulSoup(contents, 'xml')
                csv_data = soup.find('csv_data', recursive=False)
                rows = csv_data.find_all('row', recursive=False,
                                         limit=results_limit)
                return [App.reader_helper(row)
                        for row in rows]
        except Exception as e:
            print(f'Error during reading xml file: {str(e)}')
            return None

    @staticmethod
    def reader_helper(row):
        # gets text from topic and keywords in row, replacing
        # keywords into topic if empty
        topic = row.topic.get_text()
        keywords = row.keywords.get_text()
        keywords = (keywords if (len(keywords) > 0) else topic).split()
        return dict(topic=topic, keywords=keywords)
