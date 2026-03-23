from collections import defaultdict, Counter

def group_anagrams(strs: list[str]) -> list[list[str]]:

    result = defaultdict(list)
    for word in strs:
        st = frozenset(Counter(word).items())
        result[st].append(word)
    return list(result.values())
