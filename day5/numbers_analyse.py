# ask users for 2 numbers

start = int(input("Enter the start of your range: "))
end = int(input("Enter the end of your range: "))

# create and display the list

numbers = list(range(start, end + 1))
print("Here’s your number list:", numbers)

# calculate and display

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

# list of comprehension

evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

# show first and last 3 numbers

print("First three numbers:", numbers[:3])
print("Last three numbers:", numbers[-3:])
