import re
class JSONelement:
    inp = []
    flag = 0

    def __int__(self):
        self.name = ""

    def __init__(self, name):
        self.intStr = ""
        self.name = name

    def addJson(self, Json):
        self.flag = 1
        self.inp = Json

    def addStr(self, str):
        self.str = str
        self.flag = 0

    def toXML(self):
        res = ""
        res += "<" + self.name + ">"
        if self.flag == 0:
            res += self.str
        else:
            for Json in self.inp:
                res += Json.toXML()
        if self.name != "":
            res += "</" + self.name + ">"
        return res

    def toYMI(self, count):
        res = ""
        res += " "*count + self.name + ":\n"
        if self.flag == 0:
            res += " "*(count + 1) + self.str
        else:
            for Json in self.inp:
                res += Json.toYMI(count + 1)
        res += "\n"
        return res

def pareseJSON(str):
    mas = []
    if "{" in str or "}" is str:
        i = 0
        while i < len(str):
            if str[i] == "{" and i > 0 and str[i - 1] == ":":
                otk = 0
                j = i + 1
                otk += 1
                i += 1
                h = i - 3
                t = 0
                name = ""
                while h >= 0 and t < 2:
                    if str[h] == "\"":
                        t += 1
                    else:
                        name = str[h] + name
                    h -= 1
                while i < len(str) and otk > 0:
                    if str[i] == "{":
                        otk += 1
                    if str[i] == "}":
                        otk -= 1
                    i += 1
                nJ = JSONelement(name)
                nJ.addJson(pareseJSON(str[j: i - 1]))
                mas.append(nJ)
            i += 1
        return mas
    else:
        mass = parseSimpleJSON(str)
        for m in mass:
            mas.append(m)
        return mas


def parseSimpleJSON(s):
    res = re.findall(r'"(\S+)":"([,\sА-Яа-я\d\.\-\:\)\(]+)"', s)
    mas = []
    for i in res:
        name = i[0]
        value = i[1]
        je = JSONelement(name)
        je.addStr(value)
        mas.append(je)
    return mas


inputfile = open('input.json', 'r', encoding="utf-8")
file = inputfile.read()
mas = pareseJSON(file)
for i in mas:
    print(i.toXML())