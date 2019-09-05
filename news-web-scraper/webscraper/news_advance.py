from search import Search
from util import Util


class NewsAdvance(Search):

    def __init__(self, search_dict):
        # sets The News & Advance RSS URL
        Search.__init__(self, search_dict)
        keywords = self.search_dict['keywords']
        self.url = ("https://www.newsadvance.com/search/" +
                    f"?q={Util.set_plus_format(keywords)}" +
                    "&f=rss")
