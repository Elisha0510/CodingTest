import sys
num = list(map(int, sys.stdin.readline().strip().split()))

map_1 = []
for i in range(num[0]):
    map_1.append(list(sys.stdin.readline().strip()))

map_compare_1 = []
map_compare_2 = []
for y in range(8):
    m_1 = []
    m_2 = []
    for x in range(8):
        if y%2 and x%2:
            m_1.append('W')
            m_2.append('B')
        elif y%2 and not x%2:
            m_1.append('B')
            m_2.append('W')
        elif not y%2 and x%2:
            m_1.append('B')
            m_2.append('W')
        elif not y%2 and not x%2:
            m_1.append('W')
            m_2.append('B')
    map_compare_1.append(m_1)
    map_compare_2.append(m_2)

def compare(x, y, map_1):

    cnt = [0,0]
    for i in range(8):
        for j in range(8):
            if map_1[i+y][j+x] != map_compare_1[i][j]:
                cnt[0] += 1
            elif map_1[i+y][j+x] != map_compare_2[i][j]:
                cnt[1] += 1
    
    return cnt

count = []
for y in range(num[0] - 7):
    for x in range(num[1] - 7):
        return_cnt = compare(x, y, map_1)
        count += return_cnt

print(min(count))