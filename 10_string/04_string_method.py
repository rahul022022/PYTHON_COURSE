# s = "hello wolrd" # strings are immutable

# name[0] = "R" # no cannot do this

# a = len(s)
# print(a)
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())

# text = "  hello world  "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip())# Output: "hello world  "
# print(text.rstrip())# Output: "  hello world"


# text ="Python is fun"
# print(text.find("is")) # Output: 7
# print(text.replace("fun","awesome")) # Output: "Python is awesome


# text  = "Apple,banana,pineapple"

# print(text.split(","))
# print(",".join(['apple','banana']))

text ="Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False