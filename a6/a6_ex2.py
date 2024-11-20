from typing import List, Set, Tuple

def power_set(L: List) -> Set[Tuple]:
    L = sorted(L)
    result = set()
    
    def recursive_helper(index: int, current_subset: List):
        if index == len(L):
            result.add(tuple(current_subset))
            return
        
        recursive_helper(index + 1, current_subset)
        recursive_helper(index + 1, current_subset + [L[index]])
    
    recursive_helper(0, [])
    return result

print("result:", power_set([]))
print("result:", power_set([3, 1, 2]))
print("result:", power_set(['c', 'a', 'b']))