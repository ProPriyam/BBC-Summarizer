import requests
from bs4 import BeautifulSoup

class Article:

    def __init__(self, url: str):
        """
        Initializes the Article object with the given URL.

        Parameters:
            url (str): The URL of the article to scrape.

        Initializes:
            soup (BeautifulSoup): The BeautifulSoup object containing the parsed HTML content of the article.
            body (list): A list containing the paragraphs of the article's body text.
            title (str): The title of the article.
        """
        article = requests.get(url)
        self.soup = BeautifulSoup(article.content, "html.parser")
        self.body = self.get_body()
        self.title = self.get_title()

    def get_body(self) -> list:
        """
        Extracts the body paragraphs of the article.

        Returns:
            list: A list containing the paragraphs of the article's body text.
        """
        body_divs = self.soup.find_all("div", {"data-component": "text-block"})
        if body_divs:
            body = []
            for div in body_divs:
                paragraphs = div.find_all("p")
                for p in paragraphs:
                    body.append(p.text)
            return body
        return []

    def get_title(self) -> str:
        """
        Extracts the title of the article.

        Returns:
            str: The title of the article. If not found, returns an empty string.
        """
        title_element = self.soup.find("h1")
        return title_element.text.strip() if title_element else ""
