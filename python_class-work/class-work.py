# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)  
my_list.append(40)
my_list.insert(1, 15)  # Insert 15 at the second position (index 1)
my_list.extend([50, 60, 70])  # Extend with another list
my_list.pop(-1)  # Remove the last element
my_list.sort()  # Sort in ascending order
index_of_30 = my_list.index(30)  # Find the index of the value  30
print("Sorted List:", my_list)



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

#Create a program that stores a list of words. 
# Then, use list comprehension to create a new list that contains only the words 
# that have an odd number of characters.

mywords = []
n = int(input("Enter the number of words you want to input: "))
for i in range(n):
    word = input(f"Enter word {i+1}: ")
    mywords.append(word)
odd_length_words = [word for word in mywords if len(word) % 2 != 0]
print("Words with an odd number of characters:", odd_length_words)
