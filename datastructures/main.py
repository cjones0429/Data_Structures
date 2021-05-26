from linked_list import LinkedList
from immediate_family import ImmediateFamily
import months
import random
# from months import Months
# import months
# #1. a) Store the months of the year. Grab the month in which Pi Day exists and print it to the console.


def find_month_from_holiday(self, holiday_str=""):
    self.months_tuple = (months.january, months.february, months.march, months.april, months.may, months.june,
                         months.july, months.august, months.september, months.october,
                         months.november, months.december)

    i = 0
    for selected_month in self.months_tuple:
        while len(selected_month.holiday) > 1:
            if selected_month.holiday[i] == holiday_str:
                return selected_month
            else:
                i += 1


pi_day_month = find_month_from_holiday(["Pi Day"])
print(pi_day_month)


# 1. b) Store all of the locations where you have celebrated your birthday.
#       Add three locations where you may celebrate your birthday in the future.
#       Iterate over the collection and print each one to the console.

bday_locations = {"Indiana", "Florida", "Tennessee"}
bday_locations.update(["Mexico", "Colorado", "Canada"])

for location in bday_locations:
    print(location)


# 1. c)Store sweepstakes contestants, uniquely identify each contestant.
# Create a sweepstakes object with a property of the data structure
# Add five contestants to the data structure
# Create a method on the sweepstakes class to randomly pick a winner
# Print the winner’s first name and last name to the console
# import random

contestants = []

contestant_one = contestants.append("Johnny Appleseed")
contestant_two = contestants.append("Terry Lewis")
contestant_three = contestants.append("Corey Davis")
contestant_four = contestants.append("Kyle Horton")
contestant_five = contestants.append("Dave Hines")

contestant_index = random.randint(0, 4)
print("Congratulations! You Win " + contestants[contestant_index]+"!")


# 2. Use a list to store the dictionary of your immediate family members,
# with each index of the list storing its own dictionary.
# Dictionary should contain the following keys:
# First name
# Last name
# Relationship

immediate_family_list = [ImmediateFamily("Seth", "Jones", "Father"),
                         ImmediateFamily("Angela", "Jones", "Mother"),
                         ImmediateFamily("Justin", "Valenti", "Brother"),
                         ImmediateFamily("Alex", "Jones", "Brother")]

for i in immediate_family_list:
    print(i)

# 3 Watch Linked List demo video on portal. Take the already created
# linked list with an append_node method and add on the following functionality:
# add_to_beginning
# contains_node

linked_list = LinkedList()
linked_list.append_node(80)
linked_list.append_node(90)
linked_list.add_to_beginning(70)
if linked_list.contains_node(80):
    print("yes")
else:
    print("no")


# 4

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)


# *****BONUS #1*****


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


r = Node(55)
r = insert(r, 34)
r = insert(r, 29)
r = insert(r, 41)
r = insert(r, 45)
r = insert(r, 73)
r = insert(r, 66)
r = insert(r, 87)

inorder(r)
