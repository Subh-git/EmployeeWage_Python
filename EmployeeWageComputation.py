'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-02 11:30
@Title: To compute the employee wage salary.

'''
import random

#Declaring constants
Is_Absent = 0
Is_Present = 1

attendance = random.randint(0,1)

match attendance:
    case 0: 
        Is_Absent
        print("Employee is absent")
    
    case 1: 
        Is_Present
        print("Employee is present")

