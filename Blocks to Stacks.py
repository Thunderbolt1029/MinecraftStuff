import math

while True:
    block = int(input("How many blocks? "))
    stacks = block/64
    stacks = math.floor(stacks)
    leftoverBlocks = block%64
    
    if stacks==0:
        print (str(leftoverBlocks) + " blocks")
    else:
        print(str(stacks) + " stacks and " + str(leftoverBlocks) + " blocks")

    input()
