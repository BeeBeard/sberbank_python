import re


# 1 Задание
def open_test_file():
    #  Дополнительная функция для тестирования
    with open("test_data.txt", encoding="utf-8") as file:
        text_data = file.read()
    return text_data


def solution_problem_1(input_text: str = None) -> [str, None]:
    # использую zfill для добавления необходимого количества нулей
    def add_num(match):
        s1, s2 = match.group().split("\\")
        return f"{s1.zfill(4)}\\{s2.zfill(5)}"
    return re.sub(r"(\d{2,4}\\\d{2,5})", add_num, input_text)


if __name__ == '__main__':
    text = open_test_file()
    result = solution_problem_1(input_text=text)
    print(text)
    print(result)
