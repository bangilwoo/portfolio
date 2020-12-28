import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int: # N은 노드의 수, K: 도착점, 기본적인 구조 셋팅
        graph = collections.defaultdict(list) # collections: 컨테이너(객체)동일한 값을 파악, defaultdict: 딕셔너리 형식으로 변경
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
            # print(graph[u]) # 딕셔너리 형으로 변환을 확인

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, K)]
        dist = collections.defaultdict(int)
        print(Q)

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q) # heapq.heappop: heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1