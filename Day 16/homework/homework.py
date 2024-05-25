for i in range(120, 501, 3):
    if i % 3 == 1:
        print("can divide by 3", i)
    elif i % 5 == 1:
        print("can divide by 5", i)
    elif i % 7 == 1:
        print("can divide by 7" , i)