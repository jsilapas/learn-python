from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
#print txt.read()
first_line = txt.read()
print "The line in your file is %s" % first_line

#print "Type the filename again:"
#file_again = raw_input("> ")
#
#txt_again = open(file_again)
#
#print txt_again.read()

#####

#"eckie.txt" # string NAME of the file, not actual file or its contents
#open("eckie.txt")
#read(txt)
