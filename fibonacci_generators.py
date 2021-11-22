import time


def fibo_gen():
    n_max = 10
    n1 = 0
    n2 = 1
    counter = 0
    while n1 + n2 < n_max:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter +=1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield n2

if __name__ == "__main__":
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        # time.sleep(0.5)