numbers = []
shoe_sizes = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
shoe_sizes.append(8)
shoe_sizes.append(9)
shoe_sizes.append(10)
shoe_sizes.append(11)
shoe_sizes.append(12)

print(f"Numbers list {numbers}")
print(f"Shoes sizes list {shoe_sizes}")

# duplicates

if(not numbers.__contains__(3)):
   numbers.append(3) # won't be appended
if(not numbers.__contains__(6)):
   numbers.append(6) # will be be appended
print(f"Numbers list after update:  {numbers}")
for i in range(10,16):
   if(not shoe_sizes.__contains__(i)):
      shoe_sizes.append(i)
print(f"Shoe sizes list after update: {shoe_sizes}")
combined_lists = numbers + shoe_sizes
print(f"Combined list : {combined_lists}")