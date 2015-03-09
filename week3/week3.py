#!/usr/bin/env python

__author__ = "Sallyxdz"

import re
import itertools
from collections import Counter
from math import factorial

'''
This function reads the text files and output sequences without
non-alphabetical characters.
'''
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

'''
This function checks whether the parentheses are balanced.
'''
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

'''
This function checks whether the sequence is a subsequence of
a set of sequences based on the min support value.
'''
def frequent_sequences(q_elems, a, min_sup):
    if min_sup > len(q_elems):
        return False
    # if type(a) is list:
    #         print " ".join(a) + " " + "is subsequence of: "
    # else:
    #         print a + " " + "is subsequence of: "
    index = []
    for i in range(len(q_elems)):
        q = q_elems[i]
        if is_sub_sequence(q, a):
            index.append(str(i+1))
            min_sup -= 1
            # early return until reaches min_sup
            # if min_sup <= 0:
            #     return True
    print " ".join(index)

    # run through all q_elems
    if min_sup <= 0:
        return True
    return False

'''
This is the core function for checking subsequences.
'''
def is_sub_sequence(q, a):

    i, j, match = [0]*3

    while i < len(a) and j < len(q):
        len_a = len(a[i])
        len_q = len(q[j])
        if len_a < len_q:
            combs = []
            for c in itertools.combinations(q[j],len_a):
                combs.append("".join(c))
            if a[i] in combs:
                match += 1
                i += 1
        elif a[i] == q[j]:
            match += 1
            i += 1
        j += 1
        continue

    if match == len(a):
        return True
    else:
        return False

'''
Helper function for Problem 2 and 3
Return a list containing all unique letters and a dictionary of letters as keys and values as counts using Apriori pruning.
'''
def make_dict(seqs, min_sup):
    gsp_freqs = Counter()
    all_seq = ""
    for each_seq in seqs:
        seq = "".join(each_seq)
        gsp_freqs += Counter(set(seq))
        all_seq += seq

    all_values = set(all_seq)
    # Filter the dictionary by min support
    # Apriori pruning
    gsp_freqs = { k:v for k, v in gsp_freqs.iteritems() if v >= min_sup }

    return [all_values, gsp_freqs]

'''
Helper function for Problem 2
Modified function for calculating candidate sequence number
'''

def cand_seq_num(n, r):
    num = factorial(n)
    denom = factorial(r) * factorial(n - r)
    return str(n * n + num / denom)

'''
Main function for Problem 1
'''
def problem_1(Q_FILENAME, A_FILENAME, min_sup):
    q_seqs = readfile(Q_FILENAME)
    a_seqs = readfile(A_FILENAME)

    if not q_seqs or not a_seqs:
        return False

    for a in a_seqs:
        result = frequent_sequences(q_seqs, a, min_sup)

        print " ".join(a) + " => " + str(result)

'''
Main function for Problem 2
'''
def problem_2(Q_FILENAME, min_sup, length=2):
    q_seqs = readfile(Q_FILENAME)
    if not q_seqs:
        return False

    # print q_seqs
    [all_values, gsp_freqs] = make_dict(q_seqs, min_sup)
    all_values_pruning = gsp_freqs.keys()
    len_all = len(all_values)
    len_pruning = len(all_values_pruning)
    print cand_seq_num(len_pruning, length) + "; " + \
                cand_seq_num(len_all, length)

'''
Main function for Problem 3
'''
def problem_3(Q_FILENAME, min_sup, length=2):
    q_seqs = readfile(Q_FILENAME)
    if not q_seqs:
        return False

    [all_values, gsp_freqs] = make_dict(q_seqs, min_sup)
    all_values_pruning = gsp_freqs.keys()
    print "Frequent items: " + str(all_values_pruning)
    freq_terms = []
    for c in list(itertools.combinations(all_values_pruning, length)):
        freq_terms.append(["".join(c)])
    for p in list(itertools.permutations(all_values_pruning, length)):
        freq_terms.append(list(p))
    for a in all_values_pruning:
        freq_terms.append(list(a*length))
    print "Candidate sequences: " + str(freq_terms)
    for f in freq_terms:
        result = frequent_sequences(q_seqs, f, min_sup)
        # only print True results
        if result:
            if type(f) is list:
                print " ".join(f) + " => " + str(result)
            else:
                print f + " => " + str(result)

'''
Main function for Problem 4
'''
def problem_4(Q_FILENAME, projected):
    with open(Q_FILENAME, 'r') as f:
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
                # print each_line
                projected_index = []
                braces_dict = { "(":[], ")":[] }
                for i in range(len(each_line)):
                    if each_line[i] == projected:
                        projected_index.append(i)
                    elif each_line[i] in braces_dict:
                        braces = each_line[i]
                        braces_dict[braces].append(i)
                if len(projected_index) == 0:
                    print each_line + ": " + "No <" + projected + ">-projected database."
                    continue

                first_position = projected_index[0]
                # print first_position
                zipped = zip(braces_dict.values()[0], braces_dict.values()[1])
                # print zipped
                # print braces_dict
                inside = False
                underscore = False
                for z in zipped:
                    if min(z) < first_position < max(z):
                        inside = True
                        if first_position + 1 != max(z):
                            underscore = True
                # print inside
                # print underscore

                result = each_line[first_position:]
                if inside and underscore:
                    result = result.replace(projected, "_", 1)
                    result = "(" + result
                elif inside:
                    result = result[2:]
                else:
                    result = result[1:]
                print each_line + ": <" + result

if __name__ == '__main__':

    print "------------Problem 1-------------"
    Q_FILENAME = "data/q1_Q.txt"
    A_FILENAME = "data/q1_A.txt"
    min_sup = 3
    problem_1(Q_FILENAME, A_FILENAME, min_sup)

    """
    # Another dataset for testing
    print "-----------------------------"
    Q_FILENAME = "data/q11_Q.txt"
    A_FILENAME = "data/q11_A.txt"
    min_sup = 3
    problem_1(Q_FILENAME, A_FILENAME, min_sup)
    """

    print "------------Problem 2-------------"
    Q_FILENAME = "data/q2_Q.txt"
    min_sup = 3
    problem_2(Q_FILENAME, min_sup)

    print "------------Problem 3-------------"
    Q_FILENAME = "data/q31_Q.txt"
    min_sup = 4
    problem_3(Q_FILENAME, min_sup)

    """
    # Another dataset for testing
    Q_FILENAME = "data/q3_Q.txt"
    min_sup = 4
    problem_3(Q_FILENAME, min_sup)
    """

    print "------------Problem 4-------------"
    Q_FILENAME = "data/q4_Q.txt"
    projected = "e"
    problem_4(Q_FILENAME, projected)

    """
    # Another dataset for testing
    print "------------Problem 4-------------"
    Q_FILENAME = "data/q41_Q.txt"
    projected = "a"
    problem_4(Q_FILENAME, projected)
    """
