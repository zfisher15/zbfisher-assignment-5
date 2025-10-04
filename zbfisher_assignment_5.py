# Step 1
# Adds numbers to the sequence depending on if they are even or odd
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: Sequence: "))
print(current_number, end=" ")
step_count = 0

while current_number != 1:
    # even numbers
    if current_number % 2 == 0:
        current_number //= 2
    # odd numbers
    else:
        current_number = (current_number * 3) + 1
    
    step_count += 1
    if current_number == 1:
        print(current_number, end="")
        break    
    print(current_number, end=" ")
# prints how many steps it took to get to 1 or under
if step_count != 0:
    print("\nSteps:", step_count)
else:
    print("Steps:", step_count)
print()
#Step 2
# Determines whether a number prime or not prime
print("=== Challenge 2: Prime Number Checker ===")
user_num = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {user_num - 1}...")
# checks for 1 and 0
if user_num < 2:
    print({user_num}, "is not prime")
# checks for 2 
elif user_num == 2:
    print(user_num, "is prime!")
else:
    for number in range(2, user_num):
        if user_num % number == 0:
            print(f"{user_num} is not prime (divisible by {number})")
            break
    else:
        print(user_num, "is prime!")
print()
#Step 3
# Prints out the multiplication table
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication table:")
print(" ", end="")
#prints starting row
for start_num in range(1, 11):
    print(f"{start_num:4}", end="")
print() 
# prints the rest of the table
for row in range(1, 11):
    print(f"{row:2}", end="")
    for col in range(1, 11):
        table_num = row * col
        print(f"{table_num:4}", end="")
    print()




