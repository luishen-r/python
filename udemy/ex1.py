def multi(*args):
    if 0 not in args:
        try:
            total = 1
            for num in args:
                total *= num
            print(total)
        except TypeError:
            print('Digite apenas números.')
    else:
        return

multi(3, 4)