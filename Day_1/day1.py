file = open("input.txt" , 'r')
lines = file.readlines()

left = list()
right = list()

for line in lines:
    line = line.split()
    left.append(line[0])
    right.append(line[1])

left.sort()
right.sort()

sum = 0
for i in range(len(lines)):
    sum += abs(int(left[i]) - int(right[i]))

print(sum)