from bs4 import BeautifulSoup
# import lxml
with open("website.html") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup)
# print(soup.prettify())
# print(soup.a)

all_anchor_tags=soup.find_all(name='a')
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.get_text())
#     print(tag.get('href'))
heading=soup.find_all(name='h1',id='name')
print(heading)

section_heading=soup.find_all(name='h3',class_='heading')
print(section_heading)
# print(section_heading.name)
# print(section_heading.get("class"))

company_url=soup.select_one(selector="p a")
# company_name=soup.select_one(selector="#id")
heading =soup.select_one(selector=".heading")
print(heading)


print(company_url)




