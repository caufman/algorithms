import sort
from random import randint

if __name__ == '__main__':
    print("Пузырьковая сортировка\n\t", 
        sort.bubbleSort([randint(0, 9) for i in range(10)]), 
        '\n')
