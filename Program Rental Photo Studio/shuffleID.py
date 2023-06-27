import string    
import random # define the random module  
S = 5  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
userID = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
print("The randomly generated string is : " + str(userID)) # print the random data  