import openai

def summarize(body: str, api_key: str):
    """
    Summarizes the given article using the OpenAI GPT-3.5-turbo model.

    Parameters:
        body (str): The full body text of the article to be summarized.
        api_key (str): The OpenAI API key for using the GPT-3.5-turbo model.

    The function uses OpenAI's ChatCompletion API to generate a summary of the article.
    It sets up a conversation with a system, user, and assistant messages to guide the model's response.
    The summary is then printed to the console.
    """
    openai.api_key = api_key
    print("Summarized by GPT3.5-")
    
    # Setting up a conversation with system, user, and assistant messages
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": body},
        {"role": "assistant", "content": "Generate a 275 characters summary."},
    ]

    # Calling OpenAI's ChatCompletion API to get the summary
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=150,
        temperature=0.3,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    # Extracting and printing the generated summary
    summary = response.choices[0].message["content"]
    print(summary.strip())
