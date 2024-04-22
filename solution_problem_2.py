# 2 задание
def solution_problem_2(n, k, *args):

    def get_l_to_change():  # Проверяем, какие пути не стоит изменять, т.к. они не повлияют на результат
        for d, i in enumerate(sorted_list):
            short_list = sorted_list[0:n - d]
            k1 = sum(short_list) / (len(short_list) + 1 + k)
            if k1 < short_list[-1]:
                return short_list
        return sorted_list

    def split_space(space):  # разделяем длинные пути на короткие
        return [round(space / d_map[space], 1) for i in range(d_map[space])]

    d_map = {i: 1 for i in args}

    sorted_list = [i for i in args]
    sorted_list.sort(reverse=True)

    l_to_change = get_l_to_change()
    l_to_change.sort()

    c = 0
    for i in range(k):  # Добавляем коэффициенты деления путей
        c = 0 if c >= len(l_to_change) - 1 else c + 1
        d_map[l_to_change[c]] += 1

    result = []
    [result.extend(split_space(space)) for space in d_map]
    return result


if __name__ == '__main__':

    n = 5
    k = 3
    L = 100, 30, 20, 80
    result = solution_problem_2(n, k, *L)
    print(result)

