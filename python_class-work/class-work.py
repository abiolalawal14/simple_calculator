# Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.
mylist = []
n = int(input("Enter the number of integers you want to input: "))
for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    mylist.append(num)
sum_of_integers = sum(mylist)
print(f"The sum of the integers is: {sum_of_integers}")


#Create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.
mybooks = ("1984", "To Kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice","No Excuses")
for book in mybooks:
    print(book)


#Write a program that uses a dictionary to store information about a person, 
# such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.
mydict = {}
mydict['name'] = input("Enter your name: ")
mydict['age'] = int(input("Enter your age: "))
mydict['favorite_color'] = input("Enter your favorite color: ")
print("Person Information:", mydict)


#Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.
myset1 = set()
myset2 = set()
n1 = int(input("Enter the number of integers for the first set: ")) 
for i in range(n1):
    num = int(input(f"Enter integer {i+1} for the first set: "))
    myset1.add(num) 
n2 = int(input("Enter the number of integers for the second set: "))
for i in range(n2):
    num = int(input(f"Enter integer {i+1} for the second set: "))
    myset2.add(num)
common_elements = myset1.intersection(myset2)
print("Common elements in both sets:", common_elements)


#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.