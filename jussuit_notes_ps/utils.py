# Utility Module

def time_check(func):
    '''
        시간 측정용 decorator
    '''
    from time import time

    def wrapper(*args, **kwargs):
        # 시간 측정 시작
        start_time = time()
        result = func(*args, **kwargs)
        # 시간 측정 종료
        end_time = time()
        # 걸린 시간 출력
        print(f"===== Time : {end_time - start_time:.4f} second 걸렸습니다! =====")

        return result

    return wrapper