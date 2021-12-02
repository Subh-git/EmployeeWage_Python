'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-02 11:30
@Title: To compute the employee emp_hour salary.

'''
import random

#Declaring constants
Is_Absent = 0
Is_Present = 1
Is_PartTime = 2


def check_attendance():
    '''
    Description: Checks the employee attendace and returns the employee houras per the attendace.
    '''
    attendance = random.randint(0,2)
    match attendance:
        case 0: 
            print("Employee is absent")
            emp_hour = 0
            return emp_hour
        
        case 1: 
            print("Employee is present")
            emp_hour = 8
            return emp_hour
        
        case 2:
            print("Employee is part time")
            emp_hour = 4
            return emp_hour

def calc_daily_wage():
    '''
    Description: This function calculates the daily employee emp_hour.
    Returns: The daily emp wage.
    '''
    wage_per_hour = 20
    hours = check_attendance()
    daily_wage = hours * wage_per_hour
    return daily_wage





if __name__ == '__main__':
    print(calc_daily_wage())

    
