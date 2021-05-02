# 강의의 정답 코드

import re 
# bisect_left(a, x): a라는 리스트에 x라는 원소를 삽입할 가장 왼쪽 위치
# bisect_right(a, x): a라는 리스트에 x라는 원소를 삽입할 가장 왼쪽 위치
from bisect import bisect_left, bisect_right

# 값이 특정 범위에 속하는 데이터의 개수 구하기 
def count_by_range(a, lv, rv):
    ri = bisect_right(a, rv)
    li = bisect_left(a, lv)
    return ri - li # 값이 [lv, rv]인 데이터의 개수를 반환하는 함수


# words를 길이별로 나눠서 저장하기 위한 리스트
data = [[] for _ in range(10001)]
# 와일드카드가 쿼리의 앞에 있을 경우르 ㄹ위해 reverse한 words 길이별 리스트
reversed_data = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        data[len(word)] = append(word)
        reversed_data[len(word)].append(word[::-1])

    for i in range(10001):
        data[i].sort()
        reversed_data[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(data[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_data[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))

    answer.append(res)
return answer

