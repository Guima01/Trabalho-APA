import time
from random import seed, randint
import matplotlib.pyplot as plt
import copy
# seed random number generator

# generate some random numbers

def listCreation(size):
    values = []
    for i in range(size):
        values.append(i)

    array = []
    for iteration in range (1, 11):
       for y in range(int((10 ** x) * 0.45)):
           array = swapPositions(values, (10) ** (x))

    return array

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
    

def runQuicksort(method, array):

    totalTime = 0

    tic = time.perf_counter_ns()
    quicksort(array, 0, len(array)-1, method)
    toc = time.perf_counter_ns()
    
    totalTime += toc - tic

    return (totalTime / 10) / 1e9
   
results = [[], [], [], [], [], []]

for x in range(2, 8):
   lista = listCreation((10) ** (x))
   
   print(f"Lista de tamanho 10^{x}")

   
   results[0].append(runQuicksort(0, copy.copy(lista)))
   print("Executando Quicksort com pivô fixo na primeira posição da lista...")
   print(f"Tempo de médio de execução: {results[0][-1]:0.8f} segundos\n")
   
   results[1].append(runQuicksort(1, copy.copy(lista)))
   print("Executando Quicksort com pivô fixo na posição central da lista...")
   print(f"Tempo de médio de execução: {results[1][-1]:0.8f} segundos\n")

   
   results[2].append(runQuicksort(2, copy.copy(lista)))
   print("Executando Quicksort com pivô média do primeiro, central e ultimo valor da lista...")
   print(f"Tempo de médio de execução: {results[2][-1]:0.8f} segundos\n")
   
   results[3].append(runQuicksort(3, copy.copy(lista)))
   print("Executando Quicksort com pivô randômico...")
   print(f"Tempo de médio de execução: {results[3][-1]:0.8f} segundos\n")
   
   results[4].append(runQuicksort(4, copy.copy(lista)))
   print("Executando Quicksort com pivô mediana...")
   print(f"Tempo de médio de execução: {results[4][-1]:0.8f} segundos\n")
   
   results[5].append(runQuicksort(5, copy.copy(lista)))
   print("Executando Quicksort com procedimento Acha Pivô...")
   print(f"Tempo de médio de execução: {results[5][-1]:0.8f} segundos\n\n\n")
   
   
print(results)


sizes = [10**i for i in range(2, 8)]
# Iterando pelos arrays internos para criar os gráficos
for i, array in enumerate(results, start=1):
    formatted_array = [float(val) for val in array]  # Convertendo para float
    
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, formatted_array, marker='o', linestyle='-', label=f'Array {i}')
    plt.title(f'Array {i} - Relação entre tamanho dos arrays e tempo de execução')
    plt.xlabel('Tamanho (log10)')
    plt.ylabel('Tempo de execução')
    plt.xscale('log')  # Usar escala logarítmica para o eixo x
    plt.legend()
    plt.grid(True)
    plt.savefig("QuicksortMethod" + str(i))
