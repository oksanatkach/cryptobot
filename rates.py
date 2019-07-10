import datetime
import dateutil.relativedelta
import re
from ask_answer import user_answered, respond

rate_query = {}


def rates_search(analyzed):
    abbrev = {"Bitcoin": "Btc",
            "Etherium": "Eth",
            "XRP": "XRP",
            "Stellar": "Xlm",
            "Monero": "Xmr",
            "Tether": "Ustd",
            "Litecoin": "Ltc",
            "Cardano": "Ada",
            "EOS": "EOS",
            "Bitcoin Cash": "Bth"
            }

    # get currency if it wasn't given and convert it to abbrev if necessary
    if not analyzed.query_result.parameters.fields["CryptoCoin"].string_value:  # if user indicated no coin
        currency = get_currency()
    else:
        currency = analyzed.query_result.parameters.fields["CryptoCoin"].string_value

    # add currency info to global var
    rate_query.update({"currency": abbrev[currency]})
    
    # print("ONLY CURRENCY")
    # print(rate_query)

    respond("So, I'm searching the current rate of {} for you.".format(currency))

    # check if date is chosen and ask for it (date WITHIN PREVIOUS 30 DAYS!)
    date = analyzed.query_result.parameters.fields["date"].string_value
    # if not date:
        #date = get_date(currency)
        # get_date(currency)

    # rate_query.update({"date": str("-".join([date[8:10], date[5:7]]))})
    return rate_query

               
def get_currency():
    # find searched currency
    respond("Be more precise, what crypto currency do you need?")
    analyzed = user_answered()
    return analyzed.query_result.parameters.fields["CryptoCoin"].string_value # search crypto currency


def get_date(currency): 
    # get the first day 30 days back and convert it to dd.mm.yyyy format
    now = datetime.datetime.now()
    prev = now + dateutil.relativedelta.relativedelta(months=-1)
    date_limit = ".".join([str(prev.day), str(prev.month), str(prev.year)])
    respond("By the way, I can get any rate within the last 30 days if you like.\n" \
            "So, do you want the current rate of {0} or any other since {1}.".format(currency, date_limit))

    analyzed = user_answered()
    new_date = analyzed.query_result.parameters.fields["date"].string_value
    rate_query.update({"date": str("-".join([new_date[8:10], new_date[5:7]]))})
    
    # if user answers "yes" to choose certain date but doesn't indicate it
    if re.search(r"yes|sure|great|yep|yeh", analyzed.query_result.query_text) and not new_date:
        respond("What date exactly?")
        analyzed = user_answered()
        new_date = analyzed.query_result.parameters.fields["date"].string_value
        rate_query.update({"date": str("-".join([new_date[8:10], new_date[5:7]]))})

    # if immediately date is passed
    if rate_query["date"]:
        datetime_date = datetime.datetime.strptime((str(now)[:5] + new_date[5:10]), "%Y-%m-%d")
        if datetime_date < prev:
            respond("Oops, you should have mistaken, I'm not a magician.\n"
                    "I've asked you to choose a date within the previous month, try again.")
            rate_query.update({"date": None})
        else:
            new_date_srt = ".".join([str(prev.day), str(prev.month), str(prev.year)])
            respond("I got it, just a few seconds and you'll have the rates for {0} as of {1}".format(currency, new_date_srt))

