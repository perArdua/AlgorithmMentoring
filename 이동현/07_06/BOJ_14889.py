
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
stat_table = [list(MIS()) for _ in range(n)]

stat_difference = float('inf')

team_start = []
team_link = []
entire = set(range(n))
temp = {}
start_stat = 0
link_stat = 0
def select():
    global stat_difference
    global team_link
    if len(team_start) == n//2:
        temp = set(team_start)
        team_link = list(entire - temp)
        stat_difference = min(stat_difference, calc(team_start, team_link))
        return None
    for i in range(n):
        if i in team_start:
            continue
        team_start.append(i)
        select()
        team_start.pop()

def calc(team1, team2):
    sum_start = 0
    sum_link = 0 
    for i in range(len(team1)):
        for j in range(len(team1)):
            if i == j:
                continue
            sum_start += stat_table[team1[i]][team1[j]]
            sum_link += stat_table[team2[i]][team2[j]]
    return abs(sum_start - sum_link)

select()
print(stat_difference)