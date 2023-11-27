from datetime import date
import brownianMotion
import scraper

def dayDistanceCal(targetDate1,targetDate2):
    delta = -1
    delta = targetDate2-targetDate1
    return delta.days

# Convert input to float type
# Input Name
# p0=current Price,
# v=Historical Volatility,
# p1=target Price 1
# p2 = targetPrice2
# t1 = target Time 1, set to 1 if we want to calculate from current date
# t2 = target Time 2
# Remark : p1 = p2 if you only set one price target

# Input
p0 =scraper.lastPrice
v = float(scraper.hv)
p1 =float(19400.0)
p2 =float(19400.0)
t1 =float(1)


p0 = float(p0)
v = float(v)
p1 = float(p1)
p2 = float(p2)
t1 = float(t1)


targetDate1 = date.today()
targetDate2=  date(2024,1,28)
t2 = dayDistanceCal(targetDate1,targetDate2)
t2 = float(t2*24)
print("Num of Hours between targetDate2 and targetDate1 :",t2)


result =  (brownianMotion.probabilitytouch(p0,v,p1,p2,t1,t2))
probOfTouch = float((result[0]+result[2]+result[4])*100)
print("Probability of Touch:",probOfTouch,"%")
