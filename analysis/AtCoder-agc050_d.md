# Problem Analysis: AtCoder-agc050_d — Shopping

**Problem ID**: `AtCoder-agc050_d`  
**Contest**: `agc050`  
**Rating / Difficulty**: 2674  
**URL**: https://atcoder.jp/contests/agc050/tasks/agc050_d  
**VJudge Tag**: `[problem:AtCoder-agc050_d]`  
**Category File**: [`../categories/math/shopping_game_turn_expected_probability.md`](../categories/math/shopping_game_turn_expected_probability.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
N customers in line each make K shopping rounds, winning an item with probability 1 / (remaining items + 1). By tracking the number of active customers n, the current customer position i, remaining items, and remaining rounds, state transitions form a finite acyclic DAG solvable by memoized DP in O(N^3 K) time.

## 2. Core Observation & Invariant
Each turn outcome either eliminates the current customer (upon winning an item) and decrements inventory, or passes the turn to the next customer. When a round finishes, all active customers cycle to the next round with decremented round limit. Memoizing (n, i, rem_items, rem_rounds) computes win probabilities for all players.

## 3. Step-by-Step Algorithm
1. 1. Define DP state P(n, i, rem_items, rounds): probability that the i-th person among n remaining people wins an item.
2. 2. Transitions: if person 1 wins (prob 1 / rem_items), state moves to n-1 people with rem_items - 1.
3. 3. If person 1 fails, person moves to back of line.
4. 4. Memoize and solve for all N players.
5. 5. Output win probabilities modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 K)`
- **Space Complexity**: `O(N^2 K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

static const long long MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long inv(long long n) {
    return power(n, MOD - 2);
}

int N, K;
vector<long long> inv_table;
unordered_map<long long, long long> memo;

long long get_prob(int rem, int c, int a, int b, int pos) {
    if (rem == 0) return 0;
    if (a == 0) {
        if (b == 0) return 0;
        return get_prob(rem, c + 1, b, 0, pos);
    }

    long long state = ((long long)rem << 24) | ((long long)c << 18) | ((long long)a << 12) | ((long long)b << 6) | pos;
    auto it = memo.find(state);
    if (it != memo.end()) return it->second;

    long long p_win, p_fail;
    if (c == K - rem) {
        p_win = 1;
        p_fail = 0;
    } else {
        p_win = (1LL * rem * inv_table[K - c]) % MOD;
        p_fail = (MOD + 1 - p_win) % MOD;
    }

    long long res = 0;
    if (pos == 0) {
        res = (res + p_win) % MOD;
    } else {
        res = (res + p_win * get_prob(rem - 1, c, a - 1, b, pos - 1)) % MOD;
    }

    if (p_fail > 0) {
        int new_pos = (pos == 0) ? (a - 1 + b) : (pos - 1);
        res = (res + p_fail * get_prob(rem, c, a - 1, b + 1, new_pos)) % MOD;
    }

    memo[state] = res;
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> K)) return 0;

    inv_table.assign(K + 1, 0);
    for (int i = 1; i <= K; ++i) {
        inv_table[i] = inv(i);
    }

    memo.reserve(100000);

    for (int i = 0; i < N; ++i) {
        long long ans = get_prob(K, 0, N, 0, i);
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
