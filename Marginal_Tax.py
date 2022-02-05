status_menu = """
1. Single
2. Married, Filing Jointly
3. Married, Filing Separately
4. Head of Household
"""
print(status_menu) #prints the list of filing statuses

status = int(input("Enter filing status:"))  #allows input of filing status

while status not in range(1,5):                                #check for any input outside of valid statuses
    print("Invalid input for status. Please try again.")
    status = int(input("Enter filing status:"))

income = int(input("Enter taxable income:"))      #allows input of income

#calculates taxes for brackets in status 1
if status == 1: 
    if 0 <= income <= 9875:
        tax = 0.10 * income
    elif 9876 <= income <= 40125:
        tax = 987.50 + (0.12 * (income-9875))
    elif 40126 <= income <= 85525:
        tax = 4617.50 + (0.22 * (income - 40125))
    elif 85526 <= income <= 163300:
        tax = 14605.50 + (0.24 * (income - 85525))
    elif 163301 <= income <= 207350:
        tax = 33271.50 + (0.32 * (income - 163300))
    elif 207351 <= income <= 518400:
        tax = 47367.50 + (0.35 * (income - 207350))
    elif income >= 518401:
        tax = 156235 + (0.37 * (income - 518400))
        
 #calculates taxes for brackets in status 2       
elif status == 2:
    if 0 <= income <= 19750:
        tax = 0.10 * income
    elif 19751 <= income <= 80250:
        tax = 1975 + (0.12 * (income - 19750))
    elif 80251 <= income <= 171050:
        tax = 9235 + (0.22 * (income - 80250))
    elif 171051 <= income <= 326600:
        tax = 29211 + (0.24 * (income - 171050))
    elif 326601 <= income <= 414700:
        tax = 66543 + (0.32 * (income - 326600))
    elif 414701 <= income <= 622050:
        tax = 94735 + (0.35 * (income - 414700))
    elif income >= 622051:
        tax = 167307.50 + (0.37 * (income - 622050))
        
#calculates taxes for brackets in status 3        
elif status == 3:
    if 0 <= income <= 9875:
        tax = 0.10 * income
    elif 9876 <= income <= 40125:
        tax = 98750 + (0.12 * (income - 9875))
    elif 40126 <= income <= 85525:
        tax = 4617.50 + (0.22 * (income - 40125))
    elif 85526 <= income <= 163300:
        tax = 14605.50 + (0.24 * (income - 85525))
    elif 163301 <= income <= 207350:
        tax = 33271.50 + (0.32 * (income - 163300))
    elif 207351 <= income <= 311025:
        tax = 47367.50 + (0.35 * (income - 207350))
    elif income >= 311026:
        tax = 83653.75 + (0.37 * (income - 311025))
 
  #calculates taxes for brackets in status 4      
elif status == 4:
    if 0 <= income <= 14100:
        tax = 0.10 * income
    elif 14101 <= income <= 53700:
        tax = 1410 + (0.12* (income - 14100))
    elif 53701 <= income <= 85500:
        tax = 6162 + (0.22* (income - 53700))
    elif 85501 <= income <= 163300:
        tax = 13158 + (0.24* (income - 85500))
    elif 163301 <= income <= 207350:
        tax = 31830 + (0.32* (income - 163300)) 
    elif 207351 <= income <= 518400:
        tax = 45926 + (0.35* (income - 207350))
    elif income >= 518401:
        tax = 154793.50 + (0.37* (income - 518400))

print("----------------------------------")
print('Your taxable income: $', income)  
formattedtax = float("{:.2f}".format(tax))    #sets variable for formatted taxes
print('Taxes owed: $', "{:.2f}".format(tax))   #formats tax to two decimal points
print('Income after taxes: $', (income - formattedtax))