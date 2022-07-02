# GBP coin denominations in pennies
coins = [1, 2, 5, 10, 20, 50, 100, 200]


def split(n, coins):
    """
    How many ways we can reach the value n using
    the sum of any combination of the given coins

    It works, but lots of pruning of the search space
    possible!
    """

    if len(coins) == 0:
        # Base case where we have no coins left
        return 0

    # Consider the lowest coin in the list, and
    # find how many times it divides the desired
    # amount, to get the upper bound of how many
    # of this coin we can choose
    c0 = coins[0]
    upper_bound = n // c0

    count = 0

    # Loop through all `alloc` allocations of how many
    # times we could choose this coin, up to the upper bound
    # and sum up the `count` of how many ways
    for alloc in range(0, upper_bound + 1):
        cost = alloc * c0
        rest = n - cost

        if rest == 0:
            # Base case where we've exactly reached the desired
            # amount by using `alloc` coins of denomination `c0`
            count += 1
        else:
            # Recurse, finding how we can split the remanining amount
            # of money with the larger coins after choosing `alloc`
            # of coin `c0`
            count += split(rest, coins[1:])

    return count


print(split(200, coins))
