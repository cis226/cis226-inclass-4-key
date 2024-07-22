"""Program code"""

# First-party Imports
from datastructures import LinkedList, HashTable
from employee import Employee
from sorts import BubbleSort


def main(*args):
    """Method to run program"""

    ###########################
    # Linked List Work        #
    ###########################

    # Make an instance of Linked List
    linked_list = LinkedList()

    # Add to the front and back a few times.
    linked_list.add_to_front(5)
    linked_list.add_to_front(4)
    linked_list.add_to_front(3)
    linked_list.add_to_back(6)
    linked_list.add_to_back(7)
    linked_list.add_to_back(8)

    print("This list is:")
    print(linked_list)
    print()

    # Remove from front
    linked_list.remove_from_front()
    linked_list.remove_from_front()
    linked_list.remove_from_front()

    print("This list is:")
    print(linked_list)
    print()

    # Remove from back a couple of times
    linked_list.remove_from_back()
    linked_list.remove_from_back()

    print("This list is:")
    print(linked_list)
    print()

    # Also have ability to get the value that was returned
    returned_number = linked_list.remove_from_back()

    print("The removed number is:")
    print(returned_number)

    # Can also use full on objects inside of it if needed.
    employee_list = LinkedList()
    employee_list.add_to_front(Employee("David", "Barnes", 750.00))
    employee_list.add_to_front(Employee("Jean-Luc", "Picard", 640.00))
    print(employee_list)

    ###########################
    # Bubble Sort Work        #
    ###########################

    # Demonstrate how the bubble sort works.
    bubble = BubbleSort()
    # Create list to sort
    list_to_sort = [4, 2, 7, 3, 8, 6, 1, 9, 5]
    # Sort the list
    bubble.sort(list_to_sort)
    # Loop and print values in list.
    for value in list_to_sort:
        print(value)

    ###########################
    # Hash Table Work         #
    ###########################

    # Demonstrate how the hash table works
    valley_num_to_name = HashTable()
    print()
    print("Adding some entries to the HashTable")
    print('EX: valley_num_to_name.put(12345, "David Barnes")')

    valley_num_to_name.put(12345, "James Kirk")
    valley_num_to_name.put(23456, "Benjamin Sisko")
    valley_num_to_name.put(34567, "Kathryn Janeway")
    valley_num_to_name.put(45678, "Jean-Luc Picard")
    valley_num_to_name.put(56789, "Jonathan Archer")

    print("The created hash table")
    print(valley_num_to_name)
    print(valley_num_to_name.show_array())
    print("************************")

    print("Get a single value out from the hash table")
    print("valley_num_to_name.get(45678)")
    print(valley_num_to_name.get(45678))
    print()

    print("What if we add 2 entries that collide")
    print('valley_num_to_name.put(26189, "First Entry")')
    valley_num_to_name.put(26189, "First Entry")
    print('valley_num_to_name.get(26092, "Second Entry")')
    valley_num_to_name.put(26092, "Second Entry")

    print()
    print(valley_num_to_name)
    print(valley_num_to_name.show_array())
    print()

    print("Get the first entry out")
    print("valley_num_to_name.get(26189)")
    print(valley_num_to_name.get(26189))
    print("Got second entry instead. First was overwritten.")
    print()
    print()

    # What if we were to do string keys?
    print("What about using string keys")
    string_hash_table = HashTable()
    string_hash_table.put("foobar", "Joe Smith")
    string_hash_table.put("barbaz", "Fred Drees")
    print(string_hash_table.get("foobar"))
    print(string_hash_table.get("barbaz"))
    print(string_hash_table)
    print("String keys work too!")
