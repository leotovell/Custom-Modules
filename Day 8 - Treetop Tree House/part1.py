lines = []
for line in open("input.txt").readlines():
    lines.append(line.strip())

visibleCount = 0
invisibleCount = 0

for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        tree = int(line[j])

        inCol = [line[:j], line[j+1:]] # Column
        for k in range(len(lines)): # Row
            r = lines[k]
            if r != line:
                inRow = [r[:j], r[j+1:]]

        if tree > int(max(inCol)) and tree > int(max(inRow)):
            visibleCount += 1
        else:
            invisibleCount += 1
        # In Col is looking from left then looking from right.
        # In Row is look from the top and then looking from he bottom (reversed obvs)
            

print(visibleCount)

# TODO not max in row, just visible from left or right or up or down. Need to split up the lists.