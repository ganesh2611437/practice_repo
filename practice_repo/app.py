print("hello world!")
def function():
    count=0
    a="Ganesh"
    for s in a:
        if s:
            count+=1
    return count,len(a)

def function1():
    count=0
    a="Ganesh"
    for i in range(len(a)+1):
        if i:
            count+=1
    return count

print(function(),function1())
