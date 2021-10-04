'''Tips and Tricks Executed'''
# 1. Get mulitple inputs:
x, y, z = input("give me numbers: ").split(",") # [If "," is not given then the default space is "" space]
print(x)
print(z)
'''output:
give me numbers: 25 36
25
36'''

# 2. For using lot of conditions in FOR LOOP
# ex:
subscribers = 2400
likes = 200
comment =56

if subscribers > 1500 and likes > 100 and comment > 30:
    print("Awesome Video!!!")

# TRICK for many conditions in FOR LOOP:
subscribers = 2400
likes = 200
comment =56
views = 10000
joiners=10

conditions = [subscribers > 1500, likes > 100 , comment > 30, views>1200, joiners > 5]

if all(conditions):
    print("Awesome Content!!!")

#3. We just need to fulfill only ONE condition
#ex:
subscribers = 2400
likes = 200
comment =56

if subscribers > 2500 or likes > 500 or comment > 30:
    print("Awesome Video!!!")

# TRICK for any ONE conditions in FOR LOOP:
subscribers = 2400
likes = 200
comment =56
views = 10000
joiners=10

checkers = [subscribers > 2500, likes > 500 , comment > 30, views>120000, joiners > 500]

if any(checkers):
    print("Awesome Content!!!")

# 4. Switch the variables of the variables:
# ex:
subs = 2400
likes = 200

print (subs,likes)
'''print("Traditional way:")
temp = subs
subs = likes
likes = temp
print (subs,likes)'''

# Trick
print("Trick for swapping!!!!")
subs, likes = likes, subs
print (subs,likes)

# 5. Remove all the duplicates from the list by converting it to SET and then again back to LIST
a = [1,2,5,4,7,6,8,9,0,2,4,4,6,5,34,345,8845,7,3,5,6,8,2,5,8,0,4,63,3]
print(a)

a = list(set(a))
print(a)

# 6. List with duplicates, get maximum times repeated number
a = [1,2,5,4,7,6,8,9,0,2,4,4,6,5,34,3,457,7,9,8,4,9,9,9,9,8845,7,3,5,6,8,2,5,8,0,4,63,3]
print(a)

most = max(set(a), key=a.count)
print(most)

# 7. Find out the square of odd_numbers from the List
odd_sqaures = []
for i in range(11):
    if i % 2 == 1:
            odd_sqaures.append(i**2)

print(odd_sqaures)

print("The Trick for the same")
odd_sqaures = [i**2 for i in range(11) if i%2 == 1] # List Comprehension
print(odd_sqaures)

# 8. Function where we need to give lot many inputs
#ex:
print("Traditional Logic for SUM")
def sum(a, b):
    res = 0
    return a+b

res = sum(2,3)
print(res)

print("Trick for multiple inputs in a function")
def sum(*a):
    result = 0
    for i in a:
        result = result + i
    return result

res = sum(2,3, 5, 8, 2, 766)
print(res)

#9.  STRING REVERSE
name = "Nelly Furtado"
print(name)

print("Trick for STRING REVERSE")
reverse =  "Nelly Furtado"[::-1]
print(reverse)

'''numRev = 12333[::-1] #Throws an ERROR
print(numRev)'''

#10. Check Pallindrome
name = "madam"
print(name)

print("Trcik for Pallindrome!")
isPallindrome = name.find(name[::00-1])==0
print(isPallindrome)
