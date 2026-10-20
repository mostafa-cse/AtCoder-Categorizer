# Problem Analysis: AtCoder-arc149_d — D - Simultaneous Sugoroku

**Problem ID**: `AtCoder-arc149_d`  
**Contest**: `arc149`  
**Rating / Difficulty**: 2991  
**URL**: https://atcoder.jp/contests/arc149/tasks/arc149_d  
**VJudge Tag**: `[problem:AtCoder-arc149_d]`  
**Category File**: [`../categories/data_structures/interval_folding_affine_dsu_small_to_large_merging.md`](../categories/data_structures/interval_folding_affine_dsu_small_to_large_merging.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `DSU on Tree and Small to Large Merging`  

---

## 1. Problem Statement & Key Idea
Simultaneously simulate 2M pieces starting at +/-1, ..., +/-M following M steps where at step i, pieces at x > 0 move to x - X_i and pieces at x < 0 move to x + X_i, stopping if they hit 0.

## 2. Core Observation & Invariant
Active pieces at any step form a symmetric pair of contiguous intervals [xmin, xmax] with affine mapping x(i) = scale * i + offset. When step distance d falls inside [xmin, xmax], the interval splits: pieces hitting d stop at step i, and the smaller sub-interval folds into the larger sub-interval with an inverted affine sign. Small-to-large merging guarantees total work O(M log M).

## 3. Step-by-Step Algorithm
1. 1. Maintain the active coordinate range [xmin, xmax] with scale = 1, offset = 0.
2. 2. For each query d = X_i:
3.    - If d < xmin: all pieces shift by -d (offset -= d).
4.    - If d > xmax: all pieces shift by +d (offset += d).
5.    - If xmin <= d <= xmax: piece at d stops at step i. Split [xmin, xmax] into [xmin, d-1] and [d+1, xmax]. Merge the smaller side into the larger side using affine relation, and update scale and offset for the folded pieces.
6. 3. Propagate all affine relations to determine the final coordinate or stopping step for each piece 1 to M.
7. 4. Output results.

## 4. Complexity Analysis
- **Time Complexity**: `O(M \log M + N)`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MAX_VAL = 1000000;

int parent_node[MAX_VAL + 1];
int sign_rel[MAX_VAL + 1];
int die_step[MAX_VAL + 1];
int at_idx[MAX_VAL + 1];

int final_pos[MAX_VAL + 1];
bool is_dead[MAX_VAL + 1];
int dead_time[MAX_VAL + 1];

bool visited[MAX_VAL + 1];
bool ans_dead[MAX_VAL + 1];
int ans_time[MAX_VAL + 1];
int ans_pos[MAX_VAL + 1];

void dfs_ans(int u) {
    if (visited[u]) return;
    visited[u] = true;
    if (parent_node[u] == u) {
        ans_dead[u] = is_dead[u];
        ans_time[u] = dead_time[u];
        ans_pos[u] = final_pos[u];
    } else {
        int p = parent_node[u];
        int s = sign_rel[u];
        dfs_ans(p);
        ans_dead[u] = ans_dead[p];
        ans_time[u] = ans_time[p];
        ans_pos[u] = s * ans_pos[p];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<int> X(N);
    int max_coord = 0;
    for (int i = 0; i < N; ++i) {
        cin >> X[i];
        if (X[i] > max_coord) max_coord = X[i];
    }

    vector<int> D(M);
    for (int i = 0; i < M; ++i) {
        cin >> D[i];
        if (D[i] > max_coord) max_coord = D[i];
    }

    int limit = max_coord;
    for (int i = 0; i <= limit; ++i) {
        parent_node[i] = i;
        sign_rel[i] = 1;
        die_step[i] = 0;
        at_idx[i] = i;
    }

    int scale = 1;
    int offset = 0;
    int cur_sign = 1;

    int imin = 1;
    int imax = limit;

    auto get_x = [&](int i) -> int {
        return scale * i + offset;
    };

    auto get_i = [&](int x_val) -> int {
        return (x_val - offset) * scale;
    };

    for (int step = 1; step <= M; ++step) {
        if (imin > imax) break;
        int d = D[step - 1];

        int xmin = get_x(imin);
        int xmax = get_x(imax);
        if (xmin > xmax) swap(xmin, xmax);

        if (d < xmin) {
            offset -= d;
        } else if (d > xmax) {
            cur_sign = -cur_sign;
            scale = -scale;
            offset = d - offset;
        } else {
            int i_mid = get_i(d);
            die_step[at_idx[i_mid]] = step;

            int len_left = i_mid - imin;
            int len_right = imax - i_mid;

            if (len_left <= len_right) {
                for (int delta = 1; delta <= len_left; ++delta) {
                    int j_small = i_mid - delta;
                    int j_large = i_mid + delta;
                    int u = at_idx[j_small];
                    int v = at_idx[j_large];
                    parent_node[u] = v;
                    sign_rel[u] = -1;
                }
                imin = i_mid + 1;
            } else {
                for (int delta = 1; delta <= len_right; ++delta) {
                    int j_small = i_mid + delta;
                    int j_large = i_mid - delta;
                    int u = at_idx[j_small];
                    int v = at_idx[j_large];
                    parent_node[u] = v;
                    sign_rel[u] = -1;
                }
                imax = i_mid - 1;
            }

            if (imin <= imax) {
                int mid_val = get_x((imin + imax) / 2);
                if (mid_val > d) {
                    offset -= d;
                } else {
                    cur_sign = -cur_sign;
                    scale = -scale;
                    offset = d - offset;
                }
            }
        }
    }

    if (imin <= imax) {
        for (int i = imin; i <= imax; ++i) {
            int u = at_idx[i];
            final_pos[u] = cur_sign * get_x(i);
        }
    }

    for (int u = 1; u <= limit; ++u) {
        if (die_step[u] > 0) {
            is_dead[u] = true;
            dead_time[u] = die_step[u];
        }
    }

    for (int i = 0; i < N; ++i) {
        dfs_ans(X[i]);
        if (ans_dead[X[i]]) {
            cout << "Yes " << ans_time[X[i]] << "\n";
        } else {
            cout << "No " << ans_pos[X[i]] << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
