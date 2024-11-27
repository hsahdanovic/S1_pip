def permute(s: str) -> set[str]:
    if len(s) == 0:
        return {""}

    permutations = set()
    for i, ii in enumerate(s):
        rest = s[:i] + s[i + 1:]
        for p in permute(rest):
            permutations.add(ii + p)
    return permutations

if __name__ == '__main__':
    print(permute(''))
    print(permute('a'))
    print(permute('ab'))
    print(permute('abc'))