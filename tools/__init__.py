from tools.calc import calc_total_cost
from tools.date import get_today
from tools.search import make_web_search


def build_tools() -> list:
    return [make_web_search(), calc_total_cost, get_today]
