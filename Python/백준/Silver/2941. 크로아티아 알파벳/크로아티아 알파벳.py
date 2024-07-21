str_ = input()
count = 0 
kro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in kro : 
    if i in str_ : 
        str_ = str_.replace(i,'a')

print(len(str_))