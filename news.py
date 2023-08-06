import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime, timedelta, timezone
from Article import Article
from summarize import summarize


class NewsSummarizer:
    def __init__(self, url: str):
        """
        Initializes the NewsSummarizer object with the given URL.

        Parameters:
            url (str): The URL of the news website to scrape for articles.

        Initializes:
            articles (list): A list to store information about the extracted articles.
            seen_titles (set): A set to keep track of seen article titles and avoid duplicates.
            url (str): The URL of the news website.
        """
        self.articles = []
        self.seen_titles = set()
        self.url = url

    def get_articles(
        self,
        openai_api_key: str,
        hours: int = 5,
        body: bool = False,
        summarized: bool = False,
    ):
        """
        Scrapes articles from the news website, filters them based on a time window,
        and prints the relevant information about each article.

        Parameters:
            openai_api_key (str): The OpenAI API key for summarizing the articles.
            hours (int, optional): The time window in hours to filter the articles. Default is 5 hours.
            body (bool, optional): Whether to print the full body of the article. Default is False.
            summarized (bool, optional): Whether to summarize the article using OpenAI API. Default is False.
        """
        current_time = datetime.now(timezone.utc)
        response = requests.get(self.url)
        if response.status_code != 200:
            print(f"Failed to fetch data from {self.url}. Status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, "html.parser")
        container = soup.find("div", id="news-top-stories-container")
        if not container:
            print("Could not find the container for news articles.")
            return

        for article in container.find_all("div", class_="nw-c-promo"):
            try:
                timestamp = article.find(
                    "time",
                    class_="gs-o-bullet__text date qa-status-date gs-u-align-middle gs-u-display-inline",
                ).get("datetime")
                timestamp = timestamp[:-5]
                article_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

                # Convert article_time to UTC timezone
                article_time = article_time.replace(tzinfo=timezone.utc)
                time_at_hours = current_time.replace(
                    hour=hours, minute=0, second=0, microsecond=0
                )

                from_time = current_time - timedelta(hours=hours)

                if article_time >= from_time:
                    title = article.find(
                        "h3", class_="gs-c-promo-heading__title"
                    ).text.strip()
                    summary = article.find(
                        "p", class_="gs-c-promo-summary"
                    ).text.strip()
                    link = urljoin(
                        self.url, article.find("a", class_="gs-c-promo-heading")["href"]
                    )

                    if title not in self.seen_titles:
                        time_diff = current_time - article_time
                        time_diff_hours, time_diff_remainder = divmod(
                            time_diff.seconds, 3600
                        )
                        time_diff_minutes, _ = divmod(time_diff_remainder, 60)
                        self.articles.append(
                            {
                                "title": title,
                                "summary": summary,
                                "link": link,
                                "time": str(time_diff_hours) + "hours ago"
                                if time_diff_hours > 0
                                else str(time_diff_minutes) + "minutes ago",
                            }
                        )
                        self.seen_titles.add(title)

            except AttributeError:
                continue

        print("Number of articles:", len(self.articles))
        for article in self.articles:
            print("Title:", article["title"])
            if "summary" in article:
                print("Summary:", article["summary"])
            print("Time:", article["time"])
            print("Link:", article["link"])

            parsed_article = Article(article["link"])
            if body and not summarized:
                body = " ".join(parsed_article.body)
                print("Body:", body)

            if summarized and not openai_api_key:
                print("Please provide an OpenAI API key to summarize the articles.")
            elif summarized:
                body = " ".join(parsed_article.body)
                summarize(body, openai_api_key)

            print(
                "---------------------------------------------------------------------------------------"
            )




