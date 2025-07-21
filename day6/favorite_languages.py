# A dictionary of similar objects

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

### loop

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

### loop all the key

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")       

#### sorted

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

##### value

print("The following language have been mentioned.")    
for language in favorite_languages.values():
    print(language.title())

print("The following language have been mentioned.")    
for language in set(favorite_languages.values()):
    print(language.title())


poll_list = ['phil', 'sarah', 'guillaume', 'olivier', 'jen', 'lea']

for person in poll_list:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, what's your favorite programming language?")
