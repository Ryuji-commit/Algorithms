import random
import copy


# The function of decide p3 in triangle that formed p0,p1,p2
def is_p3_in_triangle(p0, p1, p2, p3):
    x_list_triangle = [p0[0], p1[0], p2[0]]
    y_list_triangle = [p0[1], p1[1], p2[1]]
    if min(x_list_triangle) < p3[0] < max(x_list_triangle):
        if min(y_list_triangle) < p3[1] < max(y_list_triangle):
            return True
    return False


# The function of slow Hull
def slow_hull(set_p):
    len_of_set_p = len(set_p)
    list_flag_of_p = [False] * len_of_set_p
    for i in range(len_of_set_p):
        p0 = set_p[i]
        for j in range(len_of_set_p):
            if i == j:
                continue
            p1 = set_p[j]
            for k in range(len_of_set_p):
                if i == k or j == k:
                    continue
                p2 = set_p[k]
                for l in range(len_of_set_p):
                    if i == l or j == l or k == l:
                        continue
                    p3 = set_p[l]
                    if is_p3_in_triangle(p0, p1, p2, p3):
                        list_flag_of_p[l] = True
    return [set_p[i] for i in range(len_of_set_p) if not list_flag_of_p[i]]


if __name__ == "__main__":
    set_p_ = [[random.randint(1, 10), random.randint(1, 10)] for _ in range(20)]
    print('集合P: {}'.format(set_p_))
    print('Slow Hull: {}'.format(slow_hull(set_p_)))
