now_hh,now_mm,now_ss  = map(int,input().split(':'))
base_hh,base_mm,base_ss = map(int,input().split(':'))

time = ( base_hh*3600+base_mm*60+base_ss ) - ( now_hh*3600+now_mm*60+now_ss )

if time < 0 :
    time += 60*60*24

hh = time//3600

mm = (time%3600)//60

ss = time%60

print("%02d:%02d:%02d" % (hh, mm, ss))