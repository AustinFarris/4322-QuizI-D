'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open("employee_data.csv", 'r')

reader = csv.reader(infile)

next(reader)

#create an empty dictionary
nsDict = {}

#use a loop to iterate through the csv file
for row in reader:

    #check if the employee fits the search criteria
    if row[3] == 'Marketing' and row[4] == "CSR":
        print("Manager Name: ", row[1],' ', row[2], ' Current Salary: $', format(float(row[5]), ',.2f'), sep='')
        key = row[1] + ' ' + row[2]
        new_sal = (int(row[5]) * .1) + int(row[5])
        nsDict[key] = new_sal 

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout


for i in nsDict:
    print("Manager Name: ", i, " New Salary: $", format(nsDict[i], ',.2f'), sep='')

        
    
