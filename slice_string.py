# slice string

randomText = "Here You can print any word from here let/'s look How we do this"
# so start from zero to whatever in your statement

print(randomText[0])

# The number you insert , python will search in Your statement

# here 0 == H in your statement

print(randomText[9])

# here 9 == c in your statement

# [start] => will take one value 

# [start:stop] => will take first value until second you enterd

# [start:stop:stepover] => will take first value until second you enterd stepover like skip

print(randomText[0:8:2])


# questions one:

# what will happen for this code?

print(randomText[2:])

# answer => will print from later 2 util the end.


# questions two:

#what will happen for this code?

print(randomText[:5])

# answer => will print from later 0 util the the value we insert.


# questions three:

# what will happen for this code?

print(randomText[::2])

# answer => will print as a default .

# if you enter negative number will start from the end

# [::-1] will print reverse (from end to start) 
