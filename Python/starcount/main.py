def calculatesum(filename):
    total = 0

    with open(filename, 'r') as file:
        for line in file:
            digits = [ char for char in line if char.isdigit()]
            if digits:
                calibration = int(digits[0] + digits[-1])
                total += calibration
    return total

print(calculatesum('file.txt'))
