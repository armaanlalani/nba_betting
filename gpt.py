from openai import OpenAI

def make_a_query(client, conversation_history, query):
    conversation_history.append({"role": "user", "content": query})
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        stream=True,
    )
    follow_up_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            follow_up_response += chunk.choices[0].delta.content

    conversation_history.append({"role": "assistant", "content": follow_up_response})
    if follow_up_response[-1] == " ":
        follow_up_response = follow_up_response[:-1]
    return client, conversation_history, follow_up_response

client = OpenAI(api_key='')

conversation_history = [
    {"role": "user", "content": "I am going to ask you some questions about pulling data from nba databases. The user is going to provide a statement and the goal is to return a response to them."}
]

stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        stream=True,
    )

response_content = ""
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        response_content += chunk.choices[0].delta.content

conversation_history.append({"role": "assistant", "content": response_content})