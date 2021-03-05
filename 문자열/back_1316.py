num = int(input())
group_num = 0
for i in range(num):
    str_dict = {}
    string = input()

    before_str = ' '

    is_group = True
    for alpha in string:  # 한 글자씩 비교
        if alpha in str_dict:  # 알파벳이 딕셔너리에 있을 경우
            if alpha == before_str:  # 이전 글자와 같을 경우
                continue
            else:  # 이전 글자와 다른 경우
                is_group = False
                break
        else:
            str_dict[alpha] = 0
            before_str = alpha

    if is_group:
        group_num += 1

print(group_num)