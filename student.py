import exp6 as e
name=input('Enter student name:')
print('Enter marks separated by space: ',end=" ")
marks=list(map(int,input().split()))

avg=e.average(marks)
grade=e.grade(avg)
print(f"student:{name}")
print(f"marks:{marks}")
print(f'average:{avg}')
print(f'grade:{grade}')
