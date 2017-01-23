from datascience import stats

# === helpers ===
def checkValues(text, valueCurrent, valueExpected):
    if valueCurrent == valueExpected:
        print (text, " OK")
    else:
        print (text, " WRONG!!, not {0} but {1}".format(valueExpected, valueCurrent))

    
# === Acceptance tests ===
# use like this: python testStats.py

X = [10.3, 4.1, 12, 15.5, 20.2, 5.5, 15.5, 4.1]
print ("===1. Test Case X1= ", X)
checkValues("mean(X1)", stats.mean(X), 10.9)
checkValues("median(X1)", stats.median(X), 11.15)
mo = stats.mode(X)
if (len(mo) == 2) and (mo[0] == 4.1) and (mo[1] == 15.5):
    print ("mode(X1) OK")
else:
    print ("mode(X1) WRONG!!, not two: 4.1 and 15.5 but {0}".format(mo))
   
checkValues("stdDev(X1)", stats.stdDev(X), 5.613)
checkValues("coeffVar(X1)", stats.coeffVar(X), 0.515)
checkValues("covariance(X1,X1)", stats.covariance(X,X), 36.003)
checkValues("correlation(X1,X1)", stats.correlation(X,X), 1)


X2 = [10, 4, 12, 15, 20, 5, 7]
print ("===2. Test Case X2= ", X2)
checkValues("mean(X2)", stats.mean(X2), 10.429)
checkValues("median(X2)", stats.median(X2), 10)
print ("mode(X2) = ", stats.mode(X2), " and shall be the entire list, sorted")
checkValues("stdDev(X2)", stats.stdDev(X2), 5.315)
checkValues("coeffVar(X2)", stats.coeffVar(X2), 0.51)


X3 = [5,10,10,10,15]
print ("===3. Test Case X3= ", X3)
print ("X3= ", X3)
mo = stats.mode(X3)
if (len(mo) == 1) and (mo[0] == 10):
    print ("mode(X3) OK")
else:
    print ("mode(X3) WRONG!!, not one mode = {0} but {1}".format(10, mo))
    
checkValues("stdDev(X3)", stats.stdDev(X3), 3.162)


X4= [1, 3, 29] 
print ("===4. Test Case X4= ", X4)
checkValues("stdDev(X4)", stats.stdDev(X4), 12.754)

X5= [1, 2, 4, 5, 8] 
print ("===5. Test Case X5= ", X5)
checkValues("stdDev(X5)", stats.stdDev(X5), 2.449)
checkValues("coeffVar(X5)", stats.coeffVar(X5), 0.612)
checkValues("covariance(X3,X5)", stats.covariance(X3,X5), 8.75)
checkValues("correlation(X3,X5)", stats.correlation(X3,X5), 0.904)


X6= [100, 200, 400, 500, 800] 
print ("===6. Test Case X6= X5*100", X6)
checkValues("stdDev(X6)", stats.stdDev(X6), 244.949) # as X5 * 100
checkValues("coeffVar(X6)", stats.coeffVar(X6), 0.612) # same as X5
checkValues("covariance(X6,X5)", stats.covariance(X6,X5), 750)
checkValues("correlation(X6,X5)", stats.correlation(X6,X5), 1)

X7 = [x + 100 for x in X5]
print ("===7. Test Case X7= X5+100 = ", X7)
checkValues("stdDev(X5 + 100)", stats.stdDev(X7), 2.449)  # same as X5
checkValues("coeffVar(X5 + 100)", stats.coeffVar(X7), 0.024) # much smaller than X5

X8 = [-1, -2, -4, -5, -8] 
print ("===8. Test Case X8 = -X5 = ", X8)
checkValues("stdDev(X8)", stats.stdDev(X8), 2.449)  # same as X5
checkValues("coeffVar(X8)", stats.coeffVar(X8), -0.612)
checkValues("covariance(X8,X5)", stats.covariance(X8,X5), -7.5)
checkValues("correlation(X8,X5)", stats.correlation(X8,X5), -1)

X9 = [6,7,15,36,39, 40, 41,42,43,47,49]
print("===9. Test case X9 (odd) = ", X9)
(lo,up) = stats.quartiles(X9)
checkValues("lower Q", lo, 15)
checkValues("upper Q", up, 43)

X10 = [7,15,36, 39,40,41]
print("===10. Test case X10 (even) = ", X10)
(lo,up) = stats.quartiles(X10)
checkValues("lower Q", lo, 15)
checkValues("upper Q", up, 40)

X11 = [7.7,15.1,36.3, 39.3,40.0,41.1]
print("===11. Test case X11 (even) = ", X11)
(lo,up) = stats.quartiles(X11)
checkValues("lower Q", lo, 15.1)
checkValues("upper Q", up, 40)

X12 = [x * 2 for x in X5]
print("===12. Test case X12 (X5 * 2) = ", X12)
checkValues("covariance(X5,X5)", stats.covariance(X5,X5), 7.5)
checkValues("covariance(X12,X5)", stats.covariance(X12,X5), 15)
