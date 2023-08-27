def maximum69Number(num):
    num_str = str(num)
    
    for i in range(len(num_str)):
        if num_str[i] == '6':
            num_str = num_str[:i] + '9' + num_str[i+1:]
            break

    return int(num_str)

# Example usage:
num=int(input())
result = maximum69Number(num)
print(result)  # Output will be 9969
