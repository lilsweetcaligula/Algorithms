# The solution should pass all tests present in this module.
#
# All tester functions should follow the TestMain signature
# and be added inside the TESTS tuple inside the TestMain
# function.

import sys
import LinkedList
import solution

FP_RATIO_PREC = 2
# The number of digits of precision in the values representing 
# the passed/failed ratio to the total number of tests.

# Tests for the "Convert a number to a linked list" problem.

def TestMain(sol, log=sys.stdout, doNotLogPassed=True) -> bool:
    """
    @param sol:             the function to be tested.
    @param log:             a stream or a file to log the tester output to.
    @param doNotLogPassed:  if True, all successful tests will not be logged.
    @return:                True if all tests in the TESTS array were successful, False otherwise.

    All tester functions should follow the signature
    of the TestMain function.
    """
  
    def TestPredefined(sol, log, doNotLogPassed=True):
        ARGS_EXPECTED_PAIRS = (
            ((0,),          LinkedList.ConvertArrayToLinkedList([0])),
            ((1,),          LinkedList.ConvertArrayToLinkedList([1])),
            ((19,),         LinkedList.ConvertArrayToLinkedList([1,9])),
            ((21,),         LinkedList.ConvertArrayToLinkedList([2,1])),
            ((99,),         LinkedList.ConvertArrayToLinkedList([9,9])),
            ((100,),        LinkedList.ConvertArrayToLinkedList([1,0,0])),
            ((123,),        LinkedList.ConvertArrayToLinkedList([1,2,3])),
            ((999,),        LinkedList.ConvertArrayToLinkedList([9,9,9])),
            ((1000,),       LinkedList.ConvertArrayToLinkedList([1,0,0,0])),
            ((99999,),      LinkedList.ConvertArrayToLinkedList([9,9,9,9,9])),
            ((100000,),     LinkedList.ConvertArrayToLinkedList([1,0,0,0,0,0])),
            ((123456,),     LinkedList.ConvertArrayToLinkedList([1,2,3,4,5,6])),
            ((134678,),     LinkedList.ConvertArrayToLinkedList([1,3,4,6,7,8])),
            ((341592,),     LinkedList.ConvertArrayToLinkedList([3,4,1,5,9,2])),
            ((1000000,),    LinkedList.ConvertArrayToLinkedList([1,0,0,0,0,0,0])),
            ((9999999,),    LinkedList.ConvertArrayToLinkedList([9,9,9,9,9,9,9])),
            ((99999999,),   LinkedList.ConvertArrayToLinkedList([9,9,9,9,9,9,9,9])),
        )

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
    TestMain(solution.ConvertPositiveNumToLinkedList)
