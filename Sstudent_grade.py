score = int(input("Enter a score"))
result = ""
if score > 90 and score  <= 100:
    result = "Distinction"
elif score >= 80 and score < 90:
    result = "Excellent"
elif score >= 70 and score < 80:
    result = "B Grade"
elif score >= 60 and score < 70:
    result = "C Grade"
elif score >= 50 and score < 60:
    result = "D Grade"
else:
    result = "Come back later"
ans = f'your score is {score}\n and your result is {result}'
print(ans)
#print(f'your score is {score}\n and your result is {result}')




