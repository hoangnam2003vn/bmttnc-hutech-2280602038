import re

def extract_and_sum_numbers(input_string):
    # Sử dụng biểu thức chính quy để tìm tất cả các số dương và âm
    # \-?\d+ tìm các số có thể có dấu trừ ở đầu, theo sau là một hoặc nhiều chữ số
    numbers = re.findall(r'(\-?\d+)', input_string)
    
    # Chuyển đổi các chuỗi số thành số nguyên
    numbers = [int(num) for num in numbers]
    
    # Tách thành hai danh sách: số dương và số âm
    positive_nums = [num for num in numbers if num > 0]
    negative_nums = [num for num in numbers if num < 0]
    
    # Tính tổng
    positive_sum = sum(positive_nums)
    negative_sum = sum(negative_nums)
    
    return positive_sum, negative_sum

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi: ")

# Tính toán kết quả
positive_sum, negative_sum = extract_and_sum_numbers(input_string)

# In kết quả
print(f"Giá trị dương: {positive_sum}")
print(f"Giá trị âm: {negative_sum}")