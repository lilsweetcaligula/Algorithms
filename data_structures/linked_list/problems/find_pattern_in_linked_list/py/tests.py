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
        ARGS_EXPECTED_PAIRS = (
            # Both lists are null.
            (
                (LinkedList.ConvertArrayToLinkedList(), 
                 LinkedList.ConvertArrayToLinkedList(), ),
                 -1
            ),

            # Pattern is null.
            (
                (LinkedList.ConvertArrayToLinkedList('hay'),       
                 LinkedList.ConvertArrayToLinkedList(), ),           
                 -1
            ),

            # Source is null.
            (
                (LinkedList.ConvertArrayToLinkedList(),            
                 LinkedList.ConvertArrayToLinkedList('hay'), ),      
                 -1
            ),

             # Needle longer than the haystack.
            (
                (LinkedList.ConvertArrayToLinkedList('ha'),        
                 LinkedList.ConvertArrayToLinkedList('hay'), ),      
                 -1
            ),

             # Needle not in the haystack.
            (
                (LinkedList.ConvertArrayToLinkedList('haystack'),  
                 LinkedList.ConvertArrayToLinkedList('needle'), ),   
                 -1
            ),

            # Needle not in the haystack.
            (
                (LinkedList.ConvertArrayToLinkedList('stack'),     
                 LinkedList.ConvertArrayToLinkedList('queue'), ),    
                 -1
            ),

            # Needle equal to the haystack.
            (
                (LinkedList.ConvertArrayToLinkedList('hay'),       
                 LinkedList.ConvertArrayToLinkedList('hay'), ),      
                 0
            ),

            (
                (LinkedList.ConvertArrayToLinkedList('hhhay'),     
                 LinkedList.ConvertArrayToLinkedList('hay'), ),       
                 2
            ),
            (
                (LinkedList.ConvertArrayToLinkedList('saynay'),    
                 LinkedList.ConvertArrayToLinkedList('nay'), ),       
                 3
            ),
            (
                (LinkedList.ConvertArrayToLinkedList('deck'),      
                 LinkedList.ConvertArrayToLinkedList('eck'), ),       
                 1
            ),
            (
                (LinkedList.ConvertArrayToLinkedList('y'),         
                 LinkedList.ConvertArrayToLinkedList('y'), ),         
                 0
            ),
            (
                (LinkedList.ConvertArrayToLinkedList('hay'),       
                 LinkedList.ConvertArrayToLinkedList('h'), ),         
                 0
            ),
            (
                (LinkedList.ConvertArrayToLinkedList('bobob'),     
                 LinkedList.ConvertArrayToLinkedList('bob'), ),       
                 0
            ),
            (
                (LinkedList.ConvertArrayToLinkedList('loloroflo'), 
                 LinkedList.ConvertArrayToLinkedList('loro'), ),      
                 2
            ),

            # Needle at the beginning.
            (
                (LinkedList.ConvertArrayToLinkedList('foobar'), 
                 LinkedList.ConvertArrayToLinkedList('fo'), ),      
                 0
            ),

            # Needle in the ending.
            (
                (LinkedList.ConvertArrayToLinkedList('foobar'), 
                 LinkedList.ConvertArrayToLinkedList('ar'), ),      
                 4
            ),

            # See: [href.] http://stackoverflow.com/questions/3134602/what-are-good-test-cases-for-benchmarking-stress-testing-substring-search-algo
            #
            # src = 'aabaabaabaabaabaabaab'
            # pat = 'aaab'
            #            
            (
                (LinkedList.ConvertArrayToLinkedList('aabaabaabaabaabaabaab'), 
                 LinkedList.ConvertArrayToLinkedList('aaab'), ),      
                 -1
            ),

            # See: [href.] http://stackoverflow.com/questions/3134602/what-are-good-test-cases-for-benchmarking-stress-testing-substring-search-algo
            #
            # src = 'yxyxyxxyxyxyxx'
            # pat = 'yxyxyxxyxyxyxy'
            #          
            (
                (LinkedList.ConvertArrayToLinkedList('yxyxyxxyxyxyxx'), 
                 LinkedList.ConvertArrayToLinkedList('yxyxyxxyxyxyxy'), ),      
                 -1
            ),
        )

        areAllPassed = True
        failedCount  = 0
        passedCount  = 0

        for testId, argsExpectedPair in enumerate(ARGS_EXPECTED_PAIRS):
            args, expected = argsExpectedPair
            actual         = sol(*args)
            isPassed       = expected == actual
            
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
    TestMain(solution.FindPatternInLinkedList)
