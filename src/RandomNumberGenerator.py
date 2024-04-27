def random_number_generator(a: int, b: int, seed: int=42) -> int:
    m: int = 2**31 - 1 
    c: int = 0          
    seed: int = (a * seed + b) % m

    random_number: int = a + seed % (b - a + 1)

    return random_number

for i in range(1000,10000):
    print(random_number_generator(1,100,i))