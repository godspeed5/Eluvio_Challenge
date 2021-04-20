import numpy as np
data=[]
maxdict=dict()
for i in range(10):
    in_file = open("sample."+str(i+1), "rb") 
    data.append(in_file.read())

lendict = {len(data[i]):i for i in range(10)}

checked_strings = []
ilist = []
reqrange = list(range(10))
max_found_len = 0

# The while could be parallelized in a real worl setting
while len(reqrange)>0:
    filenum=reqrange[0]
    # print(reqrange)
    print('checking file', filenum)
    reqrange.remove(filenum)
    ilist = []
    i=max_found_len
    while (i not in ilist) and (i<=len(data[filenum])):
        c=0
        # print('in while')
        for j in range(len(data[filenum])-i+1):
            if data[filenum][j:j+i] not in checked_strings:
                checked_strings.append(data[filenum][j:j+i])
                # print(reqrange, filenum)
                
                isvalid = any([data[filenum][j:j+i] in data[k] for k in reqrange])
                if isvalid:
                    c+=1
                    while any([data[filenum][j:j+i] in data[k] for k in reqrange]) and j+i<=len(data[filenum]):
                        ilist.append(i)
                        maxdict[i] = data[filenum][j:j+i]
                        i+=1
                    i=i+j
                    break
        i+=1
        max_found_len = max(maxdict)
        max_found_string = maxdict[max(maxdict)]
        if c==0: # if the file has no matching strings of length l with any other file, it won't have any of length >l either
            break

max_found_len = max(maxdict)
max_found_string = maxdict[max(maxdict)]
print( \
    # 'Longest common string:', max_found_string, \
     '\nLongest Common String Length:', max_found_len)
cf = np.squeeze(np.where([max_found_string in data[i] for i in range(10)]))
print('Files in which the string exists: sample.{} at offset {}'.format(cf[0]+1, data[cf[0]].find(max_found_string)), 'and sample.{} at offset {}'.format(cf[1]+1, data[cf[1]].find(max_found_string)))





