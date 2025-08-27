text = " Rahul Zapadiya 1234567 "

# index checking 
print(text[0])
print(text[1])
print(text[2])
print(text[4])

# String slicing

print(text[0:2]) # Ra
print(text[0:10]) # Rahul 1234
print(text[:7])  # Rahul 1
print(text[1:]) # ahul 1234567
print(text[::2]) # Rhl1357
print(text[::-1]) #7654321 luhaR
print(text[-1:]) # 7
print(text[-5:-2]) #

# string method
# * case conversion
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

# * searching
print(text.find("iy"))
print(text.count("a")) # count how many a

# *Cheaking
print(text.startswith("Ra"))
print(text.startswith("Za"))
print(text.endswith("67"))
"report,pdf".startswith("re")   
print(text.isalpha())
print(text.isnumeric())
print(text.isalnum())
print(text.isdigit())

# *Relace & remove
print(text.replace("Rahul","rahul"))
print(text.strip()) 

# * split & join
print(text.split(","))
",".join(["a","b","c"])   # "a,b,c"

print(sorted(text))
print(len(text))
print(ord("Z"))
"".join(reversed("abc"))   # "cba"
chr(65)   # "A"
