from bs4 import BeautifulSoup

html_file = open('C:/Users/CECCAFDE/workspace/sadbox/100-days-of-code/projects/pfds/Data/NWS Radar.html')

soup_object = BeautifulSoup(html_file, 'html.parser')
#help(soup_object)

tag = soup_object.h1

print(tag)

print(tag.string)

# Navigable String Object
print(type(tag.string))

our_ns = tag.string

print(our_ns)

# replace NS
tag.string.replace_with("Ilegal Information")

print(tag.string)

#help(tag)

for string in soup_object.stripped_strings:
    print(repr(string))

# accessing the parent of a stripped object

first_link = soup_object.a
print(first_link)

print(first_link.parent)



