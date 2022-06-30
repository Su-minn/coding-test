## 문제 : 프로그래머스 2022 KAKAO BLIND RECRUITMENT - 신고 결과 받기
## 링크 : https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3

## 풀이
### - 입력 : id_list (2 <= id_list <= 1,000) / report (1 <= report <= 200,000) / k (1 <= k <= 200)
### - 출력 : 각 유저가 받은 결과 메일 수 (id_list에 담긴 id 순)
### - 시간 제한 : 10초 (정확성)
### - Key Points
###   : 1) 필요한 data를 적절한 자료구조에 분리하여 저장
###   : 2) 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리하는 제약 사항에 유의
###   : 3) 서로 다른 자료 구조의 교집합(겹치는 원소)을 구할 때는 집합(set) 자료형의 교집합(intersection) 메서드를 사용하면 효율적 (Vs. 리스트 이중 for 문)


## Sol 1) id_list는 최대 1,000개인 반면, report는 최대 200,000개이므로, id_list를 기준으로 data를 저장하고 서칭하는 것이 효율적
from typing import List, Dict


def get_report_dict(id_list: List[str], report: List[str]) -> Dict:
    user_report_dict = {id : [] for id in id_list}
    report_id_count_dict = {id : 0 for id in id_list}
    
    for report_case in set(report):
        user_id, report_id = report_case.split()
        user_report_dict[user_id].append(report_id)
        report_id_count_dict[report_id] += 1
    return user_report_dict, report_id_count_dict


def get_ban_email_list(user_report_dict: Dict, ban_id_list: List) -> List:
    ban_email_list = []
    
    for key, val in user_report_dict.items():
        count = len(set(val).intersection(ban_id_list))
        ban_email_list.append(count)
    return ban_email_list


def solution(id_list: List[str], report: List[str], k: int) -> List:
    user_report_dict, report_id_count_dict = get_report_dict(id_list, report)
    ban_id_list = [key for key, val in report_id_count_dict.items() if val >= k]
    answer = get_ban_email_list(user_report_dict, ban_id_list)
    return answer


## Sol 2) code는 더 짧지만, report(최대 200,000개) List에 두 번 반복문을 돌면서 시간상으로는 더 비효율적인 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    return answer