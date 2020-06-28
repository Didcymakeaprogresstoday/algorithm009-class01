from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = Counter(tasks)
        nbucket = dic.most_common(1)[0][1] #桶的个数为需要执行最多次的任务的次数
        last_bucket = list(dic.values()).count(nbucket) #最后一个桶中还有的任务数的个数 等于要执行次数最多次的任务的个数
        res = (nbucket - 1) * (n + 1) + last_bucket
        return max(res, len(tasks))