from news import NewsSummarizer

openai_api_key = ""  # Replace with your API key

summarizer = NewsSummarizer(url="https://bbc.com/news")
summarizer.get_articles(
    openai_api_key=openai_api_key, hours=5, body=False, summarized=True
)
