'''
t -> type(str) | contains a stock ticker
d -> type(list(str)) | represents dates where t is mentioned
x -> type(dict[d]) | represents t mentions on a given t
o -> type(float) | containing overall sentiment towards t
s -> type(dict[d]) | representing sentiment towards t on d
a -> type(dict[d]) | represents total stock mentions on d
r -> type(dict[d]) | represents ratio of x[d] to a[d]
p -> type(dict[d]) | represents position to take; either [-1,0,1]
'''
