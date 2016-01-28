import time
def openLog(filename, mode = 'r'):
    '''open file filename in given mode and return reference to
       opened file; also log the file access in file log.txt'''

    infile = open(filename, mode)

    # obtain current time
    now = time.localtime()
    nowFormat = time.strftime('%A %b/%d/%y %I:%M %p', now)

    # open file log.txt in append mode and append log
    outfile = open('log.txt', 'a')
    log = '{}: File {} opened.\n'                  # format string
    outfile.write(log.format(nowFormat, filename))
    outfile.close()

    return infile



##################################
# Solutions to Practice Problems #
##################################



def even(n):
    '''prints numbers between 2 and n that
     are divisible by 2 or 3'''
    for i in range(2, n+1):
        if i%2 == 0 or i%3 == 0:
            print(i, end=', ')



def roster(students):
    'prints average grade for a roster of students'
    print('Last      First     Class      Average Grade')
    for student in students:
        print('{:10}{:10}{:10}{:8.2f}'.format(student[0],
                student[1], student[2], student[3]))



def stringCount(filename, target):
    '''returns the number of occurences of string
    target in content of file filename'''
    infile = open(filename)
    content = infile.read()
    infile.close()
    return content.count(target)



def words(filename):
    'returns the list of words in file filename'
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    table = str.maketrans('!,.:;?', 6*' ')
    content = content.translate(table)
    content = content.lower()
    return content.split()



def myGrep(filename, target):
    'prints every line of file filename containing string target'
    infile = open(filename)
    for line in infile:
        if target in line:
            print(line, end='')


