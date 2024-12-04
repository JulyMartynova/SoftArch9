def process(message, user_alias):
    print(f"Filter 3 received: {message}")
    print(f"User {user_alias} sent: {message}")
    return f"Filter3: {message} (User: {user_alias})"