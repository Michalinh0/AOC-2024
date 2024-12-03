file = open("input.txt" , 'r')
lines = file.readlines()

left = list()
right = list()

for line in lines:
    line = line.split()
    left.append(line[0])
    right.append(line[1])

right_set = dict()
for id in right:
    if id in right_set.keys():
        right_set.update({id:right_set[id] + 1})
    else:
        right_set[id] = 1

sum = 0

for id in left:
    if id in right_set.keys():
        sum += int(id) * int(right_set[id])

print(sum)
