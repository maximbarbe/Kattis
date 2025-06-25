import sys
from collections import deque
lines = sys.stdin.readlines()
kept = []
for i in range(len(lines)):
    cur = lines[i]
    chars = []
    for c in cur:
        if c in "<>+-.[]":
            chars.append(c)
    if chars != []:
        kept.append("".join(chars))
program = "".join(kept)

stack = []
brackets = dict()
for i, c in enumerate(program):
    if c == "[":
        stack.append(i)
    elif c == "]":
        brackets[i] = stack[-1]
        brackets[stack[-1]] = i
        stack.pop()
        
memory = deque([0])
mem_idx = 0
MOD = 2**8
idx = 0
while idx != len(program):
    match program[idx]:
        case ">":
            mem_idx += 1
            if mem_idx == len(memory):
                memory.append(0)
            idx += 1
        case "<":
            if mem_idx != 0:
                mem_idx -= 1
            else:
                memory.appendleft(0)
            idx += 1
        case "+":
            memory[mem_idx] = (memory[mem_idx] + 1)%MOD
            idx += 1
        case "-":
            memory[mem_idx] = (memory[mem_idx] - 1)%MOD
            idx += 1
        case ".":
            print(chr(memory[mem_idx]), end="")
            idx += 1
        case "[":
            if memory[mem_idx] == 0:
                idx = brackets[idx] + 1
            else:
                idx += 1
        case "]":
            if memory[mem_idx] != 0:
                idx = brackets[idx]
            else:
                idx += 1