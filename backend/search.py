### Search

#from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch

web_search_tool = TavilySearch(k=3)
#web_search_tool = TavilySearchResults(k=3)

