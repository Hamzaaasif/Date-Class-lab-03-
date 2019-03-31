class date():
  def __init__(self,day,month,year):
    self.myday=day
    self.mymonth=month
    self.myyear=year
    print("DATE :"+str(self.myday)+':'+str(self.mymonth)+':'+str(self.myyear))
  @classmethod

  def numofdays(self,day,month,year):
    if month==1 or month==3 or month==5 or month==7 or month==9 or month==11:
      print("NUMBER OF DAYS:THIS MONTH IS CONSIST OF 30 DAYS")
    else:
      print("NUMBER OF DAYS:THIS MONTH CONSIST OF 31 DAYS")  
  
  
  def isleapyear(self,day,month,year):
        if year%4==0  or year%400==0 and year*100!=0:
         print("LEAP YEAR : ITS A LEAP YEAR ,CONSISTING 29 DAYS OF FEBURARY "+str(self.myday)+':'+str(self.mymonth)+':'+str(self.myyear))    
        if month==2:
          print('NUMBER OF DAYS : THIS MONTH CONSIST OF 29 DAYS ')

  def adddays(self,days):
     self.mydays=days+self.myday
     print(" AFTER ADDING DAYS NEW DATE IS =" +str(self.mydays)+':'+str(self.mymonth)+':'+str(self.myyear))

  def subdays(self,days):
     self.mydays=days-self.myday
     print(" AFTER SUBTRACTING DAYS NEW DATE IS =" +str(self.mydays)+':'+str(self.mymonth)+':'+str(self.myyear))  
     
obj=date(24,5,2001)
obj.numofdays(24,5,2016)
obj.isleapyear(24,1,2016)
obj.adddays(3)
obj.subdays(4)