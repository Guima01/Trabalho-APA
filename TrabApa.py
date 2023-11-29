import time
from random import seed
from random import randint
# seed random number generator

# generate some random numbers


def listCreation(tamanho):
    values = []
    for i in range(tamanho):
        values.append(i)

    return values


def swapPositions(list, size):
    seed()
    pos1 = randint(0, size-1)
    pos2 = randint(0, size-1)

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def achaPivo(array, begin, end):
    pos = begin + 1
    pivo = 0

    while pos <= end:
        if array[pos] >= array[pos - 1]:
            pos = pos+1
        else:
            pivo = pos
            break
    return pivo


def pivot_aula(array, begin, end):
    begin = begin + 1
    r = end
    while (True):
        if begin > end:
            break
        if array[begin] >= array[begin - 1]:
            begin = begin + 1
        else:
            r = begin
            break

    return r


def mediana(array, begin, end):
    mid = (begin+end-1)//2
    a = array[begin]
    b = array[mid]
    c = array[end-1]

    if (a <= b <= c):
        return mid
    if (c <= b <= a):
        return mid
    if (a <= c <= b):
        return end-1
    if (b <= c <= a):
        return end-1

    return begin


def pivotChoosing(array, begin, end, method):
    try:
        if (method == 0):
            p = array[begin]
        elif (method == 1):
            p = array[mediana(array, begin, end)]
        elif (method == 2):
            p = (array[begin] + array[end] + array[(begin + end)//2]) // 3
        elif (method == 3):
            p = array[randint(begin, end)]
        elif (method == 4):
            p = array[(begin + end)//2]
        elif (method == 5):
            p = array[pivot_aula(array, begin, end)]
        else:
            raise StopIteration
    except StopIteration:
        print("Método não existe!")

    array[p], array[end] = array[end], array[p]

    return array[end]


def partition(array, begin, end, method):
    pivot = pivotChoosing(array, begin, end, method)
    i = (begin - 1)

    for j in range(begin, end):
        if (array[j] <= pivot):
            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[end] = array[end], array[i+1]

    return (i+1)


def quicksort(array, begin=0, end=None, method=3):
    if (end is None):
        end = len(array)-1
    if (begin < end):
        p = partition(array, begin, end, method)
        quicksort(array, begin, p-1, method)
        quicksort(array, p+1, end, method)
    else:
        return


for x in range(2, 3):
    lista = listCreation((10) ** (x))
    pouco = []
    for y in range(int((10 ** x) * 0.45)):
        pouco = swapPositions(lista, (10) ** (x))

    tic = time.perf_counter()
    quicksort(pouco, 0, len(pouco)-1, 0)
    print(pouco)
    toc = time.perf_counter()
    print(f"Método rodou em {toc - tic:0.8f} segundos")


    for y in range(int((10 ** x) * 0.45)):
        pouco = swapPositions(lista, (10) ** (x))
    tic = time.perf_counter()
    quicksort(pouco, 0, len(pouco)-1, 1)
    print(pouco)
    toc = time.perf_counter()
    print(f"Método rodou em {toc - tic:0.8f} segundos")


    for y in range(int((10 ** x) * 0.45)):
        pouco = swapPositions(lista, (10) ** (x))
    tic = time.perf_counter()
    quicksort(pouco, 0, len(pouco)-1, 2)
    print(pouco)
    toc = time.perf_counter()
    print(f"Método rodou em {toc - tic:0.8f} segundos")


    for y in range(int((10 ** x) * 0.45)):
        pouco = swapPositions(lista, (10) ** (x))
    tic = time.perf_counter()
    quicksort(pouco, 0, len(pouco)-1, 3)
    print(pouco)
    toc = time.perf_counter()
    print(f"Método rodou em {toc - tic:0.8f} segundos")


    for y in range(int((10 ** x) * 0.45)):
        pouco = swapPositions(lista, (10) ** (x))
    tic = time.perf_counter()
    quicksort(pouco, 0, len(pouco)-1, 4)
    print(pouco)
    toc = time.perf_counter()
    print(f"Método rodou em {toc - tic:0.8f} segundos")


    for y in range(int((10 ** x) * 0.45)):
        pouco = swapPositions(lista, (10) ** (x))
    tic = time.perf_counter()
    quicksort(pouco, 0, len(pouco)-1, 5)
    print(pouco)
    toc = time.perf_counter()
    print(f"Método rodou em {toc - tic:0.8f} segundos")
    # for y in range(int((10 ** x) * 0.25)):
    #     medio = (swapPositions(lista, (10) ** (x)))
    # for y in range(int((10 ** x) * 0.45)):
    #     muito = (swapPositions(lista, (10) ** (x)))
