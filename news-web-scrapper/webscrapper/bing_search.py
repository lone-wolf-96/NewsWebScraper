from search import Search
from util import Util


class BingSearch(Search):

    def __init__(self, search_dict):
        # sets Bing News RSS URL
        Search.__init__(self, search_dict)
        keywords = self.search_dict['keywords']
        self.url = ("https://www.bing.com/news/search" +
                    f"?q={Util.set_plus_format(keywords)}" +
                    "&format=rss&mkt=en-US")
