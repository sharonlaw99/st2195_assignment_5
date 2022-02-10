# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:10:47 2022

@author: Thunderobot
"""

def is_divisible_by_k(x, k):
  '''
  Checks whether x is divisible by k.
  '''
  try:
      return(x%k == 0)                                    #1
  except:
      return("Wrong input")
  
'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000 (excluding doubles)
'''
int_list = []                                                #2
for i in range(1001):                                        #3
  if (is_divisible_by_k(i, 2) | is_divisible_by_k(i, 5) | is_divisible_by_k(i, 7)):       #4,5,6
      int_list.append(i)
  else :                                                     #7
      pass

'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000 (excluding doubles)
'''
sum(int_list)                                                #8

##Notes:
#range(1000): from 0 to 999

##Changes:
#1:changed assert to return, such that the outcome is of Boolean type (used for functions later)
#2:changed () to [] - a list to store integers and changed x into 'int_list' (name with some meaning)
#3:changed '1000' to '1001' because we want the loop to run from 0 to 1000
#4:changed x into i (for the loop)
#5:changed & to | (and to or)
#6:moved 'is_divisible_by_k(x, 7):' up one line and changed the brackets to put all 3 conditions together
#7:added 'else: pass' for a more complete code (optional, but useful if want to add else action afterwards)
#8:sum(x) to sum(int_list)

