# https://adventofcode.com/2019/day/5#part2

from datetime import datetime

startTime = datetime.now()

sequence = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,65,39,225,2,14,169,224,101,-2340,224,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1001,144,70,224,101,-96,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,92,65,225,1102,42,8,225,1002,61,84,224,101,-7728,224,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,1102,67,73,224,1001,224,-4891,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1102,54,12,225,102,67,114,224,101,-804,224,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,19,79,225,1101,62,26,225,101,57,139,224,1001,224,-76,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1102,60,47,225,1101,20,62,225,1101,47,44,224,1001,224,-91,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1,66,174,224,101,-70,224,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,359,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1108,226,677,224,1002,223,2,223,1005,224,389,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,419,1001,223,1,223,1008,226,677,224,102,2,223,223,1005,224,434,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,509,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,108,226,677,224,1002,223,2,223,1006,224,539,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,569,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,584,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,629,1001,223,1,223,107,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,677,224,102,2,223,223,1006,224,659,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

# couple things are changing:
# 1) opcodes + instructions + parameters are bundled in 1 integer now
# 2) the bundles are read right to left
# 3) the last two digits are the opcode (DE in ABCDE)
        # the 3 other digits are parameter modes (immediate or positional)
# 4) parameter modes means that instruction pointer pos relative to instruction set
        # pointer increases by number of values in the instruction set after the
        # instruction finishes
# 5) program outputs a diagnostic code and immediately halts when finished
# 6) a successful program execution is if all outputs were 0 except the diagnostic code
# 7) parameters that an instruction writes to will never be in immediate mode
# 8) 2 new opcodes: 3 & 4. 3 is input, 4 is output.

# TODO: figure out why one input is spitting out a 3?? 0_o

def thermal_environment_supervision_terminal(seq):

    i = 0  # starting pointer address

    # for every instruction, check the mode and update the pointer steps
    for _ in range(len(seq)+1):
        # break out the opcodes and modes
        instructions = str(seq[i])  # '1002'

        # exit conditions
        if instructions == '99':
            return "END OF THE LINE, PAL."

        # establish the opcode for the instructions
        opcode = instructions[-1:]

        # parse out instruction sets to handle instruction modes
        if opcode == '1' or opcode == '2':
            instructions = instructions.zfill(5) # '01002
            m1 = int(instructions[2])  # 0 -- positional
            m2 = int(instructions[1])  # 1 -- immediate
            m3 = int(instructions[0])  # 0 -- positional
            num1 = seq[seq[i+1]] if m1 == 0 else seq[i+1]  # doesn't handle errors in arguments (no 1 check)
            num2 = seq[seq[i+2]] if m2 == 0 else seq[i+2]  # doesn't handle errors in arguments (no 1 check)
            # print(f"pos={i} instruction={instructions} opcode={opcode} m1={m1} m2={m2} m3={m3} num1={num1} num2={num2}")  # DEBUG

        # opcode: addition
        if opcode == '1':
            # print(f"opcode=1 pos={i} instruction={instructions} {seq[seq[i+3]]} = {num1} + {num2}")
            seq[seq[i+3]] = num1 + num2
            i += 4

        # opcode: multiplication
        elif opcode == '2':
            # print(f"opcode=1 pos={i} instruction={instructions} {seq[seq[i+3]]} = {num1} * {num2}")
            seq[seq[i+3]] = num1 * num2
            i += 4

        # store user input at parameter address
        elif opcode == '3':
            # print("opcode 3 detected")
            user_input = input("what is the input? ")
            p1 = int(seq[i+1])
            seq[p1] = int(user_input)
            # print(f"opcode=3 {seq[:10]} // inserting {user_input} at location {p1}")
            i += 2

        # elif 4, do 4 things
        elif opcode == '4':
            # print("opcode 4 detected")
            p1 = seq[i+1]
            # print(f"opcode=4 {seq[:10]}")
            print(f"OUTPUT: {seq[p1]}")
            i += 2
        else:
            print(seq)
            return f"YA DUN FUCKD UP!! ERROR @ {i} => {seq[i]}"

# print(thermal_environment_supervision_terminal([1002,4,3,4,33])) # test => [1002, 4, 3, 4, 99]
# print(thermal_environment_supervision_terminal([1101,100,-1,4,0])) # test => [1101, 100, -1, 4, 99]
# print(thermal_environment_supervision_terminal([1,4,3,5,33,0,0,0,4,0,0,0,99])) # test = 33+4 => 37@i=33
# print(thermal_environment_supervision_terminal([1,4,3,5,33,0,0,0,4,0,0,0,99])) # test = 33+4 => 37@i=33
# print(thermal_environment_supervision_terminal([1,4,3,5,33,0,0,0,4,0,0,0,99])) # test = 33+4 => 37@i=33
# print(thermal_environment_supervision_terminal([1,9,10,3,2,3,11,0,99,30,40,50])) # 3500
print(thermal_environment_supervision_terminal(sequence)) # the full test

print(f"Run time: {datetime.now() - startTime}")
