def longest_strike(arr):
    longest_strike = 0
    current_strike = 1
    longest_number = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_strike += 1
        else:
            if current_strike > longest_strike:
                longest_strike = current_strike
                longest_number = arr[i - 1]
            current_strike = 1

    if current_strike > longest_strike:
        longest_strike = current_strike
        longest_number = arr[-1]

    return longest_number, longest_strike

result_number, result_count = longest_strike(myArray)
print(f'Longest: {result_count}')
print(f'Number: {result_number}')