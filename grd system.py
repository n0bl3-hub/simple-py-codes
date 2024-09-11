def gradeSystem(totalscore):
    if totalscore >= 80:
        print('A class student')
    elif totalscore >= 70:
        print('B class student')
    elif totalscore >= 60:
        print('C class student')
    elif totalscore >= 50:
        print('D class student')
    elif totalscore >= 40:
        print('E class student')
    else: print('fail grade')

def valid_Score():
   print('input score')
totalscore = input()
if 0 <= totalscore <= 100:
    print(f"student got {totalscore}: {gradeSystem(totalscore)}")
else: print("invalid score input")
valid_Score()