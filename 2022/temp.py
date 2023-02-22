data=[1,1,2,2,3]
values=[1,2,3]
counts=[2,2,1]

#print(max(counts))
m = [max(counts)]
print([i for i,v in enumerate(counts)])
indexes = [x for x in [i for i,v in enumerate(counts) if v in [max(counts)]] 
print(indexes)

#Get values
ans = [x for i,x in enumerate(values) if values[indexes[i]]] 

