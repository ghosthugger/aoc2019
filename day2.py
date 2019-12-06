import math

def run(program):
    memory = program
    ip = 0

    while(memory[ip] != 99):
        opcode = memory[ip]
        if(opcode == 1):
            param1 = memory[ip+1]
            param2 = memory[ip+2]
            dest = memory[ip+3]
            memory[dest] = memory[param1] + memory[param2]
            ip = ip + 4
        elif(opcode == 2):
            param1 = memory[ip+1]
            param2 = memory[ip+2]
            dest = memory[ip+3]
            memory[dest] = memory[param1] * memory[param2]
            ip = ip + 4
        else:
            print("something is wrong")

    return memory

def gravity_assist(noun, verb):
    program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0]
    program[1] = noun
    program[2] = verb

    return run(program)

def find_output(output):
    for noun in range(100):
        for verb in range(100):
            result = gravity_assist(noun, verb)
            if(result[0] == output):
                return (noun, verb)

def main():
    assert(run([1,0,0,0,99]) == [2,0,0,0,99])
    assert(run([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])

    print(gravity_assist(12,2))

    print(find_output(19690720))


if __name__ =="__main__":
    main()
