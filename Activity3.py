#Taking inputs of test scores from user
Mathematics=int(input("What did you get on your Maths test?"))
Biology=int(input("What about Biology?"))
Spanish=int(input("And Spanish?"))
History=int(input("And last but not least, History?"))
#Calculating percentage of marks
sum=Mathematics+Biology+Spanish+History
print("The sum of all your scores is:", sum)
perc=(sum/400)*100
print("Lets see your overall percentage!")
print(perc)
print("Good job!")