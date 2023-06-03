keyboard = [[0] * 6] * 5
print(keyboard)

count = 0

for y in range(5):
    for x in range(6):
        keyboard[y][x] = chr(65 + count)
        print(keyboard)
        count += 1

print(keyboard)