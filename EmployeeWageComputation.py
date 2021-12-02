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
Days_In_Month = 20
Max_Working_Hour = 100


def check_attendance():
    '''
    Description: Checks the employee attendace and returns the employee houras per the attendace.
    '''
    attendance = random.randint(0,2)
    match attendance:
        case 0: 
            #print("Employee is absent")
            emp_hour = 0
            return emp_hour
        
        case 1: 
            #print("Employee is present")
            emp_hour = 8
            return emp_hour
        
        case 2:
            #print("Employee is part time")
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

#for monthly calculation of employee wage.
def calc_monthly_wage():
    '''
    Description: This function calculates the monthly wages.
    Returns: The monthly wage.
    '''
    n = 0
    total_wage = 0
    total_hours = 0

    while (n < Days_In_Month and total_hours < Max_Working_Hour ):
        daily_wg = calc_daily_wage()
        total_wage+= daily_wg
        #we have to improvise by obtaining the daily hour by dividing daily wage by wage per hour.
        #else we will get error in matching monthly wage and total hours.
        total_hours+= int(daily_wg/20)   
        n+=1

    print("The number of days is:",n)
    print("Total hours:",total_hours)
    return total_wage




if __name__ == '__main__':
    print("The monthly wage is:",calc_monthly_wage())

    
