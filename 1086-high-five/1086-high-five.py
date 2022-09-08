class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        import heapq, operator
        
        def score_group_generator():
            scores_by_id = [None] * (max(items, key=operator.itemgetter(0))[0] + 1)
            for ID, score in items:
                if scores_by_id[ID] is None:
                    scores_by_id[ID] = []
                scores_by_id[ID].append(score)
            for ID, scores in enumerate(scores_by_id):
                if not scores:
                    continue
                yield (ID, (sum(heapq.nlargest(5, scores) if len(scores) > 5 else scores)) // 5)

        return list(score_group_generator())