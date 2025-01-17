#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mydict = dict()
for line in handle:
    if not line.startswith('From:'):
        continue
    words = line.split()
    #if words is present in dictionary then it will add one to it
    #or a new words will be added with value 1
    mydict[words[1]] = mydict.get(words[1],0) + 1


maxKey = None
maxItem = None
for k,v in mydict.items():
    if maxKey is None or maxItem < v:
        maxKey = k
        maxItem = v

print(maxKey,maxItem)
