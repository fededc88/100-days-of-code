from bs4 import BeautifulSoup


#help(BeautifulSoup)

html_file = open('C:/Users/CECCAFDE/workspace/sadbox/100-days-of-code/projects/pfds/Data/NWS Radar.html')

soup_object = BeautifulSoup(html_file, 'html.parser')
#help(soup_object)

print(soup_object.prettify())

# Tag names

tag = soup_object.h1

print(tag)
print(tag.name)

tag.name = 'ache 1'
print(tag.name)

# Tag atributes

#list the attributes
print(tag.attrs)

#add and attribute
tag['attribute 2'] = 'attricute 2'
print(tag.attrs)

# delete tag attribute
del tag['attribute 2']

print(tag.attrs)


# Navigate tree

soup_head = soup_object.head
print(soup_head.title)

print(soup_head.attrs)

print(soup_object.body.li)
print(soup_object.a)
