from collections import deque

def solution(bracks):
    # def right_bracket(u):
    #     # thx jungmin
    #     stack = deque([])
    #     try: 
    #         for char in u:
    #             if char == '(':
    #                 stack.append(char)
    #             else: # ')'
    #                 stack.pop()

    #     except Exception as e:
    #         return False

    #     return True

    def split_brackets(parts):
        if parts == '':
            return ''

        open_cnt = 0
        close_cnt = 0
        u_idx = len(parts) - 1

        for idx in range(len(parts)):
            if parts[idx] == '(':
                open_cnt += 1
            elif parts[idx] == ')':
                close_cnt += 1
            # else:
            #   assert False

            if open_cnt == close_cnt:
                u_idx = idx + 1
                break

        u = parts[:u_idx]
        v = parts[u_idx:]

        return u, v


    if bracks == '':
        return ''

    u, v = split_brackets(bracks)
    # rightness = right_bracket(u)
    if u[0] == '(': # THX jiye
        return u + solution(v)

    # else
    answer = '('
    answer += solution(v)
    answer += ')'


    substr = u[1:-1]
    new_u = [')' if uu == '(' else '(' for uu in u[1:-1]]
    answer += ''.join(new_u)


    return answer

if __name__ == '__main__':
    brackets = ["(()())()", ")(", "()))((()"]

    for b in brackets:
        result = solution(b)
        # print("input {}, output {}".format(b, result))