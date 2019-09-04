from search import Search
from util import Util


class SearchEngineWatch(Search):

    def __init__(self, search_dict):
        # sets SearchEngineWatch RSS URL
        Search.__init__(self, search_dict)
        keywords = self.search_dict['keywords']
        self.url = ("https://searchenginewatch.com/search/" +
                    f"{Util.set_plus_format(keywords)}" +
                    "/feed/rss")
