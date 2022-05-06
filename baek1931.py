import sys
sys.stdin = open("baek1931.txt")

"""
이 문제 꼭 기억하자!
종료시간 기준으로 정렬!!!

java에서 key=lambda는
arr[i][1] 기준으로 내림차순 정렬, 같은 경우는 arr[i][1] 기준으로 내림차순 
Arrays.sort(arr, new Comparator<int[]>()) {
    @Override
    public int compare(int[] o1, int[] o2) {
        if (o1[1] == o2[1]) {
            return o1[0] - o2[0]
        } 
        return o1[1] - o2[1]
    }
}
"""


N = int(sys.stdin.readline())
CONF = [0] * N
for i in range(0, N):
    CONF[i] = list(map(int, sys.stdin.readline().split()))

# 일단 시간 정렬.
CONF.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = CONF[0][1]
idx = 0
while idx < N:
    idx += 1
    if CONF[idx][0] >= end_time:
        count += 1
        end_time = CONF[idx][1]
    if idx == N-1:
        break

print(count)