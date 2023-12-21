import time
from random import seed, randint
import matplotlib.pyplot as plt
import copy
# seed random number generator

# generate some random numbers

def quickSelect(L, k):
   smallerList = []
   largerList=[]
   if len(L) != 0:
      pivot = L[(len(L)//2)]

   for i in L:
        if i<pivot:
           smallerList.append(i)

   for i in L:
        if i>pivot:
           largerList.append(i)
   m=len(smallerList)
   count=len(L)-len(smallerList)-len(largerList)
   if k >= m and k < m + count:
       return pivot
   elif m > k:
        return quickSelect(smallerList, k)
   else:
       return quickSelect(largerList, k - m - count)


def listCreation(size, percentage):
    values = list(range(size))
    array = copy.deepcopy(values)

    for _ in range(int(size * percentage)):
        array = swapPositions(array, size)

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
        elif (method == 6):
            p = int(quickSelect(array, len(array)//2))
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
    trials = 10

    for _ in range(trials):
        temp_array = copy.copy(array)
        tic = time.perf_counter_ns()
        quicksort(temp_array, 0, len(temp_array)-1, method)
        toc = time.perf_counter_ns()
        totalTime += toc - tic

    return totalTime / trials / 1e9
   


porcentagens = [0.05, 0.25, 0.45]

def getMethodName(method):
    methodNames = {
        0: "Pivô primeira posição",
        1: "Pivô mediana da lista",
        2: "Pivô média",
        3: "Pivô randômico",
        4: "Pivô posição central",
        5: "Pivô acha Pivô",
        6: "Pivô mediana dos elementos",
    }
    return methodNames.get(method, "Método não definido")

for porcent in porcentagens:

    results = [[], [], [], [], [], []]

    for x in range(2,8):
        lista = listCreation(10**x, porcent)
        
        print(f"------------------------------------------------------------------------")
        print(f"-------------Realizando operacoes com percentual de {porcent*100}%---------------")
        print(f"Lista de tamanho 10^{x}")

        for method in range(6):
            method_name = getMethodName(method)
            results[method].append(runQuicksort(method, lista))
            print(f"Executando Quicksort com método {method_name}...")
            print(f"Tempo médio de execução: {results[method][-1]:0.8f} segundos\n")

        print("\n\n")

    # Gráficos para cada cenário de desordem
    sizes = [10**i for i in range(2,8)]
    for i, array in enumerate(results, start=1):
        formatted_array = [float(val) for val in array]
        plt.figure(figsize=(8, 6))
        plt.plot(sizes, formatted_array[:len(sizes)], marker='o', linestyle='-', label=f'{getMethodName(i-1)}')
        plt.title(f'Cenário de Desordem {int(porcent*100)}% - Relação entre tamanho dos arrays e tempo de execução')
        plt.xlabel('Tamanho')
        plt.ylabel('Tempo de execução')
        plt.xscale('log')
        plt.legend()
        plt.grid(True)
        plt.savefig(f"Cenario_{int(porcent*100)}_{getMethodName(i-1).replace(' ', '_')}.png")