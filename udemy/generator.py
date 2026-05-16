iterable = ["Eu", "Você", "__iter__"]
iterator = iter(iterable) #tem __next__ e __iter__

#generator = (n for n in range(100)) #
#for n in generator:
    #print(n)
    

def generator(max):
    for i in range(max):
        yield i


#gen = generator(max=100)
#for num in gen:
    #print(num)


def gen1(gen, *args):
    yield from gen(*args)
    return "Função generator finalizada"
 

g = gen1(generator, 100) 