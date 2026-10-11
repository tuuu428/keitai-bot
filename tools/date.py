from datetime import date

from langchain.tools import tool


@tool
def get_today() -> str:
    """今日の日付を YYYY-MM-DD 形式で返す。キャンペーン期限や情報の新しさの判断に使う。"""
    return date.today().isoformat()
