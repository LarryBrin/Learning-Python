string = 'X-DSPAM-Confidence: 0.8475'
result = float(string[string.find('0'):])
print result
