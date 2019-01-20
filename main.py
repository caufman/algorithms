import sort
from random import randint

if __name__ == '__main__':
    arr = [randint(0, 9) for i in range(10)]
    print("начальный массив:",  arr, "\n")
    print("Пузырьковая сортировка\n\t", 
        sort.bubbleSort(arr), 
        '\n')
    
    print("Сортировка вставками\n\t", 
        sort.selectionSort(arr), 
        '\n')
