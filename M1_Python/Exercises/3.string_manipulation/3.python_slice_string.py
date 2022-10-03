# Specify the start index and the end index, separated by a colon,
# to return a part of the string.

test = "data-science"

print(test[:2])
# output:da

print(test[1:])
# output:ata science

print(test[4:7])
# output:-sc

print(test[4:7:2])
# output:-c

print(test[::-1])
'''invert text'''
# output: ecneics-atad
