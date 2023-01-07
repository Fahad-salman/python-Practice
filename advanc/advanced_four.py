import re 

user_search = re.compile('Apple')
user_search2 = re.compile('Apple , Tv , Android , Smartphone , laptop , Pc , Apple')
user_search3 = re.compile('Apple , Tv , Android , Smartphone')
items = 'Apple , Tv , Android , Smartphone , laptop , Pc , Apple'

result = user_search.search(items)

# span will let you know from where start and end at .
print(result.group() , result.span()) 
# group will bring the result 
all_ = result.group()
# also you can know from where start or end by using start() , or end()
from_start = result.start() 
from_end = result.end()
# There is find all will return everything like what ever the value user entered
res = user_search.findall(items)
print(res)
# thers is full match, the value -> user entered has to be exact match
specific = user_search2.fullmatch(items)
print(specific)
# also ther is match , match no
similar = user_search3.match(items)
print(similar)
