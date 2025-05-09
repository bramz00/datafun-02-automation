"""
File: utils_brent.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Advanced: This version requires a working .venv with loguru and pyttsx3 installed.
It includes a function to read the byline aloud using pyttsx3.

Author: Brent Ramirez

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# Learn more: https://docs.python.org/3/library/

import statistics 

# Import packages from requirements.txt
# Learn more: https://pypi.org/project/loguru/ 
# Learn more:  https://pypi.org/project/pyttsx3/
import loguru   # Easy logging
import pyttsx3  # Text-to-speech engine

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
is_profitable: bool = True

# declare an integer variable 
number_of_clients: int = 50

# declare a floating point variable
average_client_review_rating: float = 4.9

# declare a list of strings
services_offered: list = ["Data Mining", "Web Scraping", "Data Analytics"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
anonymous_employee_salaries: list = [250000, 120000, 90000, 110000]

# Calculate basic statistics using built-in Python functions and the statistics module
min_salary: float = min(anonymous_employee_salaries)  
max_salary: float = max(anonymous_employee_salaries)  
mean_salary: float = statistics.mean(anonymous_employee_salaries)  
stdev_salary: float = statistics.stdev(anonymous_employee_salaries)

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
AnaLITics -- Shining a Light on Your Data
---------------------------------------------------------
Is profitable:  {is_profitable}
Number of Clients:         {number_of_clients}
Services Offered:             {services_offered}
Average Client Review Rating: {average_client_review_rating}
Minimum Employee Salary: {min_salary}
Maximum Employee Salary: {max_salary}
Mean Employee Salary: {mean_salary:.2f}
Standard Deviation of Employee Salaries: {stdev_salary:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline


# Read the byline aloud (requires pyttsx3)

def read_byline_aloud():
    engine = pyttsx3.init()
    engine.say(get_byline())
    engine.runAndWait()


#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_case.py")
    loguru.logger.info("START main() in utils_case.py")

    print(get_byline())
    loguru.logger.info("Byline:\n" + get_byline())

    # Uncomment to hear it read aloud:
    #read_byline_aloud()

    print("END main() in utils_case.py")
    loguru.logger.info("END main() in utils_case.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()