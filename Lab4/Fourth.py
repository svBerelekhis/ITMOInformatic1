import time
from json2xml import json2xml
from json2xml.utils import readfromstring

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


def pareseJSONThird(str):
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
                nJ.addJson(pareseJSONThird(str[j: i - 1]))
                mas.append(nJ)
            i += 1
        return mas
    else:
        mass = parseSimpleJSONThird(str)
        for m in mass:
            mas.append(m)
        return mas


def parseSimpleJSONThird(s):
    res = re.findall(r'"(\S+)":"([,\sА-Яа-я\d\.\-\:\)\(]+)"', s)
    mas = []
    for i in res:
        name = i[0]
        value = i[1]
        je = JSONelement(name)
        je.addStr(value)
        mas.append(je)
    return mas

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
    arr = s.split("\",")
    masstr = []
    for a in arr:
        i = 0
        while i < len(a) and a[i] != "\"":
            i += 1
        i += 1
        name = ""
        while i < len(a) and a[i] != "\"":
            name += a[i]
            i += 1
        i += 1
        while i < len(a) and a[i] != "\"":
            i += 1
        i += 1
        val = ""
        while i < len(a) and a[i] != "\"":
            val += a[i]
            i += 1
        now = JSONelement(name)
        now.addStr(val)
        masstr.append(now)
    return masstr

inputfile = open('input.json', 'r', encoding="utf-8")
file = inputfile.read()
startTime = time.time()
for i in range(10):
    mas = pareseJSON(file)
    for j in mas:
        print(j.toXML())
secondTime = time.time()
for i in range(10):
    data = readfromstring(file)
    print(json2xml.Json2xml(data).to_xml())
thirdTime = time.time()
for i in range(10):
    mas = pareseJSONThird(file)
    for j in mas:
        print(j.toXML())
fourthTime = time.time()
print("--- %s первый способ ---" % (secondTime - startTime))
print("--- %s второй способ ---" % (thirdTime - secondTime))
print("--- %s третий способ ---" % (fourthTime - thirdTime))
