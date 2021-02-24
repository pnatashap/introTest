def transform(num):
    if not (isinstance(num, int)):
        return num

    d3 = num % 3
    d5 = num % 5
    if d3 == 0 and d5 == 0:
        return "Testing"
    if d3 == 0:
        return "Software"
    if d5 == 0:
        return "Agile"
    return num


def transform_list(max):
    for i in range(max, 0, -1):
        print(transform(i))


def test_three():
    assert transform(3) == "Software"


def test_five():
    assert transform(5) == "Agile"


def test_three_five():
    assert transform(30) == "Testing"


def test_none():
    assert transform(1) == 1


if __name__ == '__main__':
    transform_list(100)
