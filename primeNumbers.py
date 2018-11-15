def primenumber_generator(x):
    for x in range(1,x+1):
        if x>1:
            for i in range(2,x):
                if x%i==0:
                    break
            else:
                print(x)
