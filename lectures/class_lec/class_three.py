class Actor():
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.my_dict ={
            'name':'dwayne johnson',
            'job':'actor',
            'age':'50'
        }
    
    def __str__(self):
        return f'color -> {self.color}'

    def __len__(self):
        return 8

    def __call__(self):
        return'Hey!'
    
    def __getItem__(self,i):
        return self.my_dict[i]

action_figure = Actor('Blue',6)

print(action_figure.__str__()) 
print(len(action_figure))
print(action_figure())
print(action_figure.my_dict['name'])
print(action_figure.my_dict['job'])
print(action_figure.my_dict['age'])