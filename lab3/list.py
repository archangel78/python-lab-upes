score_list = []
no_scores = int(input("Enter number of scores: "))

for i in range(0,no_scores):
    score = int(input("Enter score "+str(i+1)+": "))
    score_list.append(score)

highest_score = max(score_list)
runner_up = min(score_list)

for score in score_list:
    if(highest_score>score>runner_up):
        runner_up = score

print("\nRunner up is "+str(runner_up))