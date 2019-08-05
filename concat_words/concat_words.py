class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        memo = {}
        def canConcat(word_idx, idx, count):
            if words[word_idx][idx:] in memo and count > 1:
                return True
            
            elif idx == lengths[word_idx] and count > 1:
                return True

            end = idx
            while end < lengths[word_idx]:
                if words[word_idx][idx : end + 1] in words:
                    if canConcat(word_idx, end + 1, count + 1):
                        memo[words[word_idx][idx:]] = True
                        return True
                end += 1
            return False
        
        lengths = [len(w) for w in words]
        
        out = []
        for i in range(len(words)):
            if canConcat(i, 0, 0):
                out.append(words[i])
        return out
            