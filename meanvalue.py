#The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers
mean1 = 38
wrong_number =36
correct_number =56
total_numbers =40
#sum of 40 numbers
sum = mean1*total_numbers
print("the sum of 40 numbers is: ",sum)

#correct sum of these numbers
num2=sum-((wrong_number)-(correct_number))
print("sum((wrong_number)-(correct_number)) is: ",num2)

#the correct mean
mean2=num2/total_numbers
print(mean2)

