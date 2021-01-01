
# how to find and print all pathes to source files in current machine

import sys
lp = sys.path
for l in lp:
    print(l)

import readOtherModules as rom

# how to find any module path
# # 
print('\n', rom.__file__, '\n') 


# this is how to add path
sys.path.append("C:Users\czarn\OneDrive\Desktop\PythonWorkspaces\PythonBasics1\modules")

for l in lp:
    print(l)