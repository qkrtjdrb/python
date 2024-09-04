for i in range(1,6):
    print('*'*i)

for i in range(1,6):
    print(' '*(5-i)+'*'*i)

n=3
for i in range(n):
    print(' '*(-i+2)+'*'*(2*i+1))

for i in range(n, 5):
    print(' '*(1 + (i % 3))+'*'*(3 - 2*(i % 3)))

# 잘되었습니다