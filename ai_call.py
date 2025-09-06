from openai import OpenAI

def call(message):
    client = OpenAI()   #   INSERT YOUR API KEY FOR OPENAI AS OpenAI(api_key=*KEY*)"
    response = client.responses.create(
        model="gpt-5-mini",
        input=message
    )
    return response