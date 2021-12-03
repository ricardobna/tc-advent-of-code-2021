#gets depth information from input file
input = open('input', 'r')
depths = input.readlines()

increases = 1 # first depth is bigger than what you started at so it starts with 1 increase
previousDepthValue = depths[0]
for currentDepthValue in depths[1:]:
    if(previousDepthValue < currentDepthValue):
        increases += 1
    previousDepthValue = currentDepthValue

print(increases)