import requests
params={'q':'pizza'}
r=requests.get("https://www.bing.com/search",params=params)
print(r.url)
f=open("./bing.html",'w',encoding="utf-8")

f.write(r.text)