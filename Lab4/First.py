import string


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

    def addNum(self, i):
        self.i = i
        self.flag = 2

    def toXML(self):
        res = ""
        res += "<" + self.name + ">"
        if self.flag == 0:
            res += self.str
        elif self.flag == 1:
            for Json in self.inp:
                res += Json.toXML()
        else:
            res += self.i
        if self.name != "":
            res += "</" + self.name + ">"
        return res

    def toYMI(self, count):
        res = ""
        if self.flag == 0:
            res += " " * count + self.name + ": "
            res += self.str
        elif self.flag == 1:
            res += " " * count + self.name + ":\n"
            for Json in self.inp:
                res += Json.toYMI(count + 1)
        else:
            res += " " * count + self.name + ": "
            res += self.i
        res += "\n"
        return res

def pareseJSON(str):
    mas = []
    i = 0
    isInQ = False
    while i < len(str):
        if str[i] == "\"":
            if isInQ:
                isInQ = False
            else:
                isInQ = True
        if not isInQ and str[i] == ":" and i > 0 and str[i - 1] == "\"":
            i += 1
            h = i - 2
            t = 0
            name = ""
            while h >= 0 and t < 2:
                if str[h] == "\"":
                    t += 1
                else:
                    name = str[h] + name
                h -= 1
            nJ = JSONelement(name)
            if str[i] == "{":
                otk = 0
                j = i + 1
                otk += 1
                i += 1
                while i < len(str) and otk > 0:
                    if str[i] == "\"":
                        if isInQ:
                            isInQ = False
                        else:
                            isInQ = True
                    if not isInQ and str[i] == "{":
                        otk += 1
                    if not isInQ and str[i] == "}":
                        otk -= 1
                    i += 1
                nJ.addJson(pareseJSON(str[j: i - 1]))

            else:
                j = i + 1
                isItInMas = False
                while i < len(str) and (str[i] != "}" or isInQ) and (str[i] != "," or isInQ or isItInMas):
                    if str[i] == "\"":
                        if isInQ:
                            isInQ = False
                        else:
                            isInQ = True
                    if not isInQ and str[i] == "[":
                        isItInMas = True
                    if not isInQ and str[i] == "]":
                        break
                    i += 1
                if isItInMas:
                    i += 2
                e = str[j: i - 1]
                nJ.addStr(e)
            mas.append(nJ)
        i += 1
    return mas


inputfile = open('input.json', 'r', encoding="utf-8")
file = inputfile.read()
mas = pareseJSON(file)
for i in mas:
    print(i.toYMI(0))
