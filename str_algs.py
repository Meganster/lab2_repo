str = 'Hello world'
strt = 'Bad me'

def revers_str(str):
    result = ''
    last = len(str)
    i = 0

    for ch in str:
        result = result + str[last - i - 1]
        i = i + 1
    print(result)

revers_str(str)
revers_str(strt)