# Problem Analysis: AtCoder-abc179_e — Sequence Sum

**Problem ID**: `AtCoder-abc179_e`  
**Contest**: `abc179`  
**Rating / Difficulty**: 1175  
**URL**: https://atcoder.jp/contests/abc179/tasks/abc179_e  
**VJudge Tag**: `[problem:AtCoder-abc179_e]`  
**Category File**: [`../categories/math/periodic_orbit_prefix_sum.md`](../categories/math/periodic_orbit_prefix_sum.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Cycle Detection`  
- **Topic (Skill)**: `Periodic Orbit Prefix Sum Acceleration`  

---

## 1. Problem Statement & Key Idea
Given A_1 = X and A_{n+1} = A_n^2 mod M. Compute sum_{i=1}^N A_i for N <= 10^12, M <= 10^5.

**Key Idea**: Because M <= 10^5, the sequence has only M possible values and must enter a periodic cycle within M steps.

## 2. Core Observation & Invariant
Track the first visit step of each value in visited[val]. Once a value repeats at step cur with previous visit at step prev: the cycle length is L = cur - prev. Divide remaining steps into full cycles and a partial remainder, computing the sum in O(M).

## 3. Step-by-Step Algorithm
1. Store visited step of each value: visited array initialized to -1.
2. Record values in sequence order: seq vector.
3. While cur <= N: if visited[val] != -1, cycle detected! Break.
4. Compute prefix sum before cycle, cycle sum, multiply by (rem_steps / L), and add tail remainder.
5. Print total sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, x, m;
    if (!(cin >> n >> x >> m)) return 0;

    vector<int> visited(m, -1);
    vector<long long> seq;

    long long cur = x;
    int step = 0;

    while (step < n && visited[cur] == -1) {
        visited[cur] = step;
        seq.push_back(cur);
        cur = (cur * cur) % m;
        step++;
    }

    if (step == n) {
        long long total = 0;
        for (long long v : seq) total += v;
        cout << total << "\n";
        return 0;
    }

    int start_cycle = visited[cur];
    int cycle_len = step - start_cycle;

    long long total = 0;
    for (int i = 0; i < start_cycle; ++i) {
        total += seq[i];
    }

    long long cycle_sum = 0;
    for (int i = start_cycle; i < step; ++i) {
        cycle_sum += seq[i];
    }

    long long remaining_steps = n - start_cycle;
    total += (remaining_steps / cycle_len) * cycle_sum;

    long long tail = remaining_steps % cycle_len;
    for (int i = 0; i < tail; ++i) {
        total += seq[start_cycle + i];
    }

    cout << total << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Cycle detection on finite state orbits with full cycle quotient multiplication.
- **Reusable Pattern**: `Finite orbit sum: prefix_sum + (rem / L) * cycle_sum + remainder_sum.`
