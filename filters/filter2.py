def process(message, user_alias):
    print(f"Filter 2 received: {message}")
    return message.upper(), user_alias