def divide(a,b):
    try:
        print(a/b)
    except:
        print('An Error has occured')
a,b=map(int,input().split())
divide(a,b)