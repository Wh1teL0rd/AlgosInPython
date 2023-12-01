def min_eating_speed(piles, h):
    def can_eat_all(piles, k, h):
        hours_needed = 0
        for pile in piles:
            hours_needed += (pile + k - 1) // k
        return hours_needed <= h

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if can_eat_all(piles, mid, h):
            right = mid
        else:
            left = mid + 1

    return left
