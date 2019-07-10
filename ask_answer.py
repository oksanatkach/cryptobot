from config_dialogflow import detect_intent_texts, credentials


def user_answered():
    usr = "YOU: "
    usr_text = input(usr)
    analyzed = detect_intent_texts("crypto-bot-13dcf", "unique", usr_text, "en", credentials)
    return analyzed


def respond(txt):
    bot = "BOT: "
    print(bot + str(txt))
    return txt
