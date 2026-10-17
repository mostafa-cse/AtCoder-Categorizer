# Problem Analysis: AtCoder-abc258_g — Triangle

**Problem ID**: `AtCoder-abc258_g`  
**Contest**: `abc258`  
**Rating / Difficulty**: 1944  
**URL**: https://atcoder.jp/contests/abc258/tasks/abc258_g  
**VJudge Tag**: `[problem:AtCoder-abc258_g]`  
**Category File**: [`../categories/data_structures/bitset_triangle_counting_n3_64.md`](../categories/data_structures/bitset_triangle_counting_n3_64.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Bitset Optimizations`  
- **Topic (Skill)**: `Bitset-Accelerated Triangle Counting via Neighbor Set Intersections O(N^3 / 64)`  

---

## 1. Problem Statement & Key Idea
Given an undirected simple graph with N vertices (N <= 3000) as an adjacency matrix. Count the number of triangles (i, j, k) with i < j < k.

For each pair of adjacent vertices (i, j) with i < j, the number of common neighbors k > j is the size of the set intersection of neighbors of i and neighbors of j restricted to indices > j. Using std::bitset<3000>, storing only neighbors with index > i, the count is simply (adj[i] & adj[j]).count(). Running bitwise AND over 64-bit machine words reduces operations by a factor of 64 to N^3 / 64 ~ 4.2 * 10^8 ops, executing in ~0.3s.

## 2. Core Observation & Invariant
std::bitset bitwise AND + popcount achieves word-level parallelism for dense graph triangle enumeration.

## 3. Step-by-Step Algorithm
1. Initialize adj[i] as bitset<3000> for each vertex i.
2. Read adjacency matrix; if edge (i, j) exists and j > i, set bit j in adj[i].
3. ans = 0.
4. For each i from 0 to N - 1:
5.   For each j > i where adj[i].test(j):
6.     ans += (adj[i] & adj[j]).count().
7. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 / 64)`
- **Space Complexity**: `O(N^2 / 64)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <bitset>

using namespace std;

const int MAXN = 3000;
bitset<MAXN> adj[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        for (int j = i + 1; j < n; ++j) {
            if (s[j] == '1') {
                adj[i].set(j);
            }
        }
    }

    long long count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (adj[i].test(j)) {
                count += (adj[i] & adj[j]).count();
            }
        }
    }

    cout << count << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitset acceleration for word-level parallelism in cubic dense graph operations.
- **Reusable Pattern**: `Bitset Triangle Count: For edge (i, j) with i < j, count += (adj[i] & adj[j]).count().`
