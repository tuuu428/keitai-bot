from agent import build_agent


def main():
    agent = build_agent()
    messages = []
    print("携帯相談Bot です。終了は exit")

    while True:
        user = input("\nあなた> ").strip()
        if user in ("exit", "quit"):
            break
        if not user:
            continue

        messages.append({"role": "user", "content": user})
        result = agent.invoke({"messages": messages})
        new_messages = result["messages"][len(messages):]
        messages = result["messages"]

        for m in new_messages:
            for call in getattr(m, "tool_calls", None) or []:
                print(f"  [tool] {call['name']}({call['args']})")

        print(f"\nBot> {messages[-1].text}")


if __name__ == "__main__":
    main()
