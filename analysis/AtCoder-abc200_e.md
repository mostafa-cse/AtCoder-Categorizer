# Problem Analysis: AtCoder-abc200_e — Patisserie ABC 2

**Problem ID**: `AtCoder-abc200_e`  
**Contest**: `abc200`  
**Rating / Difficulty**: 1955  
**URL**: https://atcoder.jp/contests/abc200/tasks/abc200_e  
**VJudge Tag**: `[problem:AtCoder-abc200_e]`  
**Category File**: [`../categories/combinatorics/lexicographical_kth_triplet_bounded_sum.md`](../categories/combinatorics/lexicographical_kth_triplet_bounded_sum.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion-Exclusion / Stars and Bars`  
- **Topic (Skill)**: `Lexicographical K-th Triplet Selection under Bounded Sum via Stars and Bars Bounding`  

---

## 1. Problem Statement & Key Idea
Cakes have 3 integer beauty attributes (i, j, k) in [1, N]. They are sorted by sum S = i + j + k ascending, then i ascending, then j ascending. Find the K-th cake.

For a fixed sum S in [3, 3N], the number of integer solutions to i + j + k = S with 1 <= i, j, k <= N is computed via stars-and-bars with inclusion-exclusion: binom(S - 1, 2) - 3*binom(S - 1 - N, 2) + 3*binom(S - 1 - 2N, 2). Subtract counts to identify the exact sum S containing the K-th cake. Then iterate i in [1, N]; the number of pairs (j, k) with j + k = S - i and 1 <= j, k <= N is the length of interval [max(1, S - i - N), min(N, S - i - 1)]. Subtract to locate i, then j, then k = S - i - j.

## 2. Core Observation & Invariant
Stars-and-bars with inclusion-exclusion gives O(1) count for sum S, reducing search space to O(N).

## 3. Step-by-Step Algorithm
1. Compute ways(S) for S = 3..3N using inclusion-exclusion.
2. Find exact sum S containing K by subtracting ways(S).
3. For each candidate i in 1..N:
4.   rem = S - i. Compute count of j in [1, N] such that 1 <= rem - j <= N.
5.   If count >= K: commit to i, break. Else: K -= count.
6. Find j by adding min_j + K - 1. Set k = S - i - j.
7. Print i, j, k.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

long long C2(long long n) {
    if (n < 2) return 0;
    return n * (n - 1) / 2;
}

long long count_triplets(long long S, long long N) {
    long long ans = C2(S - 1);
    if (S - 1 - N >= 2) ans -= 3 * C2(S - 1 - N);
    if (S - 1 - 2 * N >= 2) ans += 3 * C2(S - 1 - 2 * N);
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    long long target_s = -1;
    for (long long s = 3; s <= 3 * n; ++s) {
        long long ways = count_triplets(s, n);
        if (k <= ways) {
            target_s = s;
            break;
        }
        k -= ways;
    }

    long long ans_i = -1, ans_j = -1, ans_k = -1;

    for (long long i = 1; i <= n; ++i) {
        long long rem = target_s - i;
        long long low_j = max(1LL, rem - n);
        long long high_j = min(n, rem - 1);

        if (low_j <= high_j) {
            long long ways = high_j - low_j + 1;
            if (k <= ways) {
                ans_i = i;
                ans_j = low_j + k - 1;
                ans_k = target_s - ans_i - ans_j;
                break;
            }
            k -= ways;
        }
    }

    cout << ans_i << " " << ans_j << " " << ans_k << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multi-variable bounded sum counting via stars-and-bars with lexicographical rank extraction.
- **Reusable Pattern**: `Lexicographical K-th Triplet: Identify sum bucket via stars-and-bars, identify first element, deduce remainder.`
