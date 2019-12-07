import math
def parameter_mode(opcode, param_position):
    opcode_parameter_mode_position = 5-(param_position+2)
    if '{:5d}'.format(opcode)[opcode_parameter_mode_position] == '1':
        return 1
    return 0

def instruction(opcode):
    instr = '{:5d}'.format(opcode)[-2:]
    res = int(instr)
    return res

def resolve_param(n, param, opcode, memory):
    if parameter_mode(opcode, n) == 0:
        return memory[param]
    if parameter_mode(opcode, n) == 1:
        return param

def run(program):
    memory = program
    ip = 0

    while(instruction(memory[ip]) != 99):
        opcode = memory[ip]
        if(instruction(opcode) == 1): # add
            param1 = memory[ip+1]
            param2 = memory[ip+2]
            dest = memory[ip+3]
            memory[dest] = resolve_param(1, param1, opcode, memory) + resolve_param(2, param2, opcode, memory)
            ip = ip + 4
        elif(instruction(opcode) == 2): # mul
            param1 = memory[ip+1]
            param2 = memory[ip+2]
            dest = memory[ip+3]
            memory[dest] = resolve_param(1, param1, opcode, memory) * resolve_param(2, param2, opcode, memory)
            ip = ip + 4
        elif(instruction(opcode) == 3): # input
            dest = memory[ip+1]
            try:
                value=int(input('Input:'))
            except ValueError:
                print("Not a number")
            memory[dest] = value
            ip = ip + 2
        elif(instruction(opcode) == 4): # output
            param = memory[ip+1]
            print(resolve_param(1, param, opcode, memory))
            ip = ip + 2
        elif(instruction(opcode) == 5): # jump-if-true
            param1 = memory[ip+1]
            param2 = memory[ip+2]
            ip = ip + 3
            if resolve_param(1, param1, opcode, memory) != 0:
                ip = resolve_param(2, param2, opcode, memory)
        elif(instruction(opcode) == 6): # jump-if-false
            param1 = memory[ip+1]
            param2 = memory[ip+2]
            ip = ip + 3
            if resolve_param(1, param1, opcode, memory) == 0:
                ip = resolve_param(2, param2, opcode, memory)
        elif(instruction(opcode) == 7): # less-than
            param1 = memory[ip+1]
            param2 = memory[ip+2]
            dest = memory[ip+3]
            memory[dest] = 1 if resolve_param(1, param1, opcode, memory) < resolve_param(2, param2, opcode, memory) else 0
            ip = ip + 4
        elif(instruction(opcode) == 8): # greater-than
            param1 = memory[ip+1]
            param2 = memory[ip+2]
            dest = memory[ip+3]
            memory[dest] = 1 if resolve_param(1, param1, opcode, memory) == resolve_param(2, param2, opcode, memory) else 0
            ip = ip + 4
        else:
            print("something is wrong")


    return memory

def main():

#    print(run([3,9,8,9,10,9,4,9,99,-1,8])) # test equals
#    print(run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])) #1 test jump

#    program = [1101,100,-1,4,0]
    program = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,82,10,225,101,94,44,224,101,-165,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,35,77,225,1102,28,71,225,1102,16,36,225,102,51,196,224,101,-3468,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1001,48,21,224,101,-57,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,2,188,40,224,1001,224,-5390,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,9,32,224,101,-41,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1102,66,70,225,1002,191,28,224,101,-868,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1,14,140,224,101,-80,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1102,79,70,225,1101,31,65,225,1101,11,68,225,1102,20,32,224,101,-640,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,226,224,1002,223,2,223,1006,224,329,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,359,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,374,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1006,224,404,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,419,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,7,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,464,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,509,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,644,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]

    print(run(program))

if __name__ =="__main__":
    main()
