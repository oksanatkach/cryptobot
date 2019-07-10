import random
import re

from ask_answer import user_answered, respond


def greeting_first():
    greetings = ["Hey! How’s life?", "Howdy!", "G’day mate!", "Hiya!", "Hi! What’s cracking?", "Hey! What’s up?"]
    respond(random.choice(greetings))


def check_greeting(analyzed):
    witty_answers = ["Somewhere between better and best.",
                    "Armed and ready!",
                    "My lawyer says I don’t have to answer that question.",
                    "I could really go for a massage.",
                    "Average. Not terrific, not terrible, just average.",
                    "Maybe one day you'll be lucky enough to find out.",
                    "Nice and dandy like cotton candy."]

    witty = random.choice(witty_answers)
    if re.search(r"sup|what's up|is it|goin|and you|\?|how are|doin", analyzed.query_result.query_text):
        respond(witty + "\n" + analyzed.query_result.fulfillment_text)
    else: 
        respond(analyzed.query_result.fulfillment_text)
