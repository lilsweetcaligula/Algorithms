import sys
import LinkedList
import solution

FP_RATIO_PREC = 2
# The number of digits of precision in the values representing 
# the passed/failed ratio to the total number of tests.

def TestMain(sol, log=sys.stdout, doNotLogPassed=True) -> bool:
    """
    @param sol:             the function to be tested.
    @param log:             a stream or a file to log the tester output to.
    @param doNotLogPassed:  if True, all successful tests will not be logged.
    @return:                True if all tests in the TESTS array were successful, False otherwise.

    All tester functions should follow the signature
    of the TestMain function.
    """
  
    def TestPredefined(sol, log, doNotLogPassed=True) -> bool:
        class ArgsExpectedPairCollection:
            def __init__(self, count=120, minLen=1, maxLen=15, minVal=-9, maxVal=9):
                self.count  = count
                self.minLen = minLen
                self.maxLen = maxLen
                self.minVal = minVal
                self.maxVal = maxVal
                
            def __len__(self):
                return self.count

            def __iter__(self):
                import random

                for _ in range(self.count):
                    listLen  = random.randint(self.minLen, self.maxLen)
                    m        = random.randint(1, listLen)
                    n        = random.randint(0, listLen)

                    values   = [random.randint(self.minVal, self.maxVal) for _ in range(listLen)]
                    expected = []

                    i        = 0

                    while i < len(values):
                        j = 0

                        while i < len(values) and j < m:
                            expected.append(values[i])
                            i += 1
                            j += 1

                        j = 0

                        while i < len(values) and j < n:
                            i += 1
                            j += 1

                    values   = LinkedList.ConvertArrayToLinkedList(values)
                    expected = LinkedList.ConvertArrayToLinkedList(expected)
                
                    yield ((values, n, m), expected)

        ARGS_EXPECTED_PAIRS = ArgsExpectedPairCollection()

        areAllPassed = True
        failedCount  = 0
        passedCount  = 0

        for testId, argsExpectedPair in enumerate(ARGS_EXPECTED_PAIRS):
            args, expected = argsExpectedPair
            actual         = sol(*args)
            isPassed       = LinkedList.Equals(expected, actual)
            
            if not(isPassed and doNotLogPassed):
                print('Test #{}'.format(testId),                             file=log)
                print('Args: ({})'.format(', '.join(map(str, args))),        file=log)
                print('Expected: {}'.format(expected),                       file=log)
                print('Actual: {}'.format(actual),                           file=log)
                print('{}'.format('OK' if expected == actual else 'FAILED'), file=log)
                print(                                                       file=log)
            
            if not isPassed:
                failedCount  += 1
                areAllPassed  = False
            else:
                passedCount  += 1
        
        passedRatio = passedCount / len(ARGS_EXPECTED_PAIRS)
        failedRatio = failedCount / len(ARGS_EXPECTED_PAIRS)

        print('Passed: {}, %{:.{prec}f}'.format(passedCount, 100.0 * passedRatio, prec=FP_RATIO_PREC), file=log)
        print('Failed: {}, %{:.{prec}f}'.format(failedCount, 100.0 * failedRatio, prec=FP_RATIO_PREC), file=log)

        return areAllPassed
    
    # Please add all tester functions to the TESTS tuple.
    TESTS        = (TestPredefined, )
    areAllPassed = True

    for Test in TESTS:
        if not Test(sol, log):
            areAllPassed = False

    return areAllPassed

if __name__ == '__main__':
    TestMain(solution.DeleteNAfterMNodes)
