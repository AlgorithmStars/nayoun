import numpy as np


# Special THX... Jeongmin + Jiye 210425
def rotate_key(key, angle):
    key_T = key.T
    n_key = None
    if angle == 0:
        return key

    if angle == 90:
        n_key = np.flip(key_T, axis=1)
    elif angle == 180:
        n_key = np.flip(key, axis=1)
        n_key = np.flip(n_key, axis=0)
    elif angle == 270 or angle == -90:
        n_key = np.flip(key_T, axis=0)

    return n_key


def solution(key, lock):
    N = len(lock); M  = len(key)
    NN = N + 2 * M
    lock = np.array(lock); key = np.array(key)


    new_lock = np.zeros((NN, NN))
    new_lock = np.array(new_lock)
    new_lock[M:N + M, M: N + M] = lock

    angles = [0, 90, 180, 270]
    answer = False
    for angle in angles:
        cur_key = rotate_key(key, angle)

        for ridx in range(NN - M):
            for cidx in range(NN - M):

                new_lock[ridx:ridx + M, cidx:cidx + M] += cur_key
                # if np.sum(new_lock[M:N + M, M: N + M]) == N ** 2:
                if np.all(new_lock[M:N + M, M: N + M] == 1):
                    answer = True
                    break

                print("--")
                print(new_lock[M:N + M, M: N + M])
                print("angle: {}, rdix: {}, cidx: {}, ".format(angle, ridx, cidx))

                new_lock[ridx:ridx + M, cidx:cidx + M] -= cur_key


    return answer


if __name__ == '__main__':
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    answer = solution(key, lock)
    print(answer)