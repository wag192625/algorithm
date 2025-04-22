import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# # N = 걸그룹의 수
# # M = 문제의 수
girl_group = {}

for _ in range(N):
    # 팀 이름
    team_name = input().strip()
    # 걸그룹의 멤버 수
    count_member = int(input())
    # 멤버들의 이름
    members_name = []
    for _ in range(count_member):
        members_name.append(input().strip())
    
    girl_group[team_name] = sorted(members_name)
    
for _ in range(M) :
    quiz = input().strip()
    quiz_type = input().strip()
	# 팀 이름 (트와이스)
    if quiz_type == '0' :
		#멤버 한 줄당 한 명 출력
        print('\n'.join(girl_group[quiz]))
	# 멤버 이름
    elif quiz_type == '1' :
        for team_name, members in girl_group.items():
            if quiz in members:
                print(team_name)
                break