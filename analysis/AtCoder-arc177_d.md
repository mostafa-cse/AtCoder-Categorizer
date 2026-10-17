# Problem Analysis: AtCoder-arc177_d — D. Earthquakes

**Problem ID**: `AtCoder-arc177_d`  
**Contest**: `arc177`  
**Rating / Difficulty**: 2299  
**URL**: https://atcoder.jp/contests/arc177/tasks/arc177_d  
**VJudge Tag**: `[problem:AtCoder-arc177_d]`  
**Category File**: [`../categories/math/expected_values_domino_toppling_segment_tree.md`](../categories/math/expected_values_domino_toppling_segment_tree.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Given $N$ poles of height $H$ at coordinates $X_i$, each falling left or right with probability $1/2$ during sequential earthquakes, compute the probability that all poles have fallen by exactly the $t$-th earthquake multiplied by $2^N$ for all $t = 1, \dots, N$ modulo 998244353.

## 2. Core Observation & Invariant
Decomposing poles into independent contiguous blocks where adjacent gaps are <= H simplifies the state: within each block, pole i is the last to fall iff all poles to its left fall left and all poles to its right fall right. The number of preceding events equals the monotonic stack sizes for running minima to the left and right. Aggregating block completion distributions using a segment tree computes the exact probability that all N poles have fallen by earthquake t in O(N log N) time.

## 3. Step-by-Step Algorithm
1. 1. Group adjacent poles with $X_{i+1} - X_i \le H$ into independent components.
2. 2. Within each group of size $m$, for each pole $i$, use monotonic stacks to count how many times the running minimum of earthquake arrival times updates when moving left and right from $i$. The number of valid outcomes where pole $i$ is the last to fall in the group is $2^{(m-1) - |sl| - |sr|} \times c$, where $c$ is the number of valid falling directions for pole $i$ that cover the entire group.
3. 3. Process earthquakes in chronological order $t = 1, \dots, N$. Maintain the running sum of weights of completed poles for each group in a segment tree. The product of group sums gives the cumulative number of outcomes where all poles have fallen by time $t$.
4. 4. Differencing $res[t] - res[t-1] \pmod{998244353}$ yields the exact answer for each $t$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

struct SegTree {
    int size;
    vector<long long> v;
    SegTree(int n) {
        size = 1;
        while (size < n) size <<= 1;
        v.assign(size * 2, 0);
    }
    void add(int pos, long long x) {
        pos += size;
        v[pos] = (v[pos] + x) % MOD;
        pos >>= 1;
        while (pos >= 1) {
            v[pos] = (v[pos * 2] * v[pos * 2 + 1]) % MOD;
            pos >>= 1;
        }
    }
    long long query(int l, int r) {
        l += size;
        r += size;
        long long res = 1;
        while (l < r) {
            if (l & 1) {
                res = (res * v[l]) % MOD;
                l++;
            }
            if (r & 1) {
                r--;
                res = (res * v[r]) % MOD;
            }
            l >>= 1;
            r >>= 1;
        }
        return res;
    }
};

vector<long long> calc(int n, const vector<int>& p) {
    vector<int> level(n, n - 1);
    vector<int> sl;
    for (int i = 0; i < n; ++i) {
        while (!sl.empty() && sl.back() > p[i]) {
            sl.pop_back();
        }
        level[i] -= sl.size();
        sl.push_back(p[i]);
    }
    vector<int> sr;
    for (int i = n - 1; i >= 0; --i) {
        while (!sr.empty() && sr.back() > p[i]) {
            sr.pop_back();
        }
        level[i] -= sr.size();
        sr.push_back(p[i]);
    }

    vector<long long> power2(n + 1, 1);
    for (int i = 0; i < n; ++i) {
        power2[i + 1] = (power2[i] * 2) % MOD;
    }

    vector<long long> res(n, 0);
    for (int i = 0; i < n; ++i) {
        int c = (i == n - 1 || p[i] > p[i + 1]) + (i == 0 || p[i] > p[i - 1]);
        res[i] = (power2[level[i]] * c) % MOD;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long H;
    if (!(cin >> N >> H)) return 0;

    vector<long long> X(N);
    for (int i = 0; i < N; ++i) {
        cin >> X[i];
    }

    vector<pair<long long, int>> pillars(N);
    for (int i = 0; i < N; ++i) {
        pillars[i] = {X[i], i};
    }
    sort(pillars.begin(), pillars.end());

    vector<int> p(N);
    for (int i = 0; i < N; ++i) {
        p[i] = pillars[i].second;
    }

    vector<long long> v;
    vector<int> g;
    int pre = 0;
    int m = 0;

    for (int i = 1; i <= N; ++i) {
        if (i == N || pillars[i].first - pillars[i - 1].first > H) {
            vector<int> sub_p(p.begin() + pre, p.begin() + i);
            vector<long long> sub_v = calc(i - pre, sub_p);
            for (long long val : sub_v) v.push_back(val);
            for (int k = pre; k < i; ++k) g.push_back(m);
            pre = i;
            m++;
        }
    }

    vector<int> pinv(N);
    for (int i = 0; i < N; ++i) {
        pinv[p[i]] = i;
    }

    SegTree seg(m);
    vector<long long> pref_res;
    pref_res.push_back(0);

    for (int idx : pinv) {
        seg.add(g[idx], v[idx]);
        pref_res.push_back(seg.query(0, m));
    }

    for (int i = 0; i < N; ++i) {
        long long ans = (pref_res[i + 1] - pref_res[i] + MOD) % MOD;
        cout << ans << (i == N - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
