

class ListDivideException(Exception):
    pass


def list_divide(numbers: list, divide: int = 2):
    try:
        num_divisible = 0
        for num in numbers:
            if num % divide == 0:
                num_divisible += 1

        return num_divisible
    except Exception:
        raise ListDivideException


def test_list_divide():
    try:
        print(list_divide([1, 2, 3, 4, 5]))
        print(list_divide([2, 4, 6, 8, 10]))
        print(list_divide([30, 54, 63, 98, 100], divide=10))
        print(list_divide([]))
        print(list_divide([1, 2, 3, 4, 5], 1))
    except ListDivideException:
        print("Error occurred!")


if __name__ == "__main__":
    test_list_divide()
