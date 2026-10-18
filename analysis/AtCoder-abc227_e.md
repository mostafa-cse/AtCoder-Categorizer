# Problem Analysis: AtCoder-abc227_e — E. Swap

**Problem ID**: `AtCoder-abc227_e`  
**Contest**: `abc227`  
**Rating / Difficulty**: 2377  
**URL**: https://atcoder.jp/contests/abc227/tasks/abc227_e  
**VJudge Tag**: `[problem:AtCoder-abc227_e]`  
**Category File**: [`../categories/dynamic_programming/multinomial_inversion_adjacent_swaps_dp.md`](../categories/dynamic_programming/multinomial_inversion_adjacent_swaps_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Count distinct strings reachable from a ternary string of characters 'K', 'E', 'Y' (|S| <= 30) using at most K adjacent swaps. Since each distinct string corresponds uniquely to the permutation preserving identical characters' relative order, state dp[cK][cE][cY][inv] tracks minimum inversions to place prefixes, running in O(|S|^5) time.

## 2. Core Observation & Invariant
Every distinct string T reachable from S corresponds uniquely to a permutation preserving identical characters' relative order. The minimum number of adjacent swaps to reach T is precisely the inversion count of this canonical permutation. State dp[cK][cE][cY][inv] tracks the number of prefixes with exact inversion count, transitioning by placing the next character and counting unplaced preceding characters.

## 3. Step-by-Step Algorithm
1. Count frequencies of 'K', 'E', 'Y' in S (|S| <= 30) and record their 0-indexed positions.
2. Initialize dp[0][0][0][0] = 1 with inv <= N(N-1)/2 <= 435.
3. For each state (i, j, k, inv), consider placing the next available character ('K', 'E', or 'Y'). The swap cost incurred is the number of already-placed characters of the other two types that originally appeared after it in S.
4. Accumulate dp transitions and sum dp[nK][nE][nY][inv] for all inv <= min(K, 435).

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|^5)`
- **Space Complexity**: `O(|S|^4)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long dp[31][31][31][450];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string S;
    long long K;
    if (!(cin >> S >> K)) return 0;
    int n = S.size();
    vector<int> posK, posE, posY;
    for (int i = 0; i < n; ++i) {
        if (S[i] == 'K') posK.push_back(i);
        else if (S[i] == 'E') posE.push_back(i);
        else posY.push_back(i);
    }
    int nK = posK.size(), nE = posE.size(), nY = posY.size();
    int max_inv = n * (n - 1) / 2;
    dp[0][0][0][0] = 1;

    for (int i = 0; i <= nK; ++i) {
        for (int j = 0; j <= nE; ++j) {
            for (int k = 0; k <= nY; ++k) {
                for (int inv = 0; inv <= max_inv; ++inv) {
                    long long cur = dp[i][j][k][inv];
                    if (!cur) continue;
                    // Try placing K
                    if (i < nK) {
                        int cost = 0;
                        for (int e = 0; e < j; ++e) if (posE[e] > posK[i]) cost++;
                        for (int y = 0; y < k; ++y) if (posY[y] > posK[i]) cost++;
                        dp[i + 1][j][k][inv + cost] += cur;
                    }
                    // Try placing E
                    if (j < nE) {
                        int cost = 0;
                        for (int kk = 0; kk < i; ++kk) if (posK[kk] > posE[j]) cost++;
                        for (int y = 0; y < k; ++y) if (posY[y] > posE[j]) cost++;
                        dp[i][j + 1][k][inv + cost] += cur;
                    }
                    // Try placing Y
                    if (k < nY) {
                        int cost = 0;
                        for (int kk = 0; kk < i; ++kk) if (posK[kk] > posY[k]) cost++;
                        for (int e = 0; e < j; ++e) if (posE[e] > posY[k]) cost++;
                        dp[i][j][k + 1][inv + cost] += cur;
                    }
                }
            }
        }
    }

    long long ans = 0;
    for (int inv = 0; inv <= min((long long)max_inv, K); ++inv) {
        ans += dp[nK][nE][nY][inv];
    }
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
