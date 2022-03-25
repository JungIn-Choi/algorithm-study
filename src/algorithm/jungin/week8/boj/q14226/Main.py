from collections import deque
s = int(input())
dp = [[-1 for _ in range(s+1)] for _ in range(s+1)]
queue = deque()
queue.append((1,0))
dp[1][0] = 0
while queue:
    num, clip = queue.popleft()
    if dp[num][num] == -1:
        dp[num][num] = dp[num][clip] + 1
        queue.append((num, num))
    if num+clip <= s and dp[num+clip][clip] == -1:
        dp[num+clip][clip] = dp[num][clip] + 1
        queue.append((num+clip, clip))
    if num-1 >= 0 and dp[num-1][clip] == -1:
        dp[num-1][clip] = dp[num][clip] + 1
        queue.append((num-1, clip))
answer = -1
for i in range(s+1):
    if  dp[s][i] != -1:
        if answer == -1 or dp[s][i] < answer:
            answer = dp[s][i]
print(answer)