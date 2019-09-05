from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


class Search:

    def __init__(self, search_dict):
        self.search_dict = search_dict
        self.url = ''

    def get_link(self):
        # get links using BeautifulSoup from GET response
        response = self.__get_text(self.url)

        if (response is None):
            return ''

        soup = BeautifulSoup(response, 'xml')
        item = soup.find('item')

        if (item is None):
            return ''

        return item.find('link').text

    def __get_text(self, url):
        # makes an HTTP GET request
        # using stream=True defers downloading the response
        # closing closes the connection upon completion
        try:
            response = get(url, stream=True)

            with closing(response):
                if (self.__is_good_response(response)):
                    return response.text
                else:
                    return None
        # logs if occurres an exception
        except RequestException as e:
            print(f'Error during requests to {url} : {str(e)}')
            return None

    def __is_good_response(self, resp):
        # returns if status code is 200 and content-type is not None
        return (resp.status_code == 200 and
                resp.headers['Content-Type'] is not None)
