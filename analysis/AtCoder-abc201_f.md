# Problem Analysis: AtCoder-abc201_f — F. Insertion Sort

**Problem ID**: `AtCoder-abc201_f`  
**Contest**: `abc201`  
**Rating / Difficulty**: 2484  
**URL**: https://atcoder.jp/contests/abc201/tasks/abc201_f  
**VJudge Tag**: `[problem:AtCoder-abc201_f]`  
**Category File**: [`../categories/data_structures_ds/insertion_sort_unmoved_lis_segment_tree.md`](../categories/data_structures_ds/insertion_sort_unmoved_lis_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Find the minimum cost to sort a permutation $P$ of $1 \dots N$ by moving elements to the front (cost $B_i$ or $A_i$), back (cost $C_i$ or $A_i$), or arbitrary position (cost $A_i$). Elements that are never moved must form an increasing subsequence of values and indices $x_1 < x_2 < \dots < x_k$. Elements with values $< x_1$ can be moved to the front paying $\min(A_i, B_i)$, elements $> x_k$ can be moved to the back paying $\min(A_i, C_i)$, and interior elements not in the subsequence pay $A_i$. The optimal sequence of unmoved elements is found via DP accelerated with a Segment Tree in $O(N \log N)$ time.

## 2. Core Observation & Invariant
Since any element moved to the left can be placed at the front, and any moved to the right at the back, all elements outside the chosen subsequence can be placed correctly. If value $i$ is unmoved, any preceding unmoved value $j < i$ must satisfy $pos[j] < pos[i]$. The transition $DP[i] = \min(\text{prefMinAB}[i-1], \min_{j < i, pos[j] < pos[i]} (DP[j] - \text{prefA}[j]) + \text{prefA}[i-1])$ allows point updates and range minimum queries over positions $pos$.

## 3. Step-by-Step Algorithm
1. 1. Precompute prefix sums of $A_i$, and prefix sums of $\min(A_i, B_i)$ and $\min(A_i, C_i)$.
2. 2. Build a Segment Tree over index positions $1 \dots N$ supporting point update and range minimum query.
3. 3. For each value $i$ from 1 to $N$, query the segment tree for range $[1, pos[i] - 1]$ to find $\min_{j < i, pos[j] < pos[i]} (DP[j] - \text{prefA}[j])$.
4. 4. Set $DP[i] = \min(\text{prefMinAB}[i-1], \text{min\_val} + \text{prefA}[i-1])$.
5. 5. Update the segment tree at position $pos[i]$ with $DP[i] - \text{prefA}[i]$.
6. 6. Compute candidate answer $DP[i] + \text{suffMinAC}[i+1]$ and take the global minimum over all $i$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

class SegTree {
public:
    int n;
    vector<long long> tree;

    SegTree(int n) : n(n), tree(4 * n, INF) {}

    void update(int node, int l, int r, int idx, long long val) {
        if (l == r) {
            tree[node] = min(tree[node], val);
            return;
        }
        int mid = (l + r) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx, val);
        else update(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    long long query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return INF;
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) / 2;
        return min(query(2 * node, l, mid, ql, qr),
                   query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    vector<int> pos(n + 1);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        pos[p[i]] = i + 1;
    }

    vector<long long> a(n + 1), b(n + 1), c(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i] >> b[i] >> c[i];
    }

    vector<long long> pref_a(n + 1, 0);
    vector<long long> pref_min_ab(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        pref_a[i] = pref_a[i - 1] + a[i];
        pref_min_ab[i] = pref_min_ab[i - 1] + min(a[i], b[i]);
    }

    vector<long long> suff_min_ac(n + 2, 0);
    for (int i = n; i >= 1; --i) {
        suff_min_ac[i] = suff_min_ac[i + 1] + min(a[i], c[i]);
    }

    long long ans = INF;
    for (int i = 0; i <= n; ++i) {
        ans = min(ans, pref_min_ab[i] + suff_min_ac[i + 1]);
    }

    SegTree st(n);
    for (int i = 1; i <= n; ++i) {
        long long best_dp = pref_min_ab[i - 1];
        long long min_prev = st.query(1, 1, n, 1, pos[i] - 1);
        if (min_prev < 1e17) {
            best_dp = min(best_dp, min_prev + pref_a[i - 1]);
        }
        ans = min(ans, best_dp + suff_min_ac[i + 1]);
        st.update(1, 1, n, pos[i], best_dp - pref_a[i]);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
