# exercise 2 questions-> check the list and insert to duplicateList . (Comprehensions)

words =['a','b','c','d','f','f','c','a']

duplicateList = list(set([find for find in words if words.count(find) > 1]))
print(duplicateList)