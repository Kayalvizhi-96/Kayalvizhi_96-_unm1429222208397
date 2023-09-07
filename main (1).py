# leapyear
"""
year%4==0&
year%100!=0/
year%400==0
'''
def is leap year(year):
 if(year%4==0 and year%100!=0) or year%400==0:
 return true
 else:
  return false
  year=2012
  if isleapyear(year):
  print('{} is not a leapyaer.'format(year))