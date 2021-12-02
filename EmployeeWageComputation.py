'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-02 11:30
@Title: To compute the employee wage salary.

'''
import random

#Declaring constants
Is_Absent = 0
Is_Present = 1


def check_attendance():
    '''
    Description: Checks the employee attendace.
    '''
    attendance = random.randint(0,1)
    match attendance:
        case 0: 
            print("Employee is absent")
            return Is_Absent
        
        case 1: 
            print("Employee is present")
            return Is_Present

def calc_daily_wage():
    '''
    Description: This function calculates the daily employee wage.
    Returns: The daily wage.
    '''
    wage_per_hour = 20
    full_day_hour = 8

    if (check_attendance() == Is_Present):
        daily_wage = wage_per_hour * full_day_hour
    
    else:
        daily_wage = 0
    
    return daily_wage



if __name__ == '__main__':
    print(calc_daily_wage())

    
