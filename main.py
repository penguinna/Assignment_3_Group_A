"""
Upper and Lower
"""
# Provide your solution here

def count_upper_lower(my_string: str) -> None:
    # n_upper = 0
    # n_lower = 0
    my_list = list(my_string)
    for c in my_list:
        if c == c.upper():
            count_upper = my_list.count(c.upper())
            # count_total = count_upper * len(my_list)
            # print(">> No. of Upper Case characters: " + str(count_total))
            print(">> No. of Upper Case characters: " + str(count_upper))
        else:
            count_lower = my_list.count(c.lower())
            print(">> No. of Lower Case characters: " + str(count_lower))

"""
Check 33
"""
# Provide your solution here


def has_33(numbers: list) -> bool:
    # my_list = list(numbers)
    for i in numbers:
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True
        else:
            return False





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

count_upper_lower("hEllO")
# count_upper_lower("NoTHinG wOrKs")
# count_upper_lower("disSAPoINtMenT")

# new_test = has_33([1, 3, 3, 4, 5])
# print(new_test)
# new_test = has_33([1, 2, 3, 4, 5])
# print(new_test)
# new_test = has_33([1, 3, 6, 4, 5])
# print(new_test)
