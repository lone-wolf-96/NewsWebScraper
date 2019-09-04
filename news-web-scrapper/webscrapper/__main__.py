from multiprocessing import cpu_count
from parmap import map as parallel_exec
from app import App
from bing_search import BingSearch
from google_search import GoogleSearch
from news_advance import NewsAdvance
from search_engine_watch import SearchEngineWatch
from twitter_rss import TwitterRSS

# limit for xml rows
LIMIT = 800

# retrieves search_dictionaries from the xml file
# format {'topic': 'Reputational risk',
# 'keywords': ['company', 'reputation', 'damage']}
search_dictionaries = App.read_xml_file(LIMIT)

if (search_dictionaries is not None):
    # dictionary array for Search classes
    search_classes = [{'index': 0, 'search_engine': GoogleSearch},
                      {'index': 1, 'search_engine': BingSearch},
                      {'index': 2, 'search_engine': SearchEngineWatch},
                      {'index': 3, 'search_engine': NewsAdvance},
                      {'index': 4, 'search_engine': TwitterRSS}]
    count = cpu_count()

    # executes parallel print_results
    parallel_exec(App.print_results, search_classes,
                  search_dictionaries, len(search_classes),
                  pm_processes=count, pm_pbar=True)
