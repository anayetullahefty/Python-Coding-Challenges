#1094 - Experiments

# Read the number of test cases
num_test_cases = int(input())

# Initialize variables to store counts for each animal type
total_animals = 0
total_rabbits = 0
total_rats = 0
total_frogs = 0

for i in range(num_test_cases):
    amount, animal_type = input().split()
    amount = int(amount)

    # Update total counts based on animal type
    if animal_type == "C":
        total_rabbits+=amount
    elif animal_type == "R":
        total_rats +=amount
    elif animal_type == "S":
        total_frogs += amount
    total_animals += amount

# Calculate percentages
percent_rabbits = (total_rabbits / total_animals) * 100
percent_rats = (total_rats / total_animals) * 100
percent_frogs = (total_frogs / total_animals) * 100

# Print the results
print(f"Total: {total_animals} cobaias")
print(f'Total de coelhos: {total_rabbits}')
print(f'Total de ratos: {total_rats}')
print(f'Total de sapos: {total_frogs}')
print(f'Percentual de coelhos: {percent_rabbits:.2f} %')
print(f'Percentual de ratos: {percent_rats:.2f} %')
print(f'Percentual de sapos: {percent_frogs:.2f} %')
