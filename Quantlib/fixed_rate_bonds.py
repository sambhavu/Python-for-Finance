#GouthamBalaraman @gsbalaraman
#******************************

import QuantLib as ql 
todaysDate = ql.Date(15,1,2015)
ql.Settings.instance().evaluationDate = todaysDate 
spotDates = [ql.Date(15,1,2015), ql.Date(15,7,2015), ql.Date(15,1,2016)]
spotRates = [0.0,0.005, 0.007]
dayCount = ql.Thirty360()
calendar = ql.UnitedStates()
interpolation = ql.Linear()
compounding = ql.Compounded
compoundingFreqeuncy = ql.Annual 
spotCurve = ql.ZeroCurve(spotdates, spotRates, dayCount, calendar, interpolation, 
                  compounding, compoundingFrequency)
spotCurveHandle = ql.YieldTermStructureHandle(spotCurve) 

issueDate = ql.Date(15,1,2015)
maturityDate = ql.Date(15,1,2016)
tenor = ql.Period(ql.Semiannual) 
calendar = ql.UnitedStates()
businessConvention = ql.Unadjusted
dateGeneration = ql.DateGeneration.Backward
montEnd = False 
schedule = ql.Schedule(issueDate, maturityDate, tenor, calendar, businessConvention, 
                  businessConvention, dateGeneration, monthEnd)
dayCount = ql.Thirty360()
couponRate - .06
coupons = [couponRate]

settlementDates = 0
faceValue = 100
fixedRateBond = ql.FixedRateBond(settlementDays, faceValue, schedule, coupons, dayCount)

fixedRateBOnd.NPV()

#105.2765399

