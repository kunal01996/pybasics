# Given a .txt file that has a list of a bunch of names, count how many of each name there
# are in the file, and print out the results to the screen. I have a .txt file for you,
# if you want to use it!
#
# Extra:
#
#     Instead of using the .txt file from above (or instead of, if you want the challenge),
# take this .txt file, and count how many of each “category” of each image there are.
# This text file is actually a list of files corresponding to the SUN database scene
# recognition database, and lists the file directory hierarchy for the images.
# Once you take a look at the first line or two of the file, it will be clear which part
# represents the scene category. To do this, you’re going to have to remember a bit about
# string parsing in Python 3. I talked a little bit about it in this post.

f = open('files/names.txt', 'r')

contents = f.read().split('\n')

unique = set(contents)

names_dict = dict()

for u in unique:
    count = 0
    for c in contents:
        if u == c:
            count += 1

    names_dict[u] = count


print(names_dict)

# Reading Sun

fs = open('files/sun.txt', 'r')
fsContents = fs.read().split('\n')

fsFinalContents = [i.split('/')[1] for i in fsContents]

uniqueFs = set(fsFinalContents)
sun_dict = dict()

for u in uniqueFs:
    count = 0
    for f in fsFinalContents:
        if u == f:
            count += 1
    sun_dict[u] = count

print(sun_dict)
