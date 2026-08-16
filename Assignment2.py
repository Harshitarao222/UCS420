# Q1
roll_no = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_no]
L = [digit * 10 for digit in digits]

print("Initial list L:", L)


L.append(250)
print("After append(250):", L)


L.insert(2, 350)
print("After insert(2, 350):", L)



L.remove(250)
print("After remove(250):", L)



removed_element = L.pop(2)
print("Element removed using pop():", removed_element)
print("After pop(2):", L)

L.sort()
print("Ascending order:", L)

L.sort(reverse=True)
print("Descending order:", L)

print("First three elements:", L[:3])
print("Last three elements:", L[-3:])


average = sum(L) / len(L)

greater_than_average = [x for x in L if x > average]

print("Average of L:", average)
print("Elements greater than average:", greater_than_average)






# Q2

scores = tuple(L[:8])

print("\nTuple scores:", scores)

highest_score = max(scores)
highest_index = scores.index(highest_score)


lowest_score = min(scores)
lowest_count = scores.count(lowest_score)

print("Highest score:", highest_score)
print("Index of highest score:", highest_index)

print("Lowest score:", lowest_score)
print("Number of times lowest score appears:", lowest_count)

reversed_scores = list(reversed(scores))

print("Reversed tuple as a list:", reversed_scores)


user_score = int(input("\nEnter a score to search: "))

if user_score in scores:
    print("First occurrence index:", scores.index(user_score))
else:
    print("Score is not present in the tuple.")



try:
    scores[0] = 100
except TypeError as e:
    print("\nError while modifying tuple:", e)
   

first_score, second_score, *remaining_scores = scores

print("\nFirst score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)






# Q3: Random Numbers

import random
from collections import Counter

# Use roll number as the random seed
roll_no = input("Enter your roll number: ")
random.seed(int(roll_no))

# i. Generate 100 random numbers between 100 and 900 inclusive

random_numbers = [random.randint(100, 900) for _ in range(100)]

print("\nRandom numbers:")
print(random_numbers)


# ii. Count and print all odd numbers

odd_numbers = [x for x in random_numbers if x % 2 != 0]

print("\nOdd numbers:")
print(odd_numbers)

print("Number of odd numbers:", len(odd_numbers))


# iii. Count and print all even numbers

even_numbers = [x for x in random_numbers if x % 2 == 0]

print("\nEven numbers:")
print(even_numbers)

print("Number of even numbers:", len(even_numbers))


# iv. Count and print all prime numbers

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


prime_numbers = [x for x in random_numbers if is_prime(x)]

print("\nPrime numbers:")
print(prime_numbers)

print("Number of prime numbers:", len(prime_numbers))


# v. Number occurring most frequently

frequency = Counter(random_numbers)

most_frequent_number, highest_frequency = frequency.most_common(1)[0]

print("\nMost frequently occurring number:", most_frequent_number)
print("Number of times it occurs:", highest_frequency)




# Q4: Sets

roll_no = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_no[:8]]

A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("\nSet A:", A)
print("Set B:", B)

union_set = A.union(B)

print("\nUnion of A and B:", union_set)



intersection_set = A.intersection(B)

print("Intersection of A and B:", intersection_set)



A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print("A - B:", A_minus_B)
print("B - A:", B_minus_A)



symmetric_difference_set = A.symmetric_difference(B)

print("Symmetric difference:", symmetric_difference_set)




print("Is A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))


X = int(input("\nEnter a value to discard from A: "))

A.discard(X)

print("Set A after discard:", A)




# Q5: Dictionaries

my_dict = {
    "name": "YOUR_NAME",
    "roll_no": "YOUR_ROLL_NUMBER",
    "branch": "YOUR_BRANCH",
    "age": "YOUR_AGE",
    "city": "YOUR_HOME_CITY"
}

print("Original dictionary:")
print(my_dict)


my_dict["location"] = my_dict.pop("city")

print("\nAfter renaming city to location:")
print(my_dict)



my_dict["cgpa"] = 9.5

print("\nAfter adding CGPA:")
print(my_dict)



my_dict["age"] += 1

print("\nAfter increasing age by 1:")
print(my_dict)



dict_pop = my_dict.copy()
dict_del = my_dict.copy()

# Using pop()
removed_branch = dict_pop.pop("branch")

print("\nDictionary after deleting branch using pop():")
print(dict_pop)
print("Value returned by pop():", removed_branch)


del dict_del["branch"]

print("\nDictionary after deleting branch using del:")
print(dict_del)


print("\nKey-value pairs:")

for key, value in my_dict.items():
    print(f"{key} → {value}")



if "email" in my_dict:
    print("\nEmail:", my_dict["email"])
else:
    print("\nEmail key does not exist in the dictionary.")



friend_dict = {
    "name": "Rahul Sharma",
    "roll_no": "1029999999",
    "branch": "Electronics",
    "age": 21,
    "city": "Delhi"
}

print("\nFriend dictionary:")
print(friend_dict)



merged_dict = {**my_dict, **friend_dict}

print("\nMerged dictionary:")
print(merged_dict)


string_values_dict = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nDictionary containing only string values:")
print(string_values_dict)