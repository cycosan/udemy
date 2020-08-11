import json
import os

if os.path.isfile("./age.json") and os.stat("./age.json").st_size != 0:
    file=open("age.json","r+")
    data=json.loads(file.read())
    print("Cureent age is",data["age"])
    data["age"]=data["age"]+1
    print("new data age",data["age"])
else:
    file=open("age.json","w+")
    data={"name":'Nick' ,"age":16}
    print("no ages found",data["age"])
file.seek(0)
file.write(json.dumps(data))
