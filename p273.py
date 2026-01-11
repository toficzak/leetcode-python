import unittest
from typing import List


class P273:
    def canFinishIterative(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        # 0 = unvisited, 1 = visiting, 2 = done
        state = [0] * numCourses

        for start in range(numCourses):
            if state[start] != 0:
                continue

            stack = [(start, 0)]

            while stack:
                node, phase = stack.pop()

                if phase == 0:
                    if state[node] == 1:
                        return False
                    if state[node] == 2:
                        continue

                    state[node] = 1
                    stack.append((node, 1))

                    for nei in graph[node]:
                        stack.append((nei, 0))
                else:
                    state[node] = 2
        return True


class Test(unittest.TestCase):
    testcases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (6, [[1, 0], [1, 2], [3, 1], [3, 2], [2, 4], [4, 5], [2, 5]], True)
    ]

    def test(self):
        for numCourses, prerequisites, expected in self.testcases:
            with self.subTest(f"{numCourses}:{prerequisites} "):
                result = P273().canFinishIterative(numCourses, prerequisites)
                self.assertEqual(expected, result)
