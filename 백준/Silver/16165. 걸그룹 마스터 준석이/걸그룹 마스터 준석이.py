import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# N = 걸그룹의 수
# M = 문제의 수
girl_group = []
for _ in range(N):
    # 팀의 이름
    team_name = input().strip()
    
	# 걸그룹의 인원 수
    count_member = int(input())
	
 	# 멤버의 이름들
    members_name = []
    for _ in range(count_member):
        members_name.append(input().strip())
    members_name.sort()
#    print(members_name)
    
    girl_group.append([team_name, count_member, members_name])

for _ in range(M):
	quiz = input().strip()
	quiz_type = input().strip()
	if quiz_type == '0' :
		# 팀 이름 (트와이스)
		for i in girl_group :
				#멤버 한 줄당 한 명 출력 
			if quiz == i[0] :
				for member in i[2]:
					print(member)
				break
	elif quiz_type == '1' :
		# 멤버 이름
		for i in girl_group :
			# 팀 이름 출력
			if quiz in i[2] :
				print(i[0])
				break
