from operator import itemgetter
def lowest_scorer(class_record,sls):
    lowest_scorer = sorted(class_record,key=itemgetter(1))
    print(lowest_scorer)
    print(lowest_scorer[0][1])
    all_lowest_scorer = []

    print(lowest_scorer)
    for i in range (0, len(lowest_scorer)):
        if lowest_scorer[i][1] == sls:
            all_lowest_scorer.append(lowest_scorer[i][0])

    print(all_lowest_scorer)

    for ele in sorted (all_lowest_scorer):
        print(ele)
    
    
    

if __name__ == '__main__':
    class_record =[]
    grade =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record =[name,score]
        class_record.append(record)
        grade.append(score)
    
    grade = sorted(set(grade))
    second_lowest_score = grade[1]
    print("second_lowest_score :"+second_lowest_score)

    lowest_scorer(class_record,second_lowest_score)
