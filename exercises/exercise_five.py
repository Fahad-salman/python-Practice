# Exercise 5 questions => (print 1 as * and 0 as ' ' )

picture = [
    [1,1,1,1,1,0,0,0,0,0,0,0,],
    [1,0,0,0,0,0,1,1,0,0,0,0,],
    [1,0,0,0,0,0,1,0,1,0,0,0,],
    [1,1,1,0,1,0,1,0,0,1,0,0,],
    [1,0,0,1,1,0,1,0,0,1,0,0,],
    [1,0,1,0,1,0,1,0,1,0,0,0,],
    [0,1,1,1,1,0,1,1,0,0,0,0,],
    [1,0,0,0,1,0,0,0,0,0,0,0,],
]

for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*',end='')
        else:
            print(' ',end='')
    print('') # this is to make a new line ror each row
