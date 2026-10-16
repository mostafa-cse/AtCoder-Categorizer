# Problem Analysis: AtCoder-abc165_c — Many Requirements

**Problem ID**: `AtCoder-abc165_c`  
**Contest**: `abc165`  
**Rating / Difficulty**: 1136  
**URL**: https://atcoder.jp/contests/abc165/tasks/abc165_c  
**VJudge Tag**: `[problem:AtCoder-abc165_c]`  
**Category File**: [`../categories/basics/monotonic_sequence_generation_dfs.md`](../categories/basics/monotonic_sequence_generation_dfs.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Backtracking`  
- **Topic (Skill)**: `Monotonic Non-Decreasing Sequence Generation via DFS`  

---

## 1. Problem Statement & Key Idea
Given integers N, M <= 10. Consider all sequences 1 <= A_1 <= A_2 <= ... <= A_N <= M. Q requirements reward d_i if A_{b_i} - A_{a_i} == c_i. Maximize the total score.

**Key Idea**: The total number of non-decreasing sequences of length N with elements in 1..M is C(N + M - 1, N) = C(19, 10) = 92,378.

## 2. Core Observation & Invariant
Because the search space is fewer than 100,000 sequences, we can generate all valid monotonic sequences using backtracking DFS and evaluate the score of each sequence in O(Q).

## 3. Step-by-Step Algorithm
1. Write DFS(current_index, last_value):
2. If current_index == N: evaluate score = sum d_i for satisfied conditions; update max_score; return.
3. For next_val from last_value to M: A[current_index] = next_val; DFS(current_index + 1, next_val).
4. Start DFS(0, 1) and output max_score.

## 4. Complexity Analysis
- **Time Complexity**: `O(C(N + M - 1, N) * Q)`
- **Space Complexity**: `O(N + Q)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Query {
    int a, b, c, d;
};

int n, m, q;
vector<Query> queries;
vector<int> a;
long long max_score = 0;

void dfs(int idx, int last_val) {
    if (idx == n) {
        long long current_score = 0;
        for (const auto& qry : queries) {
            if (a[qry.b] - a[qry.a] == qry.c) {
                current_score += qry.d;
            }
        }
        max_score = max(max_score, current_score);
        return;
    }

    for (int v = last_val; v <= m; ++v) {
        a[idx] = v;
        dfs(idx + 1, v);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m >> q)) return 0;

    queries.resize(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].a >> queries[i].b >> queries[i].c >> queries[i].d;
        queries[i].a--; // 0-indexed
        queries[i].b--;
    }

    a.resize(n);
    dfs(0, 1);

    cout << max_score << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Generating all monotonic sequences via backtracking search.
- **Reusable Pattern**: `Non-decreasing DFS: loop next_val from last_value to M.`
