import dialogflow_v2
from google.oauth2 import service_account


def detect_intent_texts(project_id, session_id, text, language_code, credentials):
    session_client = dialogflow_v2.SessionsClient(credentials=credentials)
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow_v2.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow_v2.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        return response

credentials = service_account.Credentials.from_service_account_file('crypto-bot-6ce5088d9703.json')
