name = "uNimed"

# uppercase
print(name.upper())

# lowercase
print(name.lower())

# title
print(name.title())

# Eliminating white spaces

text = "  Hello World      "

# removes any leading (spaces at the beginning) and trailing
# (spaces at the end) characters (space is the default leading
# character to remove)
print(text.strip() + ".")

# remove space from left
print(text.lstrip() + ".")

# remove space from right
print(text.rstrip() + ".")


# joins and centers
test = "Hi,unimed!"

print(test.center(14))
print(test.center(14, "#"))
print(".".join(test))
