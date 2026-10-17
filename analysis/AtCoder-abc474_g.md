# Problem Analysis: AtCoder-abc474_g — G. LRUD Moving 2

**Problem ID**: `AtCoder-abc474_g`  
**Contest**: `abc474`  
**Rating / Difficulty**: 2280  
**URL**: https://atcoder.jp/contests/abc474/tasks/abc474_g  
**VJudge Tag**: `[problem:AtCoder-abc474_g]`  
**Category File**: [`../categories/graph_theory/grid_hamiltonian_path_parity_serpentine_construction.md`](../categories/graph_theory/grid_hamiltonian_path_parity_serpentine_construction.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Hamiltonian Path`  
- **Topic (Skill)**: `Hamiltonian Path and Cycle`  

---

## 1. Problem Statement & Key Idea
Construct an $N \times N$ matrix filled with integers from 1 to $N^2$ such that each row and each column contains exactly $K$ adjacent pairs whose difference is 1 in absolute value, or report impossible.

## 2. Core Observation & Invariant
In an $N \times N$ grid, start $(1, 1)$ and end $(N, N)$ have identical bipartite colors iff $N$ is odd, so even $N$ has no Hamiltonian path. Net horizontal displacement requires $R - L = N - 1$, and parity matching restricts $K$ to even values in $[N - 1, (N^2 - 1)/2]$, realized via serpentine column-loop folding.

## 3. Step-by-Step Algorithm
1. 1. Color the grid as a bipartite chessboard with color $(r + c) \bmod 2$. A Hamiltonian path visiting all $N^2$ cells has $N^2 - 1$ steps. If $N$ is even, $N^2 - 1$ is odd, which requires start and end to have different colors. But $(1, 1)$ and $(N, N)$ both have color 0. Thus $N$ must be odd.\n2. Since the path starts at column 1 and ends at column $N$, $R - L = N - 1$. An odd-index matching argument proves that $K$ (number of 'R' moves) must be even and satisfy $N - 1 \le K \le (N^2 - 1)/2$.\n3. Let $M = (N - 1)/2$ and surplus $S = (K - (N - 1))/2$. Partition $S$ into $M$ non-increasing integers $T_1 \ge T_2 \ge \dots \ge T_M \ge 0$ such that $\sum T_i = S$.\n4. Traverse the grid row pairs with serpentine loops: for each $i = 1 \dots M$, move right $2T_i$ steps, down 1, left $2T_i$ steps, down 1; then traverse columns with vertical loops of height $2(M - \sum [T_v \ge j])$ interspersed with 'R' moves. Time complexity per testcase is $O(N^2)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve_test() {
    int n;
    long long k;
    if (!(cin >> n >> k)) return;

    if (n % 2 == 0 || k % 2 == 1 || k < n - 1 || k > (1LL * n * n - 1) / 2) {
        cout << "No\n";
        return;
    }

    int m = (n - 1) / 2;
    long long s = (k - (n - 1)) / 2;

    vector<int> t(m);
    for (int i = 0; i < m; i++) {
        t[i] = (s + m - 1 - i) / m;
    }

    string ans;
    ans.reserve(n * n);

    for (int v : t) {
        ans.append(2 * v, 'R');
        ans.push_back('D');
        ans.append(2 * v, 'L');
        ans.push_back('D');
    }

    for (int j = 1; j <= m; j++) {
        int cnt = 0;
        for (int v : t) {
            if (v >= j) cnt++;
        }
        int d = 2 * (m - cnt);
        ans.push_back('R');
        ans.append(d, 'U');
        ans.push_back('R');
        ans.append(d, 'D');
    }

    cout << "Yes\n";
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve_test();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
