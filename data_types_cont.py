s = "I am a strint"
print("The type of s is ", type(s))

#boolean
yes = True
print("The type of yes is ",type(yes))
no = False
print("The type of no is ",type(no))

#List -- odered and changeable

alpha_list = ["a", "b","c"]
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

#Tuple -- ordered and unchangeable

alpha_tuple = ("a", "b", "c")
print(type(alpha_typle))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("We can't add elements to tuples!")
	print(alpha_tuple)

