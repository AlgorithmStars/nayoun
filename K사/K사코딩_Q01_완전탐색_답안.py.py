def solution(s):
    answer = len(s)

    # 정민이 말에 따르면 반복 패턴은 어차피 최장 2/len(s)지 않나 싶었는데 강사님은 이렇게...
    # 압축 단위를 늘려가며 확인
    for step in range(1, len(s)):
        compressed = ""
        prev = s[0:step] # 앞에서부터 반복 문자열이 포함되어야 한다. 
        count = 1

        # 압축 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1

            # 더 이상 압축하지 못하는 경우라면 (다른 문자열이 나왔다면)
            else:
                compressed += '{}{}'.format(count, prev) if count >= 2 else prev
                prev = s[j:j+step]
                count = 1

        # 남아있는 문자열에 대해서 처리 
        compressed += '{}{}'.format(count, prev) if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer