from ask_answer import user_answered, respond
from greeting import greeting_first, check_greeting
from rates import *
from config_dialogflow import detect_intent_texts


def check_intent(analyzed):
    if analyzed.query_result.intent.display_name == "Welcome":
        # asking how can I help
        check_greeting(analyzed)
    elif analyzed.query_result.intent.display_name == "Rate":
        # get dict with searched currency and date in {"currency": "abbrev", "date": "dd-mm"} format
        rate_query = rates_search(analyzed)
    else:
        respond(analyzed.query_result.fulfillment_text)


if __name__ == "__main__":
    greeting_first()
    analyzed = user_answered()
    while analyzed.query_result.intent.display_name != "Goodbye":
        check_intent(analyzed)
        analyzed = detect_intent_texts("crypto-bot-13dcf", "unique", usr_text, "en", credentials)
        analyzed = user_answered()
        check_intent(analyzed)
