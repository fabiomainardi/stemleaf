# read a sequence of integers from text file and display a stem-leaf plot, with d digits for the leaves
# and m padding spaces on the left
def stemleaf(filename,d,m):
    import sys
    f = open(filename,'r')
    # read file to string
    s = ""
    while 1:
        line = f.readline()
        if not line:
            break
        s += line
    f.close()
    # convert string to oredered list of ints
    data=list(s.split(' '))
    data = map(int, data)
    data = sorted(data)
    stems=[]
    leaves=[]  
    for n in data:
        st=str(n)
        if(len(st)==d):
            prefix='0'
            suffix=st
        else:
            prefix=st[0:-d]
            suffix=st[-d:]
        if(prefix in stems):
            sys.stdout.write(' '+suffix)
        else:
            print("")
            sys.stdout.write(prefix.rjust(m)+' ⎢ '+ suffix)
            sys.stdout.flush()
        stems.append(prefix)
        leaves.append(suffix)
        