import re
import io


def func(string):
    f = io.open(string, 'r', encoding="utf-8")
    mas = f.read().splitlines()
    res = []
    for i in mas:
        if re.match(r'[А-ЯA-Z][а-яa-z]+ ([А-ЯA-Z].)\1 P3112', i) is None:
            res.append(i)

    for i in res:
        print(i)
    f.close()
    print("")


func('test30.txt')
func('test31.txt')
func('test32.txt')
func('test33.txt')
func('test34.txt')

