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




