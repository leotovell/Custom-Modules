lines = []
for line in open("input.txt").readlines():
    lines.append(line[:-1])


#My logic:
# Until we 'call cd ..', we keep the sum of the directory the same, however we need variables for the current subdirectory. Let's use a dictionary.

# All commands:
# cd - change directory
# cd x - in a level
# cd .. out a level
# cd / - master
# ls - list files/dir
#   123 abc - 123(size), abc(filename)
#   dir xyz - directory named xyz

directories = {}

def CalculateDirectorySize(directories):
    pass


inDir = False
directoryFilesize = 0
# for line in lines:
for i in range(len(lines)):
    line = lines[i]
    line = line.split(" ")
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "/":
                # Move back to the complete master root.
                pass
            if line[2] == "..":
                # Move up a level in directory map. (towrads master)
                pass
            else:
                dirFilesize = 0
                # Move down a level in a directory map (away from master)
                pass
        elif line[1] == "ls":
            # Next x lines list the contents of the directory.
            pass
    else:
        if line[0] == "dir":
            # Add dir to dictionary, mark as unvisited
            pass
        else:
            filesize = int(line[0])
            dirFilesize += filesize
            # Append the filesize to the current dir filesize
            pass
