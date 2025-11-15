numbers = [1,2,3,4,5,6,7,8,9,10]

extracted_list = numbers[:5]
reversed_list = extracted_list[::-1]

print(f"Original list: {numbers}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_list}")


# I tried with for loop and its working as extected.

'''reverse_list = []
reverse = -1
for i in range(len(extracted_list)):
    reverse_list.append(extracted_list[reverse])
    reverse -= 1

print(f"Reversed extracted elements: {reverse_list}")
'''

