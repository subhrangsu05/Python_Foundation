# Topic: Methods of Dictionary in Python
# Author: Subhrangsu Sinha
# Date: 25.08.2022

profile = {
    "name":{
        "first name":"Subhrangsu",
        "last name":"Sinha"
    },
    "company":"ABC",
    "Knowledge":["C","Java","Python","React"] 
}

# If we want to print all the keys of a dictionary:-
print(profile.keys())

# If we want to print all the values of a dictionary:-
print(profile.values())

# If we want print the all values with keys of a dictionary:-
print(profile.items()) # It will return in list format 

# If we want to add any key:values in the existing dictionary:-
profile.update({"location":"India"})
print(profile.items())

# If we wont get error while any value is not present in the dictionary:-
print(profile.get("country")) # --> It will returns None
# print(profile["country"]) # --> It will throws error
