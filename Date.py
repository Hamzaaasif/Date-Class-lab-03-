class date:
  #***constructor***
  def __init__(self,day,month,year):
    self.day=day
    self.month=month
    self.year=year
    #***Set day
  def setday(self,day):
    self.day=day
    #***Set month
  def setmonth(self,month):
    self.month=month
    #***Set year
  def setyear(self,year):
    self.year=year
  #***Get day
  def retday(self):
    return self.day
    #***Get month
  def retmonth(self):
    return self.month
    #***Get year
  def retyear(self):
    return self.year
    #***check for leap year**
  def  isLeapYear(self,year):
    if self.year % 4==0:
      print("This is a leap year")
    else:
      print("This is not a leap year")
   #**Number of days in a month***  
  def NumberOfDays(self,month):
    self.months=['jan','march','may','july','august','oct','dec']
    if month in self.months:
      return 31
    elif month=='feb':
      return 28
    else:
      return 30
   #***For display Date***
  def displaydate(self):
    print("Date :",self.retday(),"-",self.retmonth(),"-",self.retyear())
    #**For add days in a month***
  def adddate(self,adddays,months):
    adddays=self.retday()+adddays
    self.currdays=self.NumberOfDays(self.retmonth())
    if self.currdays>=adddays:
      self.setday(adddays)
    else:
      adddays=adddays-self.currdays 
      self.setmonth(months[months.index(self.retmonth())+1])
      self.setday(adddays)
     #***for subtract days in a month***
  def subdate(self,subdays,months):
    subdays=self.retday()-subdays
    if subdays <= 0:
      self.setmonth(months[months.index(self.retmonth())-1])
      self.currdays=self.NumberOfDays(self.retmonth())
      subdays=self.currdays+subdays
      self.setday(subdays)
    else:
      self.setday(subdays)


if __name__ == "__main__":
  months=['jan','feb','march','april','may','june','july','august','september','oct','november','dec']
  Date=date(24,'march',2019)
  Date.displaydate()
  Date.isLeapYear(2019)
  print("Total Days :",Date.NumberOfDays('dec'))
  Date.adddate(20,months)
  Date.displaydate()
  Date.subdate(20,months)
  Date.displaydate()