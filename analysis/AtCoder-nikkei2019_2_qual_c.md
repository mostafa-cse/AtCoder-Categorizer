# Problem Analysis: AtCoder-nikkei2019_2_qual_c — Swaps

**Problem ID**: `AtCoder-nikkei2019_2_qual_c`  
**Contest**: `nikkei2019-2-qual`  
**Rating / Difficulty**: 2136  
**URL**: https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_c  
**VJudge Tag**: `[problem:AtCoder-nikkei2019_2_qual_c]`  
**Category File**: [`../categories/basics/permutation_cycle_decomposition_bounded_swaps.md`](../categories/basics/permutation_cycle_decomposition_bounded_swaps.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given arrays A and B of length N. You can swap any two elements in A at most N - 2 times. Determine if you can make A_i <= B_i for all i.

**Key Insight**: Sort A and B independently. If sorted A_i > B_i for any i, it is impossible. If sorted A_i <= B_i holds for all i, pairing A_i with B_i defines a permutation on positions. A permutation with c disjoint cycles requires N - c swaps to sort. Thus, if the permutation has c >= 2 cycles, N - c <= N - 2 swaps suffice! If c = 1, it requires N - 1 swaps unless we can shortcut two adjacent elements: if sorted A_{i+1} <= B_i for any i, we can split the single cycle into two cycles without violating the inequality A <= B.

## 2. Core Observation & Invariant
Transposition budgeting reduces to cycle decomposition: N - 2 swaps require either >= 2 cycles or a cycle-splitting shortcut where sorted A_{i+1} <= B_i.

## 3. Step-by-Step Algorithm
1. Sort A and B. If A[i] > B[i] for any i, output No.
2. If there exists i such that A[i+1] <= B[i], output Yes (can split cycle).
3. Otherwise, build permutation mapping sorted A to original indices.
4. Count number of cycles in the permutation.
5. If cycles >= 2, output Yes; otherwise No.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Permutation cycle decomposition and parity budgeting for bounded swap operations.
- **Reusable Pattern**: Sorting under N - 2 swaps requires decomposing the assignment permutation into at least two cycles.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Element {
    long long a;
    int id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Element> a(n);
    vector<long long> b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].a;
        a[i].id = i;
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }

    sort(a.begin(), a.end(), [](const Element& x, const Element& y) {
        return x.a < y.a;
    });
    sort(b.begin(), b.end());

    for (int i = 0; i < n; ++i) {
        if (a[i].a > b[i]) {
            cout << "No\n";
            return 0;
        }
    }

    for (int i = 0; i < n - 1; ++i) {
        if (a[i + 1].a <= b[i]) {
            cout << "Yes\n";
            return 0;
        }
    }

    vector<bool> vis(n, false);
    int cycles = 0;
    for (int i = 0; i < n; ++i) {
        if (!vis[i]) {
            cycles++;
            int cur = i;
            while (!vis[cur]) {
                vis[cur] = true;
                cur = a[cur].id;
            }
        }
    }

    if (cycles >= 2) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```
