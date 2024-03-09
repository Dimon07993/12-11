from utils import arrs


def test_get():

    array = [1, 2, 3, 4, 5]

    # Проверяем извлечение элемента по существующему индексу
    assert arrs.get(array, 2) == 3, "Should be 3"

    # Проверяем извлечение элемента по несуществующему индексу с указанием значения по умолчанию
    assert arrs.get(array, 10, "Not found") == "Not found", "Should be 'Not found'"

    # Проверяем извлечение элемента по несуществующему индексу без указания значения по умолчанию
    assert arrs.get(array, 10) == None, "Should be None"








def test_slice():
    array = [1, 2, 3, 4, 5]

    # Проверяем извлечение части массива без указания start и end
    assert arrs.my_slice(array) == [1, 2, 3, 4, 5], "Should be [1, 2, 3, 4, 5]"

    # Проверяем извлечение части массива с указанием start
    assert arrs.my_slice(array, 2) == [3, 4, 5], "Should be [3, 4, 5]"

    # Проверяем извлечение части массива с указанием start и end
    assert arrs.my_slice(array, 1, 4) == [2, 3, 4], "Should be [2, 3, 4]"

    # Проверяем извлечение части массива с отрицательными индексами
    assert arrs.my_slice(array, -3, -1) == [3, 4], "Should be [3, 4]"

    # Проверяем извлечение части массива с отрицательным end
    assert arrs.my_slice(array, 1, -1) == [2, 3, 4], "Should be [2, 3, 4]"

    # Проверяем извлечение части пустого массива
    assert arrs.my_slice([], 1, 4) == [], "Should be []"





