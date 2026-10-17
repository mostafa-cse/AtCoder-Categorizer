# Problem Analysis: AtCoder-abc013_4 — 阿弥陀

**Problem ID**: `AtCoder-abc013_4`  
**Contest**: `abc013`  
**Rating / Difficulty**: 1730  
**URL**: https://atcoder.jp/contests/abc013/tasks/abc013_4  
**VJudge Tag**: `[problem:AtCoder-abc013_4]`  
**Category File**: [`../categories/data_structures/binary_lifting_permutation_amidakuji.md`](../categories/data_structures/binary_lifting_permutation_amidakuji.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Binary Lifting`  
- **Topic (Skill)**: `Binary Lifting on Permutations / Amidakuji Exponentiation`  

---

## 1. Problem Statement & Key Idea
An Amidakuji ladder has N vertical lines and M horizontal rungs. Given D <= 10^9, find where each vertical line ends up after traversing the ladder D times.

**Key Insight**: Traversing the ladder once forms a permutation P of {1, ..., N}. Traversing D times corresponds to computing P^D. Use binary lifting (doubling) over the permutation table up[k][i] = P^{2^k}(i).

## 2. Core Observation & Invariant
Constructing P from M rungs takes O(N + M). Precomputing binary lifting takes O(N log D), and applying it takes O(N log D).

## 3. Step-by-Step Algorithm
1. Start with identity permutation P[i] = i for i = 1..N.
2. Process rungs from bottom to top: swapping P[a_j] and P[a_j + 1].
3. Build binary lifting table up[30][N + 1] where up[0][i] = P[i].
4. For k = 1 to 29: up[k][i] = up[k - 1][up[k - 1][i]].
5. For each line i = 1 to N, apply D's set bits to find final position.
6. Print results.

## 4. Complexity Analysis
- **Time Complexity**: `O(M + N log D)`
- **Space Complexity**: `O(N log D)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long d;
    if (!(cin >> n >> m >> d)) return 0;

    vector<int> a(m);
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }

    vector<int> p(n + 1);
    iota(p.begin(), p.end(), 0);

    for (int i = m - 1; i >= 0; --i) {
        swap(p[a[i]], p[a[i] + 1]);
    }

    vector<vector<int>> up(31, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        up[0][i] = p[i];
    }

    for (int k = 1; k < 31; ++k) {
        for (int i = 1; i <= n; ++i) {
            up[k][i] = up[k - 1][up[k - 1][i]];
        }
    }

    for (int i = 1; i <= n; ++i) {
        int cur = i;
        for (int k = 0; k < 31; ++k) {
            if ((d >> k) & 1) {
                cur = up[k][cur];
            }
        }
        cout << cur << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Permutation exponentiation using binary lifting tables.
- **Reusable Pattern**: `Permutation Exponentiation via Doubling: up[k][i] = up[k-1][up[k-1][i]].`
