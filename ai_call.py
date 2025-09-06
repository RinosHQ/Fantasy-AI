from openai import OpenAI

def call_ai(message):
    client = OpenAI()   #   INSERT YOUR API KEY FOR OPENAI AS api_key=*KEY*"
    response = client.responses.create(
        model="gpt-5-mini",
        input=message
    )
    print(response)