from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
print(response.status_code)
yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")

article_tag=soup.find_all(name="a",class_="storyline")
article_texts=[]
article_links=[]
for article_tag in article_tag:
    text=article_tag.get_text()
    article_texts.append(text)
    link=article_tag.get("href")
    article_links.append(link)
article_upvotes=[int(score.getText().split()[0]) for score in soup.find(name="span",class_="score")]
largest_number=max(article_upvotes)
largest_index=article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_upvotes)
# print(article_upvotes[0].split()[0])


