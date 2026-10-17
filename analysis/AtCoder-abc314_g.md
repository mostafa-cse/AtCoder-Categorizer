# Problem Analysis: AtCoder-abc314_g — G. Amulets

**Problem ID**: `AtCoder-abc314_g`  
**Contest**: `abc314`  
**Rating / Difficulty**: 2301  
**URL**: https://atcoder.jp/contests/abc314/tasks/abc314_g  
**VJudge Tag**: `[problem:AtCoder-abc314_g]`  
**Category File**: [`../categories/basics/prefix_immunity_dual_heap.md`](../categories/basics/prefix_immunity_dual_heap.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Standard Template Library (STL)`  
- **Topic (Skill)**: `Priority Queue / Heap`  

---

## 1. Problem Statement & Key Idea
Given $N$ monsters each with type $A_i$ and attack $B_i$, and $M$ amulet slots, find the maximum prefix of monsters that can be defeated when using $k$ amulets for each $k = 0, \dots, M$.

## 2. Core Observation & Invariant
For any prefix of monsters and $k$ amulets, it is strictly optimal to grant immunity to the $k$ monster types with the largest accumulated damage in that prefix.

## 3. Step-by-Step Algorithm
1. Maintain two balanced heaps/sets partitioning monster types into the top-$k$ highest total damage and the remaining types.
2. As $k$ increases, dynamically advance the maximum defeatable prefix of monsters using two pointers.
3. Updating a monster's damage or balancing heaps takes $O(\log M)$ time per operation.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \log M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    long long H;
    if (!(cin >> N >> M >> H)) return 0;

    vector<int> A(N);
    vector<long long> B(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i] >> B[i];
    }

    // D[t] = total damage for type t
    vector<long long> D(M + 1, 0);

    set<pair<long long, int>> top_m; // (damage, type)
    set<pair<long long, int>> rest;
    for (int t = 1; t <= M; ++t) {
        rest.insert({0, t});
    }

    long long sum_top = 0;
    long long sum_total = 0;
    int m = 0;

    vector<int> ans(M + 1, 0);

    for (int k = 0; k < N; ++k) {
        int t = B[k];
        long long b = A[k];

        // Update D[t]
        pair<long long, int> old_elem = {D[t], t};
        sum_total += b;
        D[t] += b;
        pair<long long, int> new_elem = {D[t], t};

        if (top_m.count(old_elem)) {
            top_m.erase(old_elem);
            sum_top -= old_elem.first;
            top_m.insert(new_elem);
            sum_top += new_elem.first;
        } else {
            rest.erase(old_elem);
            rest.insert(new_elem);
        }

        // Maintain top_m property: min(top_m) >= max(rest)
        while (!top_m.empty() && !rest.empty() && top_m.begin()->first < rest.rbegin()->first) {
            auto from_top = *top_m.begin();
            auto from_rest = *rest.rbegin();
            top_m.erase(from_top);
            sum_top -= from_top.first;
            rest.erase(from_rest);

            top_m.insert(from_rest);
            sum_top += from_rest.first;
            rest.insert(from_top);
        }

        // While damage taken >= H, we need more amulets
        while (sum_total - sum_top >= H) {
            ans[m] = k; // with m amulets, can only defeat up to k monsters
            m++;
            if (m > M) break;
            // Move largest from rest to top_m
            auto best_rest = *rest.rbegin();
            rest.erase(best_rest);
            top_m.insert(best_rest);
            sum_top += best_rest.first;
        }
        if (m > M) break;
    }

    while (m <= M) {
        ans[m] = N;
        m++;
    }

    for (int i = 0; i <= M; ++i) {
        cout << ans[i] << (i == M ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
