N = int(input())  # кол-во событий
events = [input() for _ in range(N)]  # события

team_dict = {}
max_ = ["", 0]

for event in events:
    name, T = event.split()
    sum_ = 0
    if name not in team_dict:
        team_dict[name] = int(T)
        max_ = [name, int(T)]
    else:
        for teammate, val in team_dict.items():
            team_dict[teammate] = int(T)
            team_dict[teammate] -= sum(team_dict.values())
            print(team_dict.values())
            sum_ += sum(team_dict.values()) - max(team_dict.values())
            if team_dict[teammate] > max_[1]:
                max_[1] = team_dict[teammate]
                max_[0] = teammate
    print(*max_)
