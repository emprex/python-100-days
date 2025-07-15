cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


############################

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#############################

answer = 17
if answer != 42:
    print("That is not the right answer. Please try again!")

##############################

banned_users = ['andrew', 'caroline', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
   
 # try myself

s1 = 'la vie est belle'
s2 = 'la vie est belle'
s3 = 'La vie est belle'

print(s1 == s2) # true
print(s1 == s3) # false  
print(s1 == s3.lower()) # true 

age1 = 21 
age2 = 32
age3 = 43

print(age1 >= 23 and age2 >= age3) # false




