import requests
data={'name':'NIck','email':'emailaddress'}
para={'filename':'demo_form_post'}
r=requests.post("https://tryphp.w3schools.com/showphp.php",data=data,params=para)
print(r.status_code)
f=open('post1.html','w+',encoding="utf-8")
f.write(r.text)