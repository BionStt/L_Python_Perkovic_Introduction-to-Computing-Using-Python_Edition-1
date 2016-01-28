__author__ = 'Rolando'
##################################################
### Perkovic Intro to Python                   ###
#### CH 4: Text Data, Files, and exceptions   ####
##### PG 124 CH 4 Case Study                 #####
##################################################

############
### 4.11 ###
############
print('PP 4.11')

""" REFERENCE
    %A == Weekday Name (Full)
    %a == Weekday Name (Abbreviated)
    %B == Month (Full)
    %b == Month (Abbreviated)
    %m == Month (Number as decimal(00 - 12))
    %d == Day (Number as decimal (00 - 31))
    %Y == Year (Full, as decimal)
    %y == Year (W/O century (00-99))
    %H == Hour (24-hr military (00-24))
    %I == Hour (12-hr standard (00-12))
    %M == Minute (Number as Decimal (00-59))
    %p == AM/PM
    %S == Seconds (Number as Decimal (00-61))
    %Z == Time zone name
"""
import time

print(time.time())
print(time.gmtime())
print(time.localtime())
print(time.strftime('%A %b/%d/%y %I:%M %p', time.localtime()))
print('\nPP 4.11')
t = time.localtime(1500000000)

# A
print(time.strftime('%A, %B, %d, %Y', t))
# B
print(time.strftime('%I:%M %p %Z on %m/%d/%Y', t))
#C
print(time.strftime('I will meet you on %a %b %d at %I:%M %p', t))


def openlog(filename, mode):
    """ Open file in given mode and return reference to opened file; also log the file access in file log.txt
    """
    infile9 = open(filename, mode)

    # Obtain current time
    now = time.localtime()
    nowformat = time.strftime('%A %b/%d/%y %I:%M %p', now)

    # Open file log.txt in append mode and append log
    outfile3 = open('log.txt', 'a')
    log = '{}: File {} opened.\n'       # Format string
    outfile3.write(log.format(nowformat, filename))
    outfile3.close()

    return infile9

print(openlog('test.txt', 'r'))