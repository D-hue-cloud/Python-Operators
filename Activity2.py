Amount=int(input("Please inpput amount of GBP you would like to withdraw: £"))
#Calculating amount of different types of bank notes that will be withdrawn
no_100GBP=Amount//100
no_50GBP=(Amount%100)//50
no_10GBP=(Amount%100)%50//10
no_1GBP=(Amount%100)%50%10//1

print("The number of £100 notes withdrawn will be",no_100GBP)
print("The number of £50 notes withdrawn will be", no_50GBP)
print("The number of £10 notes withdrawn will be",no_10GBP)
print("The number of £1 coins withdrawn will be", no_1GBP)