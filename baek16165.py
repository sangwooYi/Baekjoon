import sys
sys.stdin = open("baek16165.txt")


team_member_dict = {}
member_team_dict = {}

N, M = map(int, input().split())

for i in range(0, N):
    team_name = input()
    member_cnt = int(input())
    team_member_dict[team_name] = [0] * member_cnt

    for j in range(0, member_cnt):
        member = input()
        # 팀_멤버 dict 에는 member저장
        # 멤버_팀 dict에는 team명 저장
        team_member_dict[team_name][j] = member
        member_team_dict[member] = team_name
    team_member_dict[team_name].sort()


for i in range(0, M):
    cur_quiz = input()
    oper = int(input())

    # 팀에속한 멤버 사전순
    if oper == 0:  
        members = team_member_dict[cur_quiz]

        for member in members:
            print(member)
    # 멤버가 속한 팀
    else:
        print(member_team_dict[cur_quiz])