from typing import List, Set, Tuple

def power_set(L: List) -> Set[Tuple]:
    L = sorted(L)
    result = set()
    
    def subset(i: int, p_subset: List):
        if i == len(L):
            result.add(tuple(p_subset))
            return
        
        subset(i + 1, p_subset)
        subset(i + 1, p_subset + [L[i]])
    
    subset(0, [])
    return result


if __name__ == '__main__':
    print("result:", power_set([]))
    print("result:", power_set([3, 1, 2]))
    print("result:", power_set(['c', 'a', 'b']))