from bs4 import BeautifulSoup
import requests as r


search = input('Enter the thing you want to search for:')
params = {"q": search}

data = r.get('http://www.bing.com/search', params=params)

soup = BeautifulSoup(data.text, "html.parser")
soup.prettify()

results = soup.find("ol", {"id": "b_results"})
print(results)
links = results.findAll("li", {"class": "b_algo"})
print(links)

for item in links:
    item_text = item.find("a").text 
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Parent:",item.find("a").parent)
