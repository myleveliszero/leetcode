def firstBadVersion(n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = left + (right-left)//2
        is_bad = isBadVersion(mid)
        if is_bad:
            right = mid
        else:
            left = mid+1
    