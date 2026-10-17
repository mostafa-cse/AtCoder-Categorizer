# Problem Analysis: AtCoder-arc138_c — Rotate and Play Game

**Problem ID**: `AtCoder-arc138_c`  
**Contest**: `arc138`  
**Rating / Difficulty**: 1728  
**URL**: https://atcoder.jp/contests/arc138/tasks/arc138_c  
**VJudge Tag**: `[problem:AtCoder-arc138_c]`  
**Category File**: [`../categories/game_theory/raneys_lemma_circular_game.md`](../categories/game_theory/raneys_lemma_circular_game.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Raney's Lemma / Cyclic Shifts`  
- **Topic (Skill)**: `Raney's Lemma / Circular Prefix Balance on 2-Player Game`  

---

## 1. Problem Statement & Key Idea
Given an even-length array A of size N. You choose a cyclic shift k of A. Then Takahashi and Aoki play a game where in each turn Takahashi takes an element and Aoki deletes an element. Maximize Takahashi's score and find the shift k.

**Key Insight**: Assign +1 to the N/2 largest elements of A and -1 to the N/2 smallest elements. By Raney's Lemma, there is a cyclic shift where every prefix sum is strictly positive (or non-negative), allowing Takahashi to guarantee obtaining all N/2 largest elements.

## 2. Core Observation & Invariant
Find the index where prefix sum of the (+1/-1) array is minimized. Shifting to start immediately after this minimum index guarantees all prefix sums stay >= 0.

## 3. Step-by-Step Algorithm
1. Sort copy of A to find threshold value separating N/2 largest from smallest.
2. Assign B[i] = +1 if A[i] is in top N/2, else -1.
3. Compute prefix sums of B. Find index min_i with the minimum prefix sum.
4. Optimal shift is k = (min_i + 1) % N.
5. Max score is sum of the N/2 largest elements.
6. Print k and max_score.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, int>> a(n);
    long long total_top = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i].first;
        a[i].second = i;
    }

    sort(a.rbegin(), a.rend());

    vector<int> b(n, -1);
    for (int i = 0; i < n / 2; ++i) {
        b[a[i].second] = 1;
        total_top += a[i].first;
    }

    int min_pref = 0;
    int min_idx = -1;
    int cur_pref = 0;

    for (int i = 0; i < n; ++i) {
        cur_pref += b[i];
        if (cur_pref < min_pref) {
            min_pref = cur_pref;
            min_idx = i;
        }
    }

    int k = (min_idx + 1) % n;
    cout << k << " " << total_top << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Application of Raney's Lemma to guarantee positive prefix sums in circular two-player selection games.
- **Reusable Pattern**: `Circular Prefix Balance (Raney's Lemma): Shift array to start at min prefix sum + 1.`
