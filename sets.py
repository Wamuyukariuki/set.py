# user input to create two sets
set1 = input("Enter integers from 1 to 5 separated by space: ").split()
set2 = input("Enter integers from 4 to 9 separated by space: ").split()


# we convert the input strings into integers
int_set1 = set([int(number) for number in set1])
int_set2 = set([int(number) for number in set2])

new_set = int_set1 | int_set2

print(int_set1)
print(int_set2)
print(new_set)


