STOP_WORDS = ["bird-watching", "ailurophobia", "mango"]

def process(message, user_alias):
    print(f"Filter 1 received: {message}")
    if any(word in message for word in STOP_WORDS):
        print("Message contains stop words, discarding.")
        return None
    return message, user_alias