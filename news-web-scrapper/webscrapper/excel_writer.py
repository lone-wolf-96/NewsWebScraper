from os import getcwd
import xlsxwriter


class ExcelWriter:

    @staticmethod
    def write_excel(name, search_dictionaries, links):
        # writes in cells the search results
        # Index | URL | Topic | Keywords structure
        try:
            file_path = getcwd() + "\\" + f'{name}.xlsx'
            workbook = xlsxwriter.Workbook(
                file_path, {'strings_to_urls': False})
            worksheet = workbook.add_worksheet()

            worksheet.write(0, 0, 'Index')
            worksheet.write(0, 1, 'URL')
            worksheet.write(0, 2, 'Topic')
            worksheet.write(0, 3, 'Keywords')

            length = len(search_dictionaries)
            for i in range(length):
                worksheet.write(i + 1, 0, i)
                worksheet.write(i + 1, 1, links[i])
                search_dict = search_dictionaries[i]
                worksheet.write(i + 1, 2, search_dict['topic'])
                keywords = " ".join(search_dict['keywords'])
                worksheet.write(i + 1, 3, keywords)

        # logs if occurres an exception
        except Exception as e:
            print(f'Error during writing in excel file: {str(e)}')
        finally:
            workbook.close()
