#multiple variables

# wanna take a variable address you can go deep down with the internal memory 

Frey = 666
id(666)

# it will provide you an variable "frey" address

# same as an string

github = 'frey'
id(github)

# it will give the address of github 

# can we have the same address ?
# yes it is when we have same values for e.g

a = 5
b = a

print(a)
print(b)
id(a)
id(b) 

# will give same address

# well if i just change 

a = 6
b = 7

# then there is nothing where the 5 is assined Right 

# so here comes the garbage collection 

type(a) #for looking on the type 
