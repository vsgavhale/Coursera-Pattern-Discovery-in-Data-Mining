#!/usr/bin/env python

__author__      = "Sallyxdz"

import re
import itertools
from collections import Counter


def readfile(FILENAME):
    with open(FILENAME, 'r') as f:
        seqs = []
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
                line_result = [] # single sequence
                elem = ""
                inside = False # inside a pair of parentheses
                for char in each_line:
                    if not char.isalpha():
                        if len(elem) > 0:
                            # make sure it is sorted alphabetically
                            # inside the parentheses
                            elem = ''.join(sorted(elem))
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
                    seqs.append(line_result)
        return seqs


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

def make_dict(seqs):
    result = ""
    for each_seq in seqs:
        seq = "".join(each_seq)
        result += seq

    #freqs = Counter(result)
    #print freqs


def frequent_sequences(q_elems, a, min_sup):
    if min_sup > len(q_elems):
        return False
    print " ".join(a) + " " + "is subsequence of: "
    for i in range(len(q_elems)):
        q = q_elems[i]
        if is_sub_sequence(q, a):
            print  i+1
            min_sup -= 1
            # early return until reaches min_sup
            # if min_sup <= 0:
            #     return True

    # run through all q_elems
    if min_sup <= 0:
        return True
    return False

'''
Core function for checking subsequences
'''
def is_sub_sequence(q, a):

    i, j, match = [0]*3
    while i < len(a) and j < len(q):
        len_a = len(a[i])
        len_q = len(q[j])
        if len_a > len_q:
            j += 1
            continue
        elif len_a == len_q:
            if a[i] == q[j]:
                match += 1
                i += 1
                j += 1
                continue
            else:
                j += 1
                continue
        else: # len_a < len_q
            combs = []
            for c in itertools.combinations(q[j],len_a):
                combs.append("".join(c))
            if a[i] in combs:
                match += 1
                i += 1
                j += 1
                continue
            else:
                j += 1
                continue

    if match == len(a):
        return True
    else:
        return False



'''
Main function
'''
def main(Q_FILENAME, A_FILENAME, min_sup):
    q_seqs = readfile(Q_FILENAME)
    # print q_seqs
    # make_dict(q_seqs)

    a_seqs = readfile(A_FILENAME)
    # print a_seqs

    for a in a_seqs:
        result = frequent_sequences(q_seqs, a, min_sup)
        print " ".join(a) + " => " + str(result)


if __name__ == '__main__':
    Q_FILENAME = "q1_Q.txt"
    A_FILENAME = "q1_A.txt"
    min_sup = 3
    main(Q_FILENAME, A_FILENAME, min_sup)

    Q_FILENAME = "q11_Q.txt"
    A_FILENAME = "q11_A.txt"
    min_sup = 3
    main(Q_FILENAME, A_FILENAME, min_sup)






