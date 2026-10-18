# Problem Analysis: AtCoder-abc384_g — G. Abs Sum

**Problem ID**: `AtCoder-abc384_g`  
**Contest**: `abc384`  
**Rating / Difficulty**: 2343  
**URL**: https://atcoder.jp/contests/abc384/tasks/abc384_g  
**VJudge Tag**: `[problem:AtCoder-abc384_g]`  
**Category File**: [`../categories/data_structures/mos_algorithm_prefix_abs_sum.md`](../categories/data_structures/mos_algorithm_prefix_abs_sum.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Mo's Algorithm`  

---

## 1. Problem Statement & Key Idea
Answer $K$ prefix queries $\sum_{i=1}^X \sum_{j=1}^Y |A_i - B_j|$ on arrays of size $N$. Maintaining two Fenwick trees over coordinate-compressed values under 2D Mo's algorithm with block size $N/\sqrt{K}$ yields $O((N + K)\sqrt{K} \log N)$.

## 2. Core Observation & Invariant
Prefix queries $\sum_{i=1}^X \sum_{j=1}^Y |A_i - B_j|$ on static sequences $A$ and $B$ can be maintained under pointer movement: advancing $X$ queries the current multiset $B_{1..Y}$ via Fenwick tree in $O(\log N)$, and advancing $Y$ queries $A_{1..X}$. Ordering queries with Mo's algorithm on $(X_k, Y_k)$ with block size $N / \sqrt{K}$ yields $O((N + K)\sqrt{K} \log N)$ total work.

## 3. Step-by-Step Algorithm
1. Coordinate-compress all elements of $A$ and $B$.
2. Sort queries $(X_k, Y_k)$ by $\lfloor X_k / B \rfloor$, alternating $Y_k$ sort direction across adjacent blocks with block size $B \approx N / \sqrt{K}$.
3. Maintain two Fenwick trees (one for $A$, one for $B$) storing prefix frequencies and prefix sums.
4. When extending or shrinking $X$ or $Y$, update the global sum in $O(\log N)$ via prefix Fenwick queries.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + K)\sqrt{K} \log N)`
- **Space Complexity**: `O(N + K)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Query {
    int x, y, id;
};

const int MAX = 200005;

struct Fenwick {
    int n;
    long long tree_cnt[MAX];
    long long tree_sum[MAX];
    long long tot_cnt = 0;
    long long tot_sum = 0;

    void init(int _n) {
        n = _n;
        for (int i = 0; i <= n; ++i) {
            tree_cnt[i] = 0;
            tree_sum[i] = 0;
        }
        tot_cnt = 0;
        tot_sum = 0;
    }

    void add(int i, long long val, int delta) {
        tot_cnt += delta;
        tot_sum += delta * val;
        for (; i <= n; i += i & -i) {
            tree_cnt[i] += delta;
            tree_sum[i] += delta * val;
        }
    }

    // returns pair: {count <= i, sum <= i}
    void query_le(int i, long long& le_cnt, long long& le_sum) {
        le_cnt = 0;
        le_sum = 0;
        for (; i > 0; i -= i & -i) {
            le_cnt += tree_cnt[i];
            le_sum += tree_sum[i];
        }
    }
};

Fenwick fenwA, fenwB;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N + 1), B(N + 1);
    vector<long long> vals;
    vals.reserve(2 * N);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
        vals.push_back(A[i]);
    }
    for (int i = 1; i <= N; ++i) {
        cin >> B[i];
        vals.push_back(B[i]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    int M = vals.size();

    vector<int> rA(N + 1), rB(N + 1);
    for (int i = 1; i <= N; ++i) {
        rA[i] = lower_bound(vals.begin(), vals.end(), A[i]) - vals.begin() + 1;
        rB[i] = lower_bound(vals.begin(), vals.end(), B[i]) - vals.begin() + 1;
    }

    int K;
    if (!(cin >> K)) return 0;
    vector<Query> Q(K);
    for (int i = 0; i < K; ++i) {
        cin >> Q[i].x >> Q[i].y;
        Q[i].id = i;
    }

    int blockSize = max(1, (int)(N / max(1.0, sqrt(K))));
    sort(Q.begin(), Q.end(), [&](const Query& a, const Query& b) {
        int b1 = a.x / blockSize;
        int b2 = b.x / blockSize;
        if (b1 != b2) return b1 < b2;
        return (b1 % 2 == 1) ? (a.y < b.y) : (a.y > b.y);
    });

    fenwA.init(M);
    fenwB.init(M);

    int curX = 0, curY = 0;
    long long cur_ans = 0;
    vector<long long> ans(K);

    auto addX = [&](int idx) {
        long long v = A[idx];
        int r = rA[idx];
        long long le_cnt, le_sum;
        fenwB.query_le(r, le_cnt, le_sum);
        long long gt_cnt = fenwB.tot_cnt - le_cnt;
        long long gt_sum = fenwB.tot_sum - le_sum;
        cur_ans += (le_cnt * v - le_sum) + (gt_sum - gt_cnt * v);
        fenwA.add(r, v, 1);
    };

    auto removeX = [&](int idx) {
        long long v = A[idx];
        int r = rA[idx];
        fenwA.add(r, v, -1);
        long long le_cnt, le_sum;
        fenwB.query_le(r, le_cnt, le_sum);
        long long gt_cnt = fenwB.tot_cnt - le_cnt;
        long long gt_sum = fenwB.tot_sum - le_sum;
        cur_ans -= (le_cnt * v - le_sum) + (gt_sum - gt_cnt * v);
    };

    auto addY = [&](int idx) {
        long long v = B[idx];
        int r = rB[idx];
        long long le_cnt, le_sum;
        fenwA.query_le(r, le_cnt, le_sum);
        long long gt_cnt = fenwA.tot_cnt - le_cnt;
        long long gt_sum = fenwA.tot_sum - le_sum;
        cur_ans += (le_cnt * v - le_sum) + (gt_sum - gt_cnt * v);
        fenwB.add(r, v, 1);
    };

    auto removeY = [&](int idx) {
        long long v = B[idx];
        int r = rB[idx];
        fenwB.add(r, v, -1);
        long long le_cnt, le_sum;
        fenwA.query_le(r, le_cnt, le_sum);
        long long gt_cnt = fenwA.tot_cnt - le_cnt;
        long long gt_sum = fenwA.tot_sum - le_sum;
        cur_ans -= (le_cnt * v - le_sum) + (gt_sum - gt_cnt * v);
    };

    for (const auto& q : Q) {
        while (curX < q.x) addX(++curX);
        while (curY < q.y) addY(++curY);
        while (curX > q.x) removeX(curX--);
        while (curY > q.y) removeY(curY--);
        ans[q.id] = cur_ans;
    }

    for (int i = 0; i < K; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
