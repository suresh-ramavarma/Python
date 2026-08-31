#slice string and convert to float
str = 'X-DSPAM-Confidence:0.8475'
colpos=str.find(':')
strnum=str[colpos+1:]
print(strnum)
print(float(strnum))
