def convert_input_to_list(numerical_sequence):
    my_list = []
    my_list = numerical_sequence.split(" ")
    try:
        my_list = list(map(int, my_list))
    except ValueError:
        return print('Это не числовая последовательность. Выход из программы.') and exit()
        
    return my_list

def binary_search(array, element, left, right):
    if element<array[0] or element>array[-1]:
        return "Условия не удовлетворены, число вышло за пределы списка"
    
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует
    
    middle = (right+left) // 2 # находимо середину
    if array[middle-1] < element and element <= array[middle]: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)


def sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        
    return array
    
number = int(input("Введите число:")) 
numerical_sequence = input("Введите числовую последовательность через пробел:")

numerical_sequence = convert_input_to_list(numerical_sequence)

numerical_sequence = sort(numerical_sequence)
number_position = binary_search(numerical_sequence, number,0,len(numerical_sequence))


print('Позиция числа {0} в отсортированном массиве {1}:{2}'.format(number,numerical_sequence, number_position))