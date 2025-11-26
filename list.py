numbers = [1,2,3,4,5,6,7,8,9,10]

# print(numbers[-1])
# print(numbers[9])
# print the 10th element (index 9)

new_arr = [num ** 2 for num in numbers]
print(new_arr)


# Use a list comprehension to compute squares
# squares = [x * x for x in numbers]
# print("squared:", squares)


# def squared_list(numbers_list):
# 	"""Return a new list containing squares using a list comprehension."""
# 	return [x * x for x in numbers_list]


# if __name__ == "__main__":
# 	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 	print("original:", nums)
# 	print("squared (via helper):", squared_list(nums))

