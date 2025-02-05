#!/usr/bin/env python3
import sys

file = open(sys.argv[1])
content1 = file.read()

sequences = []

split = content1.split(">")[1:]
for i in split:
    remove_name = i.split("]")
    temp = remove_name[-1]
    replace_enter = temp.replace("\n", "")
    sequences.append(replace_enter)

seq1 = sequences[1]
seq2 = sequences[0]

pipes = ""
i = 0
while i < len(seq1):
    if seq1[i] == seq2[i]:
        pipes += '|'
    else:
        pipes += ' '
    i += 1

print(sequences[0])
print(pipes)
print(sequences[1])
