from openai import OpenAI

def call(message):
    client = OpenAI(api_key="")   #   INSERT YOUR API KEY FOR OPENAI AS OpenAI(api_key=*KEY*)"
    response = client.responses.create(
        model="gpt-5",
        input=message
    )
    return response