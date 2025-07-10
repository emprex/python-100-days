# Variables 
message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World"
print(message)

# try my self

spl_mess = "Zuzana tu revindras pres de moi"
print(spl_mess)

# strings

name = "guillaume strohecker"
print(name.title())
print(name.upper())
print(name.lower())

# using variables in strings

first_name = "zuzana"
last_name = "compelova"
full_name =f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")
message = f"hello, {full_name.title()}!"
print(message)

# adding whitespace

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJaveScript")

# try my self

person_name = "Eric"
print(f"Hello {person_name}, would you like to learn some python today?")
print(person_name.lower())
print(person_name.upper())
print(person_name.title())

print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")
famous_person = "Albert Einstein"
message = "A person who never made a mistake never tried anything new"
print(f"{famous_person} once said, \"{message}\"")

name_to_strip = '\n  zuzana\t'
print(name_to_strip)
print(name_to_strip.lstrip())
print(name_to_strip.rstrip())
print(name_to_strip.strip())
print(name_to_strip)