def double(y):
    x=2
    print('x = {}, y = {}'.format(x,y))
    return x*y



def readAge(filename):
    '''converts first line of file filename to
       an integer and prints it'''
    try:
        infile = open(filename)
        strAge = infile.readline()
        age = int(strAge)
        print('age is',age)
    except IOError:
        # executed only if an IOError exception is raised
        print('Input/Output error.')
    except ValueError:
        # executed only if a ValueError exception is raised
        print('Value cannot be converted to integer.')
    except:
        # executed if an exception other than IOError
        # or ValueError is raised
        print('Other error.')



##################################
# Solutions to Practice Problems #
##################################



def safe_open(filename, mode):
    'returns handle to opened file filename, or None if error occurred'
    try:
        # try block
        infile = open(filename, mode)
        return infile
    except:
        # except block
        return None


