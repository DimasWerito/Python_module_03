

# print numbers of even squares from start to end
# start = 0, end = 10,     0, 2, 4, 6, 8 => 0, 4, 16, 36, 64


def show_even_squeres(start, end = 10, step = 1):
    for i in range(start, end + 1, step):
        if i % 2 == 0:
            print(f"{i} : {i**2}")

show_even_squeres(2, 4, 1) #atguments