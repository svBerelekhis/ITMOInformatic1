import re
import io


def funk(string):
    f = io.open(string, 'r', encoding="utf-8")
    result = re.findall(r'(\b[А-ЯA-Z][а-яa-z]*)(\s[А-ЯA-Z].\n?[А-ЯA-Z].)', f.read())
    for i in result:
        print(i[0])
    f.close()
    print(' ')


funk('test20.txt')
funk('test21.txt')
funk('test22.txt')
funk('test23.txt')
funk('test24.txt')
