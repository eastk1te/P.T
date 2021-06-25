participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]


'''
def solution_1(participant, completion): #정확성 50, 효율성 0
    if len(set(participant)) == len(set(completion)): #set은 중복없는 리스트
        for i in participant:
            pc = participant.count(i)
            cc = completion.count(i)
            if (pc >= 2) & (pc != cc):
                answer = i
            else:
                continue
    else:
        for i in participant:
            if i not in completion:
                answer = i
            else:
                continue

    return answer

def solution_2(participant, completion): #정확성 50, 효율성 0

    for i in participant:

        if participant.count(i) > completion.count(i):
            answer = i
            
        else:
            if i not in completion:
                answer = i
            else:
                continue

    return answer



def solution_3(participant, completion): #정확성 50, 효율성 0

    for i in participant:
        if participant.count(i) > completion.count(i):
            answer = i


    return answer


def solution_4(participant, completion): #정확성 50, 효율성 0

    for i in set(participant):
        if i not in completion:
            answer = i
        else:
            if participant.count(i) == 1:
                continue
            else:
                if participant.count(i) > completion.count(i):
                    answer = i
                else:
                    continue


    return answer


def solution_5(participant, completion): #정확성 50, 효율성 0
    for i in range(len(completion)):
        participant.remove(completion[i])

    answer = participant[0]

    return answer
    
'''

def solution(participant, completion): #정확성 50, 효율성 50
    participant.sort()
    completion.sort()
    answer = 0

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            continue

    if answer == 0:
        answer = participant[-1]

    return answer

a = solution(participant, completion)
print(a)

