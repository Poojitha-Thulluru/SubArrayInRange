try:
    nums_array = list(map(int, input("Enter only integers separated by space : ").split()))
    start = int(input("Enter the starting index : "))
    end = int(input("Enter the ending index : "))
    if start <= end and 0 <= start < len(nums_array) and 0 < end <= len(nums_array):
        print("The sub array is : ", nums_array[start: end + 1])
    else:
        print("Enter valid range values")
except ValueError:
    print("Invalid Input. Please enter only integers")
