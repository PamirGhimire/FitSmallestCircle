import sys, getopt

def _parseArgs(argv):
    useStubData = False
    useExternalImpl = True

    stubArg = ""
    implArg = ""
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["useStubData=","useExternalImpl="])
    except getopt.GetoptError:
        print ('usage : start.py --useStubData <true/false> --useExternalImpl <true/false>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('usage : start.py --useStubData <true/false> --useExternalImpl <true/false>')
            sys.exit()
        elif opt in ("--useStubData"):
            stubArg = arg
        elif opt in ("--useExternalImpl"):
            implArg = arg

    validArgs = ["true", "false", ""]
    if(stubArg in validArgs and implArg in validArgs):
        if stubArg=="true":
            useStubData = True
        if implArg=="false":
            useExternalImpl = False        
    else:
        print ('usage : start.py --useStubData <true/false> --useExternalImpl <true/false>')
        sys.exit(2)

    return useStubData, useExternalImpl