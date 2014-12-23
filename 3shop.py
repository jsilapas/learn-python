from sys import argv

"""
This script will take a filename argument and open it up for writing.
It will then prompt the user to enter three shopping list items, one by one.
After the third item has been entered, those lines will be written to a file
'shopping_list.txt'
Then, everything closes

"""
#script, filename = argv

#print "We're going to erase %r." % filename
#print "If you don't want that, hit CTRL-C (^C)."
#print "If you do want that, hit RETURN."

shop_list = raw_input("What would you like your shopping list to be called? ")

print "Opening the shopping list..."
target = open(shop_list, 'w')

#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask for your 3 shopping items."

item1 = raw_input("Item 1: ")
item2 = raw_input("Item 2: ")
item3 = raw_input("Item 3: ")

print "I'm going to add these to your shopping list!"

target.write(item1)
target.write("\n")
target.write(item2)
target.write("\n")
target.write(item3)
target.write("\n")

#print "Closing your shopping list..."

target.close()

target = open(shop_list, 'r')

print target.read()
print target.read()
print target.read()
print target.read()
print target.read()

target.close()


