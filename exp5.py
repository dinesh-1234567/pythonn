with open('t.txt', 'w') as file:
    file.write("Welcome world")
with open('t.txt','r') as f:
    for i in f:
        print(i)