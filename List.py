#list 
# well for list in python we have to use []
nums = [12,45,65,34]
nums = [0]
#last one
nums = [3]
#alt
nums = [-1]

# from 45 to all

nums = [1:]

# Now let's use some of the strings too

Names = ['frey','lol','Danix','chutiyaman']

names = [0]
names = [1]
names = [2]
names = [3]

# ok so we know that this will work fine on this but can we mix int and strings

mix = [100,'fr3y'75.01]

#well ofcourse it will work that's so cool for using list 
# unless, like others language we call mix types here xD (easy and classic)

# so now we i have to add both above list in one can i ?

# "yes" i can 

add = [nums,Names]

# and now the important thing is this list are mutables means it can be changed at any time life it is like life change always !!

# well if i have to add 76 on my nums list i can like 

nums.append(76) # it will add 76
# there is another type too which is insert 
nums.insert(2,7) #it will just add 76 on the place of 2 
#result will be [12,45,7,65,34,76]
nums.clear #clear out all list you have 
nums.remove(12) #it will just remove 12
nums.sort() # in sort form
nums.pop(1)#it will delete 7 
nums.pop() # it will just pop out the last value
del nums[2:] # it will delete all values agter 2 
nums.extend[(12,45,78,35,56)] # add multple values
#now inbuilt fun 
# like 
max(nums)
min(nums)
sum(nums) 



# well this is all and also check out the pyton docs
