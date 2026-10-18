# Problem Analysis: AtCoder-code_festival_morning_hard_c — C - 宝探し 2

**Problem ID**: `AtCoder-code_festival_morning_hard_c`  
**Contest**: `code_festival_morning_hard`  
**Rating / Difficulty**: 2521  
**URL**: https://atcoder.jp/contests/code_festival_morning_hard/tasks/code_festival_morning_hard_c  
**VJudge Tag**: `[problem:AtCoder-code_festival_morning_hard_c]`  
**Category File**: [`../categories/data_structures_ds/treasure_hunt_2d_bit_multitype_grid.md`](../categories/data_structures_ds/treasure_hunt_2d_bit_multitype_grid.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Binary Indexed Tree (BIT)`  
- **Topic (Skill)**: `2D BIT`  

---

## 1. Problem Statement & Key Idea
Process cell swaps and sub-rectangle majority type queries on an $N \times M$ grid with cell types $1 \dots K$ ($N, M \le 500, K \le 100$).

## 2. Core Observation & Invariant
With $K \le 100$ and $N, M \le 500$, we maintain a separate 2D Binary Indexed Tree (Fenwick Tree) for each of the $K$ types. Total memory is $100 \times 500 \times 500 \times 4 \text{ bytes} \approx 100 \text{ MB}$, well within limits. Type 1 swaps two cells, updating 4 points across the 2D BITs in $O(\log N \log M)$ time. Type 2 queries a sub-rectangle $[r_1, r_2] \times [c_1, c_2]$: querying each of the $K$ 2D BITs takes $O(K \log N \log M)$ time to find the maximum frequency and tiebreak by largest type.

## 3. Step-by-Step Algorithm
1. 1. Initialize $K$ 2D Binary Indexed Trees of size $(N+1) \times (M+1)$.
2. 2. Insert initial grid entries into their respective 2D BITs.
3. 3. For swap query $(r_1, c_1, r_2, c_2)$: if $grid[r_1][c_1] \ne grid[r_2][c_2]$, update $(-1, +1)$ at $(r_1, c_1)$ and $(r_2, c_2)$ and swap values.
4. 4. For rectangle query $(r_1, c_1, r_2, c_2)$: query each type $k \in [1, K]$ in $O(\log N \log M)$, finding the maximum count with tie-break favoring larger $k$.
5. 5. Output the best type and count for each query.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q_1 \log N \log M + Q_2 K \log N \log M)`
- **Space Complexity**: `O(K N M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, K;
int bit[101][502][502];
int grid[502][502];

void add(int k, int r, int c, int val) {
    for (int i = r; i <= N; i += i & (-i)) {
        for (int j = c; j <= M; j += j & (-j)) {
            bit[k][i][j] += val;
        }
    }
}

int query_pref(int k, int r, int c) {
    int res = 0;
    for (int i = r; i > 0; i -= i & (-i)) {
        for (int j = c; j > 0; j -= j & (-j)) {
            res += bit[k][i][j];
        }
    }
    return res;
}

int query_rect(int k, int r1, int c1, int r2, int c2) {
    return query_pref(k, r2, c2) - query_pref(k, r1 - 1, c2)
         - query_pref(k, r2, c1 - 1) + query_pref(k, r1 - 1, c1 - 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> M >> K)) return 0;

    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= M; ++j) {
            cin >> grid[i][j];
            add(grid[i][j], i, j, 1);
        }
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int r1, c1, r2, c2;
            cin >> r1 >> c1 >> r2 >> c2;
            if (grid[r1][c1] != grid[r2][c2]) {
                int v1 = grid[r1][c1], v2 = grid[r2][c2];
                add(v1, r1, c1, -1); add(v2, r1, c1, 1);
                add(v2, r2, c2, -1); add(v1, r2, c2, 1);
                grid[r1][c1] = v2; grid[r2][c2] = v1;
            }
        } else {
            int r1, c1, r2, c2;
            cin >> r1 >> c1 >> r2 >> c2;
            if (r1 > r2) swap(r1, r2);
            if (c1 > c2) swap(c1, c2);
            int best_cnt = -1;
            int best_k = -1;
            for (int k = 1; k <= K; ++k) {
                int cnt = query_rect(k, r1, c1, r2, c2);
                if (cnt >= best_cnt) {
                    best_cnt = cnt;
                    best_k = k;
                }
            }
            cout << best_k << " " << best_cnt << "\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
