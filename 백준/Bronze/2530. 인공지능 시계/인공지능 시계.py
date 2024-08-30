hh, mm, ss = map(int,input().split())
time = int(input())

hh += time // (60*60)
time = time % (60*60)

mm += (time // 60)
time = time % 60

ss += time

if ss > 59 :
    mm += (ss // 60)
    ss = ss % 60

if mm > 59 :
    hh += (mm // 60)
    mm = mm % 60

if hh > 23 :
    hh = hh % 24

print(hh,mm,ss)
