# Problem Analysis: AtCoder-arc201_e — E - Subsets and Bounding Box Areas

**Problem ID**: `AtCoder-arc201_e`  
**Contest**: `arc201`  
**Rating / Difficulty**: 2635  
**URL**: https://atcoder.jp/contests/arc201/tasks/arc201_e  
**VJudge Tag**: `[problem:AtCoder-arc201_e]`  
**Category File**: [`../categories/combinatorics/bounding_box_areas_contribution_technique.md`](../categories/combinatorics/bounding_box_areas_contribution_technique.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Given N points in the plane, compute the sum of bounding box areas (X_max - X_min)(Y_max - Y_min) over all non-empty subsets of points modulo 998244353.

## 2. Core Observation & Invariant
The area (X_max - X_min)(Y_max - Y_min) equals the number of unit cells [x, x+1] x [y, y+1] covered by the bounding box. A cell is covered iff the subset contains points both to its left and right, and both above and below. Decomposing by 4 quadrants around (x, y), the count of valid subsets is expressed via inclusion-exclusion in terms of quadrant counts. Sweeping across x and maintaining quadrant counts in a Lazy Segment Tree evaluates all contributions in O(N log N).

## 3. Step-by-Step Algorithm
1. Coordinate-compress point coordinates X_i, Y_i.
2. Decompose total area into integral of coverage probabilities over grid lines.
3. Maintain counts of points in 4 quadrants using a Lazy Segment Tree with affine/addition tags.
4. Sweep through coordinates x, updating tree values as points cross from right to left quadrants.
5. Accumulate valid subset counts weighted by interval lengths.
6. Output sum modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

using ll = long long;

const int MOD = 998244353;
const int INV2 = (MOD + 1) / 2;

struct Node {
    ll sum1, sum2, sum3, sum4;
    ll lazy1, lazy2, lazy3, lazy4;
};

const int MAXN = 200005;
Node tree[4 * MAXN];

void apply(int node, ll m1, ll m2, ll m3, ll m4) {
    tree[node].sum1 = tree[node].sum1 * m1 % MOD;
    tree[node].sum2 = tree[node].sum2 * m2 % MOD;
    tree[node].sum3 = tree[node].sum3 * m3 % MOD;
    tree[node].sum4 = tree[node].sum4 * m4 % MOD;

    tree[node].lazy1 = tree[node].lazy1 * m1 % MOD;
    tree[node].lazy2 = tree[node].lazy2 * m2 % MOD;
    tree[node].lazy3 = tree[node].lazy3 * m3 % MOD;
    tree[node].lazy4 = tree[node].lazy4 * m4 % MOD;
}

void push(int node) {
    if (tree[node].lazy1 != 1 || tree[node].lazy2 != 1 || tree[node].lazy3 != 1 || tree[node].lazy4 != 1) {
        apply(2 * node, tree[node].lazy1, tree[node].lazy2, tree[node].lazy3, tree[node].lazy4);
        apply(2 * node + 1, tree[node].lazy1, tree[node].lazy2, tree[node].lazy3, tree[node].lazy4);
        tree[node].lazy1 = tree[node].lazy2 = tree[node].lazy3 = tree[node].lazy4 = 1;
    }
}

void pull(int node) {
    tree[node].sum1 = (tree[2 * node].sum1 + tree[2 * node + 1].sum1) % MOD;
    tree[node].sum2 = (tree[2 * node].sum2 + tree[2 * node + 1].sum2) % MOD;
    tree[node].sum3 = (tree[2 * node].sum3 + tree[2 * node + 1].sum3) % MOD;
    tree[node].sum4 = (tree[2 * node].sum4 + tree[2 * node + 1].sum4) % MOD;
}

ll pow2_arr[MAXN];

void build(int node, int l, int r, int N) {
    tree[node].lazy1 = tree[node].lazy2 = tree[node].lazy3 = tree[node].lazy4 = 1;
    if (l == r) {
        tree[node].sum1 = 1;
        tree[node].sum2 = 1;
        tree[node].sum3 = pow2_arr[l];
        tree[node].sum4 = pow2_arr[N - l];
        return;
    }
    int mid = (l + r) / 2;
    build(2 * node, l, mid, N);
    build(2 * node + 1, mid + 1, r, N);
    pull(node);
}

void update_range(int node, int l, int r, int ql, int qr, ll m1, ll m2, ll m3, ll m4) {
    if (ql > r || qr < l) return;
    if (ql <= l && r <= qr) {
        apply(node, m1, m2, m3, m4);
        return;
    }
    push(node);
    int mid = (l + r) / 2;
    update_range(2 * node, l, mid, ql, qr, m1, m2, m3, m4);
    update_range(2 * node + 1, mid + 1, r, ql, qr, m1, m2, m3, m4);
    pull(node);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> Y(N);
    for (int i = 0; i < N; ++i) {
        cin >> Y[i];
    }

    pow2_arr[0] = 1;
    for (int i = 1; i <= N; ++i) {
        pow2_arr[i] = (pow2_arr[i - 1] * 2) % MOD;
    }

    ll sum_pow_x = 0;
    for (int x = 1; x < N; ++x) {
        sum_pow_x = (sum_pow_x + pow2_arr[x]) % MOD;
    }

    ll const_part = (ll)(N - 1) * (N - 1) % MOD * ((pow2_arr[N] - 1 + MOD) % MOD) % MOD;
    const_part = (const_part - 4LL * (N - 1) % MOD * sum_pow_x % MOD + MOD) % MOD;

    build(1, 1, N - 1, N);

    ll ans = 0;
    for (int x = 1; x < N; ++x) {
        int p = Y[x - 1];
        // update [1, p - 1]: m1=1, m2=2, m3=1, m4=INV2
        if (p > 1) {
            update_range(1, 1, N - 1, 1, p - 1, 1, 2, 1, INV2);
        }
        // update [p, N - 1]: m1=2, m2=1, m3=INV2, m4=1
        if (p <= N - 1) {
            update_range(1, 1, N - 1, p, N - 1, 2, 1, INV2, 1);
        }

        ll cur_sum = (tree[1].sum1 + tree[1].sum2 + tree[1].sum3 + tree[1].sum4) % MOD;
        ans = (ans + cur_sum) % MOD;
    }

    ll final_ans = (ans + const_part) % MOD;
    final_ans = (final_ans + MOD) % MOD;
    cout << final_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
