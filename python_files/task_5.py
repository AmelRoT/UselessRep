import sys 
import re
s1 = "msa_cssa"
s2 = "miw_Pod"
s3 = "mMss_ss"
s4 = "ss4455_mss1"
s5 = "miiii"

p1  = re.compile(r'[a-z]+\_[a-z]+'); 

print("msa_cssa - "+ str(p1.match(s1)))
print("miw_Pod -" + str(p1.match(s2)))
print("mMss_ss - "+ str(p1.match(s3)))
print("ss4455_mss1 - "+str(p1.match(s4)))
print("miiii - "+ str(p1.match(s5)))