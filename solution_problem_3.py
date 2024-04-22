# 3 Задание
def solution_problem_3(list_of_str):
    return int(''.join(sorted(list_of_str, key=lambda x: x*3, reverse=True)))


if __name__ == '__main__':

    los = ["41", "4", "005", "89"]
    result = solution_problem_3(los)
    print(result)
