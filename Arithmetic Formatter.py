# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:48:52 2024

@author: jlove
"""

import re


def arithmetic_arranger(problems, show_answers=False):
    
    pattern = re.compile(r'(\d+)\s([-+*/])\s(\d+)')
    digit_pattern1 = re.compile(r'\D+\s([-+*/])\s')
    digit_pattern2 = re.compile(r'\d+\D+\s([-+*/])\s')
    digit_pattern3 = re.compile(r'\D+\d+\s([-+*/])\s')
    digit_pattern4 = re.compile(r'\d+\s([-+*/])\s\D+')
    digit_pattern5 = re.compile(r'\d+\s([-+*/])\s\d+\D+')
    number_listA =[]
    number_listB =[]
    operator_list=[]
    resualt_list=[]
    #check problem limit
    if len(problems)>5:
       return 'Error: Too many problems.'
      
    #creat problem list    
    for problem in (problems):
        #check digits
        if digit_pattern1.findall(problem):
            return 'Error: Numbers must only contain digits.'
        elif digit_pattern2.findall(problem):
            return 'Error: Numbers must only contain digits.'
        elif digit_pattern3.findall(problem):
            return 'Error: Numbers must only contain digits.'
        elif digit_pattern4.findall(problem):
            return 'Error: Numbers must only contain digits.'
        elif digit_pattern5.findall(problem):
            return 'Error: Numbers must only contain digits.'
        
        matches = pattern.findall(problem)
        for match in(matches):
            numA = match[0]
            operator = match[1]
            numB = match[2]
            #check operator without * or /
            if match[1]=='*' or match[1]=='/':
                return "Error: Operator must be '+' or '-'."
            #check only 4 digits
            if len(numA)>4 or len(numB)>4:
                return 'Error: Numbers cannot be more than four digits.'
        
            
            number_listA.append(numA)
            operator_list.append(operator)
            number_listB.append(numB)
            if operator =='+':
                resualt_list.append(int(numA)+int(numB))
            else:
                resualt_list.append(int(numA)-int(numB))
    #print answer
    arranged_problems = ""

    # arrange problems
    for i in range(len(problems)):
        width = max(len(number_listA[i]), len(number_listB[i])) + 2
        arranged_problems += f"{number_listA[i]:>{width}}    "
    arranged_problems  = arranged_problems.rstrip()
            
    arranged_problems += "\n"

    for i in range(len(problems)):
        width = max(len(number_listA[i]), len(number_listB[i]))
        arranged_problems += f"{operator_list[i]} {number_listB[i]:>{width}}    "
    arranged_problems  = arranged_problems.rstrip()
    arranged_problems += "\n"

    for i in range(len(problems)):
        width = max(len(number_listA[i]), len(number_listB[i]))+2
        arranged_problems += f"{'-' * (width)}    "
    arranged_problems  = arranged_problems.rstrip()
    arranged_problems += "\n"
    
    if show_answers:
        for i in range(len(problems)):
            width = max(len(number_listA[i]), len(number_listB[i]))+2
            arranged_problems += f"{resualt_list[i]:>{width}}    "
    arranged_problems  = arranged_problems.rstrip()
    return arranged_problems

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
arithmetic_arranger(["1 + 2", "1 - 9380"])
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["3 + 855", "988 + 40"], True)
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
