def multi(multiplier):
    def execute(num):
        return f'{num} x {multiplier} = {num*multiplier}'
    return execute


c1 = multi(5)
print(c1(3))

    
    