unites=(int(input('Enter number of unites  : ')))
while True:
    print(unites)
    if unites <= 100:
        print('bill = 0')
    elif unites <=200:
        bill = (unites - 100) * 5
        print(bill)
    else:
        bill=(100 * 5)+(unites-200)* 10
        print(bill)    