import QuantLib as Ql

date = Ql.Date(31,3,2015)
print(date)

effective_date = Ql.Date(1,1,2015)
termination_date = Ql.Date(1,1,2016)
tenor = Ql.Period(Ql.Monthly)
