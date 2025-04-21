import sys

# Read all input from stdin
data = list(map(int, sys.stdin.read().split()))

# Check that exactly 10 numbers were provided
if len(data) != 10:
    print("Error: Expected 10 integers.")
    sys.exit()

# Initialize count list for values 0 through 99
counts = [0] * 100

# Validate input and count frequencies
for num in data:
    if num < 0 or num > 99:
        print(f"Invalid input: {num} is not in 0-99")
        sys.exit()
    counts[num] += 1

# Find mode (value with highest frequency)
mode = 0
mode_freq = counts[0]

for i in range(1, 100):
    if counts[i] > mode_freq:
        mode = i
        mode_freq = counts[i]

# Output the mode and its frequency
print(f"{mode} {mode_freq}")
