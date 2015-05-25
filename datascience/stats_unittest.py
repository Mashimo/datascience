import unittest
import stats

# === Unit tests for stats ===
# use like this: python stats_unittest.py

class statsTest(unittest.TestCase):

    def SetUp(self):
        # put here all the initializations
        pass
        
    # mean
        
    def testEmptyMean(self):
            # passing empty list to mean() must raise exception
        Z = []
        self.assertRaises(TypeError, stats.mean, *Z)
        
    def testSingleMean(self):
            # passing only one data point to mean() must return the same value
        self.assertEqual(stats.mean([25]), 25)
        
    def testDefaultPrecisionMean(self):
        X = [10, 4, 12, 15, 20, 5, 7]
        self.assertEqual(stats.mean(X), 10.429)

    def testOtherPrecisionMean(self):
        X = [10, 4, 12, 15, 20, 5, 7]
        self.assertEqual(stats.mean(X,4), 10.4286)

    # median
        
    def testEmptyMedian(self):
            # passing empty list to median() must raise exception
        Z = []
        self.assertRaises(TypeError, stats.mean, *Z)

    def testSingleMedian(self):
            # passing only one data point to median() must return the same value
        self.assertEqual(stats.median([7]), 7)
        
    # mode

    def testEmptyMode(self):
            # passing empty list to mode() must raise exception
        Z = []
        self.assertRaises(TypeError, stats.mode, *Z)

    def testSingleMode(self):
            # passing only one data point to mode() must return a list with that value
        self.assertEqual(stats.mode([25.7]), [25.7])
        
    # standard deviation

    def testEmptyStdDev(self):
            # passing empty list to stdDev() must raise exception
        Z = []
        self.assertRaises(TypeError, stats.stdDev, *Z)
      
    def testSingleStdDev(self):
            # passing only one data point to stdDev() must return zero (no deviation!)
        self.assertEqual(stats.stdDev([5]), 0.0)
          
    def testDefaultPrecisionStdDev(self):
        X = [1, 2, -2, 4, -3]
        self.assertEqual(stats.stdDev(X), 2.577)

    def testOtherPrecisionStdDev(self):
        X = [1, 2, -2, 4, -3]
        self.assertEqual(stats.stdDev(X,4), 2.5768)

    # coefficient of variation

    def testEmptyCoeffVar(self):
            # passing empty list must raise exception
        Z = []
        self.assertRaises(TypeError, stats.coeffVar, *Z)

    def testZeroMeanCoeffVar(self):
            # passing mixed list with mean=0 must raise exception
        Z = [-3,0,3]
        self.assertRaises(TypeError, stats.coeffVar, *Z)

    def testSingleCoeffVar(self):
            # passing only one data point must return zero (no deviation!)
        self.assertEqual(stats.coeffVar([5]), 0.0)
          
    def testDefaultPrecisionCV(self):
        X = [1, 2, 2, 4, 3]
        self.assertEqual(stats.coeffVar(X), 0.425)

    def testOtherPrecisionCV(self):
        X = [1, 2, 2, 4, 3]
        self.assertEqual(stats.coeffVar(X,5), 0.42492)

    # range
    
    def testRange(self):
                # passing empty list must raise exception
        Z = []
        self.assertRaises(TypeError, stats.range, *Z)
        
    def testSingleRange(self):
            # passing only one data point must return zero
        self.assertEqual(stats.range([5]), 0)        
        
    def testNoRange(self):
            # passing two equal data points must return zero
        self.assertEqual(stats.range([5.3,5.3]), 0.0)
      
if __name__ == "__main__":
    unittest.main()