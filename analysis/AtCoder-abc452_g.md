# Problem Analysis: AtCoder-abc452_g — G. 221 Substring

**Problem ID**: `AtCoder-abc452_g`  
**Contest**: `abc452`  
**Rating / Difficulty**: 2255  
**URL**: https://atcoder.jp/contests/abc452/tasks/abc452_g  
**VJudge Tag**: `[problem:AtCoder-abc452_g]`  
**Category File**: [`../categories/strings/rle_suffix_array_lcp_distinct_221_substrings.md`](../categories/strings/rle_suffix_array_lcp_distinct_221_substrings.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Suffix Structures`  
- **Topic (Skill)**: `Suffix Array`  

---

## 1. Problem Statement & Key Idea
A 221-sequence is a sequence where every run-length encoding block $(v, m)$ has $v = m$. Count the number of distinct 221-sequences that appear as contiguous subsequences of $A$.

## 2. Core Observation & Invariant
In any valid 221 contiguous subsequence, interior blocks must satisfy $v_i = m_i$, while endpoint blocks can take $v$ elements from a block of length $m \ge v$. Transforming the RLE of $A$ into string $T$ by mapping $(v, m)$ to $(0)$ if $v > m$, $(v)$ if $v = m$, and $(v, 0, v)$ if $v < m$ establishes a bijection between 221-sequences and contiguous subarrays of $T$ that contain no 0. Counting distinct 0-free subarrays is solved via Suffix Array and LCP array.

## 3. Step-by-Step Algorithm
1. Compress $A$ into its run-length encoding.
2. Construct string $T$ according to the 0-separator transformation.
3. Compute the Suffix Array and LCP array of $T$.
4. For each suffix $k$ with starting index $p_k$, compute $\max(0, zerofree[p_k] - lcp[k])$ where $zerofree[p_k]$ is the count of non-zero elements until the next 0.
5. Sum these contributions to get the answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(|T| \log |T|)`
- **Space Complexity**: `O(|T|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

// Suffix Array doubling + Kasai's LCP algorithm
vector<int> build_sa(const vector<int>& s) {
    int n = s.size();
    vector<int> sa(n), rank(n), tmp(n);
    iota(sa.begin(), sa.end(), 0);
    sort(sa.begin(), sa.end(), [&](int i, int j) {
        return s[i] < s[j];
    });

    rank[sa[0]] = 0;
    for (int i = 1; i < n; ++i) {
        rank[sa[i]] = rank[sa[i - 1]] + (s[sa[i]] != s[sa[i - 1]]);
    }

    for (int k = 1; k < n; k <<= 1) {
        auto cmp = [&](int i, int j) {
            if (rank[i] != rank[j]) return rank[i] < rank[j];
            int ri = i + k < n ? rank[i + k] : -1;
            int rj = j + k < n ? rank[j + k] : -1;
            return ri < rj;
        };
        sort(sa.begin(), sa.end(), cmp);
        tmp[sa[0]] = 0;
        for (int i = 1; i < n; ++i) {
            tmp[sa[i]] = tmp[sa[i - 1]] + cmp(sa[i - 1], sa[i]);
        }
        rank = tmp;
        if (rank[sa.back()] == n - 1) break;
    }
    return sa;
}

vector<int> build_lcp(const vector<int>& s, const vector<int>& sa) {
    int n = s.size();
    vector<int> rank(n), lcp(n, 0);
    for (int i = 0; i < n; ++i) rank[sa[i]] = i;

    int h = 0;
    for (int i = 0; i < n; ++i) {
        if (rank[i] > 0) {
            int j = sa[rank[i] - 1];
            while (i + h < n && j + h < n && s[i + h] == s[j + h]) h++;
            lcp[rank[i]] = h;
            if (h > 0) h--;
        }
    }
    return lcp;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    vector<pair<int, int>> rle;
    int i = 0;
    while (i < N) {
        int j = i;
        while (j < N && A[j] == A[i]) j++;
        rle.push_back({A[i], j - i});
        i = j;
    }

    vector<int> T;
    for (auto [v, m] : rle) {
        if (v > m) {
            T.push_back(0);
        } else if (v == m) {
            T.push_back(v);
        } else {
            T.push_back(v);
            T.push_back(0);
            T.push_back(v);
        }
    }

    int M = T.size();
    if (M == 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<int> zerofree(M);
    int run = 0;
    for (int k = M - 1; k >= 0; --k) {
        if (T[k] == 0) {
            run = 0;
        } else {
            run++;
        }
        zerofree[k] = run;
    }

    vector<int> sa = build_sa(T);
    vector<int> lcp = build_lcp(T, sa);

    long long ans = 0;
    for (int k = 0; k < M; ++k) {
        int p = sa[k];
        int zf = zerofree[p];
        int match = lcp[k];
        if (zf > match) {
            ans += (zf - match);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
