# Step 1: Create or expand your glossary dictionary with ten terms
glossary = {
    'variable': 'A named reference to a value that can be changed during program execution.',
    'function': 'A reusable block of code that performs a specific task when called.',
    'loop': 'A control structure that repeats a block of code as long as a condition is true.',
    'dictionary': 'A Python data structure that stores data as key-value pairs.',
    'boolean': 'A data type that can have the values True or False.',
    # Five new terms:
    'list': 'An ordered collection of items that can be changed (mutable).',
    'tuple': 'An ordered, immutable collection of items.',
    'string': 'A sequence of characters, used to represent text.',
    'set': 'An unordered collection of unique elements.',
    'argument': 'A value passed to a function when it is called.'
}

# Step 2: Print all words and meanings neatly using a loop
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n  {meaning}\n")