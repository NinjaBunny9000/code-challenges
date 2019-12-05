# https://adventofcode.com/2019/day/2

from datetime import datetime

startTime = datetime.now()

# PROBLEM BREAKDOWN
# valid opcodes are 1, 2, 99
# 99: program is finished and should immediatley halt
# 1:  adds together numbers read from two pos and stores result in third pos
    # three integers after opcode are the 3 positions
# 2:  works like 1, except multiplies the two inputs
# ?:  error

# NOTE: the three integers indicates WHERE the inputs and outputs are (indexes) not their values

# determine what pair of inputs produces the output 19690720
# affect address 1 & 2
    # 1 is called noun, 2 is called verb
    # values will be between 0 and 99
# reset the values before each input you try

def intcode_processor(seq, magic_number):
    seq_reset = seq[:]
    noun = 1
    verb = 2
    word_range = 99
    for n in range(word_range + 1):
        for v in range(word_range + 1):
            seq = seq_reset[:]
            seq[noun] = n
            seq[verb] = v
            i = 0
            for _ in range(len(seq)+1):
                if seq[i] == 1:
                    seq[seq[i+3]] = seq[seq[i+1]] + seq[seq[i+2]]
                elif seq[i] == 2:
                    seq[seq[i+3]] = seq[seq[i+1]] * seq[seq[i+2]]
                elif seq[i] == 99:
                    if seq[0] == magic_number:
                        print(f"MATCH FOUND: n={n} v={v}")
                        return(f"ANSWER: {100*n+v}")
                else:
                    break
                i += 4

seq = [
    1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,1,23,13,27,2,
    6,27,31,1,5,31,35,2,10,35,39,1,6,39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,
    6,59,2,59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,1,79,5,83,2,10,
    83,87,1,87,6,91,2,9,91,95,1,95,5,99,1,5,99,103,1,103,10,107,1,9,107,111,1,
    6,111,115,1,115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,131,2,135,1,
    10,135,0,99,2,0,14,0
    ]


# the full test
print(intcode_processor(seq, 19690720))

print(f"Run time: {datetime.now() - startTime}")