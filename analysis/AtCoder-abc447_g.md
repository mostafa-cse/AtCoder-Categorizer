# Problem Analysis: AtCoder-abc447_g — G. Div. 1 & Div. 2

**Problem ID**: `AtCoder-abc447_g`  
**Contest**: `abc447`  
**Rating / Difficulty**: 2391  
**URL**: https://atcoder.jp/contests/abc447/tasks/abc447_g  
**VJudge Tag**: `[problem:AtCoder-abc447_g]`  
**Category File**: [`../categories/dynamic_programming/distinct_genres_prefix_suffix_top_elements_segtree.md`](../categories/dynamic_programming/distinct_genres_prefix_suffix_top_elements_segtree.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Partition 6 problems into prefix (i1, i2), pivot pair (i3, i4), and suffix (i5, i6). Forbidding the 2 pivot genres reduces prefix and suffix choices to top-4 distinct genre candidates, dynamically maintained in a segment tree in O(N log N) time.

## 2. Core Observation & Invariant
Choosing 6 problems i1 < i2 < i3 < i4 < i5 < i6 where Div 2 (i1..i4) and Div 1 (i3..i6) have distinct genres separates at the shared boundary (i3, i4). In the prefix before i3, only the top 4 genre-distinct elements matter; similarly in the suffix after i4. Fixing the genre c of i4, the prefix best values M(x) undergo only O(1) transitions across all c, maintainable dynamically in a segment tree.

## 3. Step-by-Step Algorithm
1. Precompute prefix top 4 distinct genre elements L[i] and suffix top 4 distinct genre elements R[i] in O(N).
2. For each index i, define baseline M(i) as A[i] + top 2 values from L[i-1] avoiding genre K[i].
3. For each genre c, record index updates where forbidding c drops the top 2 sum to the 3rd candidate.
4. Maintain M(i) in a Segment Tree of top 4 distinct-genre values, query st.prod(0, i4) for each i4 of genre c, and pair with best suffix choices from R[i4+1] in O(N log N) total time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll inf = 1LL << 60;

const int SZ = 4;
using S = array<pair<ll, ll>, SZ>;

S op(const S &a, const S &b) {
    array<pair<ll, ll>, SZ * 2> c;
    copy(a.begin(), a.end(), c.begin());
    copy(b.begin(), b.end(), c.begin() + SZ);
    sort(c.rbegin(), c.rend());
    S res;
    int it = 0;
    for (int i = 0; i < SZ; i++) {
        while (true) {
            bool ok = true;
            for (int j = 0; j < i; j++) {
                if (res[j].second == c[it].second) {
                    ok = false;
                    break;
                }
            }
            if (ok) break;
            it++;
        }
        res[i] = c[it++];
    }
    return res;
}

S e() {
    return {
        make_pair(-inf, -1LL),
        make_pair(-inf, -2LL),
        make_pair(-inf, -3LL),
        make_pair(-inf, -4LL)
    };
}

S single(ll k, ll a) {
    a = max(a, -inf);
    S res = e();
    res[0] = {a, k};
    return res;
}

S add(S s, ll k, ll a) {
    for (int i = 0; i < SZ; i++) {
        if (s[i].second == k) {
            s[i].first = max(s[i].first, a);
            sort(s.rbegin(), s.rend());
            return s;
        }
    }
    array<pair<ll, ll>, SZ + 1> tmp;
    copy(s.begin(), s.end(), tmp.begin());
    tmp[SZ] = {a, k};
    sort(tmp.rbegin(), tmp.rend());
    for (int i = 0; i < SZ; i++) {
        s[i] = tmp[i];
    }
    return s;
}

struct SegTree {
    int n, size;
    vector<S> d;
    SegTree(const vector<S>& v) {
        n = v.size();
        size = 1;
        while (size < n) size <<= 1;
        d.assign(2 * size, e());
        for (int i = 0; i < n; i++) d[size + i] = v[i];
        for (int i = size - 1; i >= 1; i--) d[i] = op(d[2 * i], d[2 * i + 1]);
    }
    void set(int p, S x) {
        p += size;
        d[p] = x;
        while (p > 1) {
            p >>= 1;
            d[p] = op(d[2 * p], d[2 * p + 1]);
        }
    }
    S prod(int l, int r) {
        S sml = e(), smr = e();
        l += size;
        r += size;
        while (l < r) {
            if (l & 1) sml = op(sml, d[l++]);
            if (r & 1) smr = op(d[--r], smr);
            l >>= 1;
            r >>= 1;
        }
        return op(sml, smr);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<ll> k(n), a(n);
    vector<vector<int>> ls(n);
    for (int i = 0; i < n; i++) {
        cin >> k[i] >> a[i];
        --k[i];
        ls[k[i]].push_back(i);
    }

    vector<S> l(n + 1), r(n + 1);
    l[0] = r[n] = e();
    for (int i = 0; i < n; i++) {
        l[i + 1] = add(l[i], k[i], a[i]);
    }
    for (int i = n - 1; i >= 0; i--) {
        r[i] = add(r[i + 1], k[i], a[i]);
    }

    vector<ll> ori(n);
    vector<S> init(n);
    vector<vector<pair<int, ll>>> change(n);
    for (int i = 0; i < n; i++) {
        vector<pair<ll, ll>> cand;
        for (auto p: l[i]) {
            if (p.second != k[i]) cand.push_back(p);
        }
        ori[i] = a[i] + cand[0].first + cand[1].first;
        init[i] = single(k[i], ori[i]);
        for (int j = 0; j < 2; j++) {
            if (cand[j].second < 0) continue;
            ll now = ori[i] - cand[j].first + cand[2].first;
            change[cand[j].second].emplace_back(i, now);
        }
    }

    SegTree st(init);
    ll ans = -1;
    for (int c = 0; c < n; c++) {
        for (auto [i, now]: change[c]) {
            st.set(i, single(k[i], now));
        }
        for (int i: ls[c]) {
            vector<pair<ll, ll>> cand;
            for (auto p: r[i + 1]) {
                if (p.second != k[i]) cand.push_back(p);
            }
            S best = st.prod(0, i);
            for (auto p: best) {
                if (p.second == k[i]) continue;
                ll now;
                if (p.second == cand[0].second) {
                    now = cand[1].first + cand[2].first;
                } else if (p.second == cand[1].second) {
                    now = cand[0].first + cand[2].first;
                } else {
                    now = cand[0].first + cand[1].first;
                }
                now += p.first + a[i];
                ans = max(ans, now);
            }
        }
        for (auto [i, _]: change[c]) {
            st.set(i, single(k[i], ori[i]));
        }
    }

    if (ans < 0) cout << -1 << "\n";
    else cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
