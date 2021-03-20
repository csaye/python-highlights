# imports
import readchar

# initialize bytelist and pointer
bytelist = []
for i in range(0, 256):
    bytelist.append(0)
pointer = 0

# outputs byte at pointer
def output_byte():
    char = chr(bytelist[pointer])
    print(char, end = '')

# inputs byte at pointer
def input_byte():
    try:
        char = readchar.readchar()
    except:
        char = input()
        if (len(char) < 1):
            char = '\n'
        char = char[0]
    byte = ord(char)
    if (byte < 0 or byte > 255):
        byte = 0
    bytelist[pointer] = byte

# increments pointer
def increment_pointer():
    global pointer
    if (pointer == len(bytelist) - 1):
        pointer = 0
    else:
        pointer += 1

# decrements pointer
def decrement_pointer():
    global pointer
    if (pointer == 0):
        pointer = len(bytelist) - 1
    else:
        pointer -= 1

# increments byte at pointer
def increment_byte():
    if (pointer == 255):
        bytelist[pointer] = 0
    else:
        bytelist[pointer] += 1

# decrements byte at pointer
def decrement_byte():
    if (bytelist[pointer] == 0):
        bytelist[pointer] = 255
    else:
        bytelist[pointer] -= 1

# ends loop if pointer zero
def start_loop():
    global index
    if (bytelist[pointer] == 0):
        offset = -1
        while (program[index] != ']' or offset > 0):
            if (program[index] == '['):
                offset += 1
            elif (program[index] == ']'):
                offset -= 1
            index += 1

# loops if pointer nonzero
def end_loop():
    global index
    if (bytelist[pointer] != 0):
        offset = -1
        while (program[index] != '[' or offset > 0):
            if (program[index] == ']'):
                offset += 1
            elif (program[index] == '['):
                offset -= 1
            index -= 1

# get program input
program = open("./input.txt").read()
index = 0

# process commands
while (index < len(program)):
    char = program[index]
    if (char == '.'):
        output_byte()
    elif (char == ','):
        input_byte()
    elif (char == '>'):
        increment_pointer()
    elif (char == '<'):
        decrement_pointer()
    elif (char == '+'):
        increment_byte()
    elif (char == '-'):
        decrement_byte()
    elif (char == '['):
        start_loop()
    elif (char == ']'):
        end_loop()
    index += 1
