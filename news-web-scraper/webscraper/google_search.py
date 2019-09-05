from search import Search
from util import Util


class GoogleSearch(Search):

    def __init__(self, search_dict):
        # sets Google News RSS URL
        Search.__init__(self, search_dict)
        keywords = self.search_dict['keywords']
        self.url = ("https://news.google.com/rss/search" +
                    f"?q={Util.set_plus_format(keywords)}" +
                    "&hl=en-US&gl=US&ceid=US:en")
