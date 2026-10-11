from langchain_tavily import TavilySearch


def make_web_search() -> TavilySearch:
    """環境変数 TAVILY_API_KEY を使う。"""
    return TavilySearch(name="web_search", max_results=5)
