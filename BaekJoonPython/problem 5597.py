import sys

students = [i for i in range(1,31)]

for _ in range(28):
    applied = int(sys.stdin.readline())
    students.remove(applied)

print(min(students))
print(max(students))