def calculate_calibration_sum(filename):
    digit_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    def find_digit(s, reverse=False):
        if reverse:
            s = s[::-1]
            digit_map_rev = {k[::-1]: v for k, v in digit_map.items()}
        else:
            digit_map_rev = digit_map
        
        for i, char in enumerate(s):
            if char.isdigit():
                return char
            for word, digit in digit_map_rev.items():
                if s[i:].startswith(word):
                    return digit
        return None

    total_sum = 0
    with open(filename, 'r') as file:
        for line in file:
            first = find_digit(line)
            last = find_digit(line, reverse=True)
            if first and last:
                total_sum += int(first + last)
    
    return total_sum

if __name__ == "__main__":
    result = calculate_calibration_sum('file.txt')
    print(f"The sum of all calibration values is: {result}")
        
