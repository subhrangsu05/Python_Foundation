# Topic: Introduction with Dictionary in Python
# Author: Subhrangsu Sinha
# Date: 25.08.2022

# Dictionary is a collection of key-value pairs. It can be also 1D,2D,3D....
'''
1) Dictionary is unordered
2) It is mutable
3) It is indexed
4) can not contain duplicate keys, If we want to add duplicate keys forcefully then the value will be overwrite
'''
# 1D Dictinary:-
details = {"company":"ABC COMPANY",
"name":"Subhrangsu",
"Program":"Python",
"age":24
}

print(details)
# If we want to show age only:-
print(details["age"])

# If we want to change any data:-
details["Program"]="React"
print(details)

# 2D Dictionary:-
profile = {
    "name":{
        "first name":"Subhrangsu",
        "last name":"Sinha"
    },
    "company":"ABC",
    "Knowledge":["C","Java","Python","React"]  # We can add list in the dictionary
}

print(profile)

# If we want to access the 2D elements:-
print(profile["name"]["first name"])
print(profile["Knowledge"][2]) # we're using index no due to LIST

# If we want to change the value of 2D element:-
profile["Knowledge"][2] = "Angular"
print(profile)




# DISCLAIMER: Dictionary mainly helps to create Json data