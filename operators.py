x = 10
y = 20
# and operator
if (x < 20 and x >9):
    print(True)
else:
    print(False)
# or operator
if (x < 11 or x >9):
    print(True)
else:
    print(False)    
# not operator    
if (not(x < 10 and x >8)):
    print(True)
else:
    print(False)
# is operator
x = ["apple", "banana"]
y = ["apple", "banana"]    
z = x

print(x is z)
print(x is y)
print(x == y)
# in operator
x = ["apple","banana"]
print("banana" in x)
print("pinapple" not in x)
# Bitwise operatoprs
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(6 << 3)
print(6 >> 3)
# Operator precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
# Precedence rule
#() 
# **
# +x -x ~x
# * / // %
#  + - 
# >>
# <<
# &                        
# ^
# |
# ==, !=, >, <, is, is not, in, not, in
# not
# and
# or
