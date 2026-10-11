# keitai-bot

携帯端末と料金プラン選びを手伝う、LangChain の学習用エージェントです。CLI で動きます。

- LLM: Gemini（`langchain-google-genai`）
- Web 検索: Tavily（`langchain-tavily`）
- ツール: `web_search` / `calc_total_cost`（総額計算） / `get_today`（今日の日付）

## 使い方

```bash
uv sync
cp .env.example .env   # GOOGLE_API_KEY と TAVILY_API_KEY を入れる
uv run python main.py
```

終了は `exit` です。
