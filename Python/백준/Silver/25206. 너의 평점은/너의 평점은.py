grade_std = [('A+',4.5),('A0',4.0),('B+',3.5),('B0',3.0),('C+',2.5),('C0',2.0),('D+',1.5),('D0',1.0),('F',0.0)]
full_score = 0.0
hakjum = 0
score_grade = []

for i in range(20) :
    a,b,c = input().split()
    score_grade.append((float(b),c))
    # (4.0 'A'=4.5)

for each_ in score_grade :
    for g in grade_std :
        if each_[1] == 'P':
            break
        elif each_[1] == g[0] :
            full_score += (each_[0] * g[1])
            hakjum += each_[0]
            break 

print(full_score/hakjum)