#!/usr/bin/env python3

import sys

def tag(tag: str, text: str):
    return "<" + tag + ">" + text + "</" + tag + ">"

def getfile(name: str):
    f = open(name, "r")
    t = f.read()
    f.close()
    return t

def putfile(name: str, txt):
    f = open(name, "w")
    f.write(txt)
    f.close()

def split(csv):
    cnt = 0
    delim = "__$COMMA$_$SPECIAL$_$DELIMETER$"
    i = 0
    while i < len(csv):
        if csv[i] == '"':
            if i == 0 or csv[i - 1] != '"':
                cnt += 1
        elif csv[i] in [',', ';'] and cnt % 2 == 0:
            now = csv.index(',', i)
            csv = csv[:now] + delim + csv[now + 1:]
            i += len(delim)
        i += 1
    return csv.split(delim)

def parse(s):
    items = split(s)
    return "".join(list(map(lambda x: tag("td", x), items)))

def main(argv):
    if len(argv) != 1:
        print("No argument.")
        return -1
    name = argv[0]
    if argv[name.find(".", -1):] != ".csv":
        print("Not a CSV file.")
        return -2
    csv = getfile(argv).split("\n")
    result = "<table border=1>"
    for s in csv:
        result += "<tr>" + parse(s) + "</tr>"
    result += "</table>"
    putfile(name + ".html", result)
    return 0

if __name__ = "__main__":
    exit(main(sys.argv))
