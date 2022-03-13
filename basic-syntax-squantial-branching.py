"""
The basic syntax of the Python programming language ;
1. Sequential : Sequential steps
2. Branching : Step jump, if condition is met
3. Loops : Repeating the same steps many times for and until the condition is met
"""

# Examples and reviews
# Sequential

print('Mom says : "go to the shop!"')
print('Joe answered : "OK, what should i do there?"')
print('Mom says : "please buy me a bottle of milk!"')
print('And then joe went to the shop and started shopping')

# Branching

egg_count = 100
print(f'egg count {egg_count} eggs')
milk_bottle_count = 10
print(f'milk bottle count {milk_bottle_count} bottles')

if milk_bottle_count > 0:
    print('Joe brings enough money')
    print('Joe bought a bottle of milk')
else:
    print("Joe didn't buy a bottle of milk")

if egg_count == 0:
    print("Joe didn't buy the eggs")
else:
    print('and Joe bought 6 eggs too')

print("and Joe handed over the groceries to his mother")

