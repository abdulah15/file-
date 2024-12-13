file = open('file.txt', 'r')
count = 0

for i in file.readlines():

    count = count + 1 
print('Number of lines in the file: ', count)