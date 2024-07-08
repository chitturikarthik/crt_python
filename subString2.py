def isPresent(s1,s2):
    j=0
    for i in range(len(s1)):
        if s1[i]==s2[j]:
            j+=1
        if len(s2)==j:
            return True

s1="NAVESEREKER"
s2="SRKR"
if isPresent(s1,s2):
    print("YES")