# Problem Analysis: AtCoder-arc050_d — D. Suffix Concat

**Problem ID**: `AtCoder-arc050_d`  
**Contest**: `arc050`  
**Rating / Difficulty**: 2487  
**URL**: https://atcoder.jp/contests/arc050/tasks/arc050_d  
**VJudge Tag**: `[problem:AtCoder-arc050_d]`  
**Category File**: [`../categories/strings/suffix_concat_lcp_sparse_table_suffix_array.md`](../categories/strings/suffix_concat_lcp_sparse_table_suffix_array.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Suffix Structures`  
- **Topic (Skill)**: `Suffix Array`  

---

## 1. Problem Statement & Key Idea
Given a string $S$ of length $N$, sort the $N$ suffixes by comparing the infinite periodic concatenations $S[i \dots N]^\infty$ vs $S[j \dots N]^\infty$, which simplifies to comparing $S_i + S_j$ against $S_j + S_i$ where $S_i = S[i \dots N]$. The string comparison $S_i + S_j < S_j + S_i$ can be evaluated in $O(1)$ time by comparing at most two intervals using Longest Common Prefix (LCP) queries on the Suffix Array with a Sparse Table RMQ.

## 2. Core Observation & Invariant
To compare $S_i + S_j$ and $S_j + S_i$ where $|S_i| < |S_j|$: if $S_i$ is not a prefix of $S_j$, the first $|S_i|$ characters determine the comparison via $LCP(i, j)$. If $S_i$ is a prefix of $S_j$, comparing $S_i + S_j$ with $S_j + S_i$ reduces to comparing $S_j$ with $S_j[|S_i| \dots] + S_i$, which is a second LCP query between $j$ and $j + |S_i|$.

## 3. Step-by-Step Algorithm
1. 1. Construct the Suffix Array, Rank array, and LCP array for string $S$ in $O(N \log N)$ or $O(N)$.
2. 2. Build a Sparse Table over the LCP array to support $O(1)$ RMQ range minimum queries for $LCP(u, v)$.
3. 3. Define a custom comparator for suffix indices $i$ and $j$:
4.    a. Query $l = LCP(i, j)$. If $l < \min(|S_i|, |S_j|)$, compare $S[i + l]$ and $S[j + l]$.
5.    b. If lengths are equal, return false.
6.    c. Otherwise, query $LCP(i + l, j)$ or $LCP(i, j + l)$ to resolve the remainder in $O(1)$.
7. 4. Sort the suffix indices $1 \dots N$ using `std::sort` in $O(N \log N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N \log N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Suffix Array and LCP via doubling
struct SuffixArray {
    int n;
    string s;
    vector<int> sa, rank, lcp;
    vector<vector<int>> st;
    vector<int> lg;

    SuffixArray(const string& s) : s(s), n(s.size()), sa(n), rank(n), lcp(n) {
        build_sa();
        build_lcp();
        build_rmq();
    }

    void build_sa() {
        vector<int> tmp(n);
        for (int i = 0; i < n; ++i) {
            sa[i] = i;
            rank[i] = (unsigned char)s[i];
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
                tmp[sa[i]] = tmp[sa[i - 1]] + (cmp(sa[i - 1], sa[i]) ? 1 : 0);
            }
            rank = tmp;
            if (rank[sa[n - 1]] == n - 1) break;
        }
    }

    void build_lcp() {
        int h = 0;
        for (int i = 0; i < n; ++i) {
            if (rank[i] > 0) {
                int j = sa[rank[i] - 1];
                while (i + h < n && j + h < n && s[i + h] == s[j + h]) h++;
                lcp[rank[i]] = h;
                if (h > 0) h--;
            }
        }
    }

    void build_rmq() {
        lg.assign(n + 1, 0);
        for (int i = 2; i <= n; ++i) lg[i] = lg[i / 2] + 1;
        int K = lg[n] + 1;
        st.assign(K, vector<int>(n));
        for (int i = 0; i < n; ++i) st[0][i] = lcp[i];
        for (int j = 1; j < K; ++j) {
            for (int i = 0; i + (1 << j) <= n; ++i) {
                st[j][i] = min(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
            }
        }
    }

    int get_lcp(int i, int j) {
        if (i == j) return n - i;
        int l = rank[i], r = rank[j];
        if (l > r) swap(l, r);
        int len = r - l;
        int k = lg[len];
        return min(st[k][l + 1], st[k][r - (1 << k) + 1]);
    }

    bool compare_concat(int i, int j) {
        if (i == j) return false;
        int len_i = n - i;
        int len_j = n - j;

        if (len_i == len_j) {
            return rank[i] < rank[j];
        }

        if (len_i < len_j) {
            int l1 = get_lcp(i, j);
            if (l1 < len_i) {
                return s[i + l1] < s[j + l1];
            }
            // S_i is prefix of S_j: compare S_i and S_{j + len_i}
            return compare_concat(i, j + len_i);
        } else {
            // len_i > len_j: opposite of compare_concat(j, i)
            return !compare_concat(j, i);
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    string s;
    cin >> s;

    SuffixArray sa(s);

    vector<int> p(n);
    for (int i = 0; i < n; ++i) p[i] = i;

    sort(p.begin(), p.end(), [&](int i, int j) {
        return sa.compare_concat(i, j);
    });

    for (int i = 0; i < n; ++i) {
        cout << p[i] + 1 << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
