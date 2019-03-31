class date:

  def __init__(self,day,month,year):
    self.day = day
    self.month = month
    self.year = year
    
  def SetDay(self,day):
    self.day=day
    
  def SetMonth(self,month):
    self.month=month
  
  def ReturnDay(self):
    return self.day
  
  def ReturnMonth(self):
    return self.month
  
  def ReturnYear(self):
    return self.year
    
  def  isLeapYear(self,year):
    if self.year % 4==0:
      print(year ,"is a Leap year")
    else:
      print(year,"is not a leap year")
     
  def NumberOfDays(self,month):
    self.months=['January','March','May','July','August','October','December']
    if month in self.months:
      return 31
    elif month=='February':
      return 28
    else:
      return 30
   
  def printDate(self):
    print("Date :",self.ReturnDay(),self.ReturnMonth(),self.ReturnYear())
   
  def AddinaDate(self,newdays,months):
    newdays=self.ReturnDay()+newdays
    self.CurrentMonthDays=self.NumberOfDays(self.ReturnMonth())
    if self.CurrentMonthDays>=newdays:
      self.SetDay(newdays)
    else:
      newdays=newdays-self.CurrentMonthDays 
      self.SetMonth(months[months.index(self.ReturnMonth())+1])
      self.SetDay(newdays)
     
  def SubInaDate(self,newdays,months):
    newdays=self.ReturnDay()-newdays
    if newdays <= 0:
      self.SetMonth(months[months.index(self.ReturnMonth())-1])
      self.CurrentMonthDays=self.NumberOfDays(self.ReturnMonth())
      newdays=self.CurrentMonthDays+newdays
      self.SetDay(newdays)
    else:
      self.SetDay(newdays)


if __name__ == "__main__":
  months=['January','February','March','April','May','June','July','August','September','October','November','December']
  Date=date(24,'March',2019)
  Date.printDate()
  Date.isLeapYear(2019)
  print("Total Days :",Date.NumberOfDays('December'))
  Date.AddinaDate(20,months)
  Date.printDate()
  Date.SubInaDate(20,months)
  Date.printDate()