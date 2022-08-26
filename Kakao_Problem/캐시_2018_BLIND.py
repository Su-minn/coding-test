# 문제 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/17680


def solution(cacheSize, cities):
    lru = LRUCache(cacheSize)

    for city in cities:
        case_insensitive_city = city.lower()
        lru.use_cache(case_insensitive_city)

    return lru.run_time


class LRUCache:
    def __init__(self, max_size: int):
        self.cache = {}
        self.max_size = max_size
        self.run_time = 0

    def use_cache(self, element: str):
        if element in self.cache:
            self.__get(element)
        else:
            self.__put(element)

    def __get(self, element: str):
        self.run_time += 1
        self.__move_to_end(element)

    def __put(self, element: str):
        self.run_time += 5

        if self.max_size == 0:
            return

        if self.__is_full():
            del self.cache[next(iter(self.cache))]

        self.cache[element] = True

    def __is_full(self):
        return len(self.cache) == self.max_size

    def __move_to_end(self, element: str):
        value = self.cache.pop(element)
        self.cache[element] = value
