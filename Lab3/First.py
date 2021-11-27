import re
import io


def funk(string):
    f = io.open(string, 'r', encoding='utf-8')
    print(len(re.findall(r'=<\{\(', f.read())))
    f.close()
    return 0


funk('test10.txt')
funk('test11.txt')
funk('test12.txt')
funk('test13.txt')
funk('test14.txt')




