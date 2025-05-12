import itertools

# Danh sách ban đầu
my_list = [1, 2, 3]

# Sử dụng itertools.permutations() để tạo tất cả các hoán vị
permutations = list(itertools.permutations(my_list))

# In ra tất cả các hoán vị
print("Tất cả các hoán vị của danh sách", my_list, "là:")
for i, perm in enumerate(permutations, 1):
    print(f"Hoán vị {i}: {perm}")

# In tổng số hoán vị
print(f"\nTổng cộng có {len(permutations)} hoán vị.")