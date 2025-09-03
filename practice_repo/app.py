print("hello world!")
def function():
    count=0
    a="Ganesh"
    for s in a:
        if s:
            count+=1
    return count,len(a)

def fun():
    count = 0
    z="python"
    for w in z:
        if z:
            count+=1
    return count,len(z)        

print(function(),fun())
