#!/usr/bin/env python

__author__      = "Sallyxdz"

import re

def readfile(FILENAME):
    with open(FILENAME, 'r') as f:
        elems = []
        lines = f.readlines()
        for each_line in lines:
            each_line = each_line.strip()
            each_line = each_line.lower()
            each_line = re.sub("[^a-z|\(|\)|\<|\>]+", \
                        "", each_line)
            if not is_valid(each_line):
                print "Parentheses don't match! Check input file."
                return False
            else:
                # print "Success"
                line_result = []
                elem = ""
                inside = False
                for char in each_line:
                    if not char.isalpha():
                        if len(elem) > 0:
                            line_result.append(elem)
                        elem = ""
                        if char == "(":
                            inside = True
                        elif char == ")":
                            inside = False

                    else:
                        if not inside and len(elem) > 0:
                            line_result.append(elem)
                            elem = ""
                        elem += char
                if len(line_result) > 0:
                    elems.append(line_result)
        return elems


def is_valid(str):
    stack = []
    matching = { "<":">", "(":")" } #  "[":"]", "{":"}" }
    for char in str:
        if char in matching:
            stack.append(char)
        elif char in matching.values():
            if len(stack) == 0 or char != matching[stack.pop()]:
                return False
        else:
            pass
    return len(stack) == 0

if __name__ == '__main__':
    Q_FILENAME = "q1_Q.txt"
    q_elems = readfile(Q_FILENAME)
    print q_elems
    A_FILENAME = "q1_A.txt"
    a_elems = readfile(A_FILENAME)
    print a_elems


































