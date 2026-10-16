# Monotonic Non-Decreasing Sequence Generation via DFS

**Domain**: `Basics`  
**Subtopic**: `Backtracking`  

This workbook contains curated, high-quality competitive programming problems teaching **Monotonic Non-Decreasing Sequence Generation via DFS**.

---

## Curated Problems

### [problem:AtCoder-abc165_c] — Many Requirements
- **Contest**: `abc165`
- **Rating / Difficulty**: 1136
- **Specific Skill**: Monotonic Non-Decreasing Sequence Generation via DFS
- **Individual Analysis**: [`../../analysis/AtCoder-abc165_c.md`](../../analysis/AtCoder-abc165_c.md)
- **Problem Statement Summary**: Given integers N, M <= 10. Consider all sequences 1 <= A_1 <= A_2 <= ... <= A_N <= M. Q requirements reward d_i if A_{b_i} - A_{a_i} == c_i. Maximize the total score.
- **Core Insight**: Because the search space is fewer than 100,000 sequences, we can generate all valid monotonic sequences using backtracking DFS and evaluate the score of each sequence in O(Q).
- **Complexity**: Time: `O(C(N + M - 1, N) * Q)` | Space: `O(N + Q)`
- **Verified C++ Implementation**:
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
