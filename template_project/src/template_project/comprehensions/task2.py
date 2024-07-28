from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

a_tags = [a for a in soup.find_all("a")]

filtered_a_tags = [
    a for a in a_tags if a.get("href") and a["href"].startswith("/wiki/")
]

wiki_links = {a.get_text(): a["href"] for a in filtered_a_tags}

for link_text, link_url in wiki_links.items():
    print(f"{link_text}: {link_url}")
