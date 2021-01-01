import sys

# shows where is python installed
print('\n', sys.prefix)

# where are compiled binaries are stored
print('\n', sys.exec_prefix)

print(sys.prefix)
print(sys.prefix is sys.exec_prefix)

# where does python look for the code
import sys
lp = sys.path
for l in lp:
    print(l)
import readOtherModules



#import testMyModule