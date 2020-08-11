import re

print("welcome to calculator")
print("press quit to exit")
exits=True
previous=0
while exits:
    if previous==0:
        equation=input("0")
    else:
        equation=input(str(previous))
        equation=str(previous)+equation
    if equation=='quit':
        exits=False
    else:
        equation=re.sub('[a-zA-Z,"":,]','',equation)
        previous=eval(equation)


