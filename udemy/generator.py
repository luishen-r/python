iterable = ["Eu", "Você", "__iter__"]
iterator = iter(iterable) #tem __next__ e __iter__

#generator = (n for n in range(100)) #
#for n in generator:
    #print(n)
    

def generator(n=0, max=1):
    while True:
        yield n
        n += 1
        
        if n >= max:
            return


gen = generator(max=100)
for num in gen:
    print(num)