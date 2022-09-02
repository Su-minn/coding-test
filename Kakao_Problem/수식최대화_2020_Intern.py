# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/67257


from itertools import permutations


def solution(expression):
    # 1) 연산자 경우의 수 list 구하기    
    ops_priority = list(permutations("*+-"))
    # 2) parsing
    parsing_expression = parse_expression(expression)
    # 3) 각 경우에 따른 연산 수행하여 최솟값 계산
    max_reword = calculate_expression(ops_priority, parsing_expression)
    
    return max_reword


def calculate_expression(ops_priority, parsing_expression):
    max_award = float("-inf")
    
    for ops in ops_priority:
        temp_expression = parsing_expression.copy()

        for op in ops:
            idx = 0

            while idx < len(temp_expression):
                if temp_expression[idx] == op:
                    k = eval("".join(temp_expression[idx - 1 : idx + 2]))
                    temp_expression[idx - 1 : idx + 2] = [str(k)]
                    idx -= 1
                
                idx += 1
        
        if max_award < abs(int(temp_expression[0])):
            max_award = abs(int(temp_expression[0]))
    
    return max_award


def parse_expression(expression):
    parsing_expression = []
    
    start = 0
    for idx, ch in enumerate(expression):
        if ch in "*+-":
            parsing_expression.extend([expression[start:idx], expression[idx]])
            start = idx + 1

    parsing_expression.append(expression[start:])
    
    return parsing_expression
