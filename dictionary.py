#define a dictionary data structure

#dictionaries have key:valyue pairs for the elements
example_dict = {
	"class" : "ASTR 119",
	"prof" : "Brant",
	"awesomeness" : 10
}

print ("The type of example_dict is ", type(example_dict))

#get value via key
course = example_dict["class"]
print(course)

example_dict["awesomeness"] += 1

#print the dictionary
print(example_dict)


#print dictionary element by element
for x in example_dict.key():
	print(x, example_dict[x])