#!/usr/bin/python3
"""Prime Game"""


def is_winner(x, nums):
    """Return name of player that won most rounds"""

    def generate_primes(n):
        """Filters prime numbers"""
        primes = []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for p in range(2, n + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return primes

    def find_winner(n):
        """This finds the winner"""
        primes = generate_primes(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = [find_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
