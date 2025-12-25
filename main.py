print('hello world')

def feature(data: list[str]) -> str:
    result = ''
    for s in data:
        result += s

    return result

def another_1():
    feature([])


def another_2():
    feature(['', '', ''])