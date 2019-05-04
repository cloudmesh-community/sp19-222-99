def prime(x):
    if x >= 2:
        for i in range(2, x):
            if(x % i) == 0:
                print(x,"is prime\n")
                break
        else:
            print(x,"is not prime")
    else:
        print("error")
    return
