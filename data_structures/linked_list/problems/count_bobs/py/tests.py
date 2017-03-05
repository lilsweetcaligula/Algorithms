#
# Tests adapted from:
# [href.] https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015

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
        #
        # See: [href.] # [href.] https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015
        # PSET 1, Week 2
        #
        ARGS_EXPECTED_PAIRS = (
            ((LinkedList.ConvertArrayToLinkedList('bbobbobobbyoobobo'), ), 4, ),
            ((LinkedList.ConvertArrayToLinkedList('otobooobfbobbxgjbobbypbobboboo'), ), 4),
            ((LinkedList.ConvertArrayToLinkedList('bobbobbbmtobobobobqjcobbobobobobobooxobobobob'), ), 13),
            ((LinkedList.ConvertArrayToLinkedList('obobebobobobobbobbbooboo'), ), 6, ),
            ((LinkedList.ConvertArrayToLinkedList('obobobobooboobbobbxobob'), ), 5, ),
            ((LinkedList.ConvertArrayToLinkedList('obobohgbbdo'), ), 1, ),
            ((LinkedList.ConvertArrayToLinkedList('bbohbobbuobobbobbooobobhboboosbobbboboboobooboboo'), ), 9, ),
            ((LinkedList.ConvertArrayToLinkedList('rntjrssjy'), ), 0, ),
            ((LinkedList.ConvertArrayToLinkedList('bobobobobobobobobob'), ), 9, ),
            ((LinkedList.ConvertArrayToLinkedList('bobobohbboobobob'), ), 4, ),
            ((LinkedList.ConvertArrayToLinkedList('bobbbobobbobbaobobo'), ), 5, ),
            ((LinkedList.ConvertArrayToLinkedList('oboobobobrboobrgbobobbobobrubobb'), ), 7, ),
            ((LinkedList.ConvertArrayToLinkedList('bobbbbobqoboboobobobobohudbu'), ), 6, ),
            ((LinkedList.ConvertArrayToLinkedList('mcbbobboboboobobbobobxbobobczobobobobobboob'), ), 12, ),
            ((LinkedList.ConvertArrayToLinkedList('bobbzrobgbobbrbbobobbobdcobobobo'), ), 7, ),
            ((LinkedList.ConvertArrayToLinkedList('boobobooobobbobobbrbobboboooboooboboboboboor'), ), 10, ),
            ((LinkedList.ConvertArrayToLinkedList('boobozobhobobobodnobobobioboboboboobbobb'), ), 8, ),
            ((LinkedList.ConvertArrayToLinkedList('bouobobbobooboo'), ), 2, ),
            ((LinkedList.ConvertArrayToLinkedList('cbobbebobbirvoo'), ), 2, ),
            ((LinkedList.ConvertArrayToLinkedList('obobobufbob'), ), 3, ),
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
    TestMain(solution.CountBobs)
