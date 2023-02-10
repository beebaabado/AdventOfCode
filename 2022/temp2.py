x = {}
y = {}
stack = []
x = y
x['cat'] = {"meow"}
stack.append(x)
x['cat'] = {"woof"}
print("X: ", x)
print("Y: ", y)

x = {'asdfljj': {'item1': {'bird.txt': "cheep"}, 'item2': {'cat.txt': "meow"}}}

print("X: ", x)
print("Y: ", y)

x = stack.pop() 
print("X: ", x)
print("Y: ", y)
