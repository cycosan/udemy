def abc():
    n=1
    print("This is first")
    yield n
    n+=1
    print("second")
    yield n
    n+=1
    print("second")
    yield n
b=abc()
for i in b:
    print(b)