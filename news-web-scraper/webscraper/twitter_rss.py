from search import Search
from util import Util


class TwitterRSS(Search):

    def __init__(self, search_dict):
        # sets Twitter RSS URL
        Search.__init__(self, search_dict)
        keywords = self.search_dict['keywords']
        self.url = ("http://twitrss.me/twitter_search_to_rss/" +
                    f"?term={Util.set_plus_format(keywords)}")
