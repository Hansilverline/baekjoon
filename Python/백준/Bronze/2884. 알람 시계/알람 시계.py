H , M = map(int,input().split())
if M >= 45 :
    M -= 45
elif M <45 and H >= 1 :
    H -= 1
    M = (M+60)-45
else :
    H = (H+24) -1
    M = (M+60)-45
print(f'{H} {M}')