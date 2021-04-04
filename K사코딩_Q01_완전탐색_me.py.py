# 제일 마지막 예시를 통과 못 함 ㅠ ㅋㅋㅋㅋㅋ
# 모든 반복을 압축해버리는 코드. 

def solution(strs):
    N = len(strs) # 압축할 수 있는 최대 길이.

    # clen: 압축할 문자열의 길이 (compressed)
    c_results = []
    for c_len in range(1, int(N /2) + 1):
        new_strs = ''
        idx = 0

        while idx < N:
            m_idx = idx + c_len
            p_token = strs[idx:m_idx]
            n_token = strs[m_idx:m_idx + c_len]

            if p_token == n_token:
                dup_cnt = 2
                m_idx += c_len
                m_token = strs[m_idx:min(N, m_idx + c_len)]

                while p_token == m_token and m_idx + c_len <= N:
                    dup_cnt += 1
                    m_idx += c_len
                    m_token = strs[m_idx:m_idx + c_len]

                tempor = '{}{}'.format(dup_cnt, p_token)
                new_strs += tempor
                idx += dup_cnt * c_len

            else:
                new_strs += strs[idx]
                idx += 1

        c_results.append(len(new_strs))
    answer = min(c_results)
    return answer


if __name__ == "__main__":
    strss = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
    # strss = ["xababcdcdababcdcd"]
    for strs in strss:
        print("[*] strs: {}".format(strs))
        a = solution(strs)
        print(a)