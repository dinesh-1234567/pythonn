def store(n):
    a=list()
    for i in range(n):
        a.append(int(input()))
    print(a[::-1])
    print(sum(a))
    print(sum(a)//2)
n=int(input('Enter no of numbers to be in list: '))
store(n)