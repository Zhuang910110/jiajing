total_students = 0
pass_students = 0
fail_students = 0 
total_score = 0

while True:
    score = float(input("請輸入成績（輸入-1結束）："))
    if score >= 101:
      print("不可大於100")
      continue # 跳出(本次)迴圈，進入下一迴圈
    if score == -1:
        break  # 結束
    total_students += 1
    total_score += score
    if score >= 60:
        pass_students += 1
    else:
        fail_students += 1

# 計算平均
if total_students > 0:
    average_score = total_score / total_students
else:
    average_score = 0

# 結果
print("全班人数：", total_students)
print("及格人数：", pass_students)
print("不及格人数：", fail_students)
print("全班平均成绩：", average_score)