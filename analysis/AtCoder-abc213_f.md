# Problem Analysis: AtCoder-abc213_f — Common Prefixes

**Problem ID**: `AtCoder-abc213_f`  
**Contest**: `abc213`  
**Rating / Difficulty**: 2215  
**URL**: https://atcoder.jp/contests/abc213/tasks/abc213_f  
**VJudge Tag**: `[problem:AtCoder-abc213_f]`  
**Category File**: [`../categories/strings/suffix_array_common_prefixes_lcp_monotonic_stack.md`](../categories/strings/suffix_array_common_prefixes_lcp_monotonic_stack.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Suffix Structures`  
- **Topic (Skill)**: `Suffix Array`  

---

## 1. Problem Statement & Key Idea
Compute the sum of longest common prefixes between suffix S_i and all other suffixes S_j for every i in [1, N] for string S of length N <= 10^6.

## 2. Core Observation & Invariant
In the suffix array, LCP(S_i, S_j) is the range minimum of the LCP array between rank(i) and rank(j). The sum of range minimums from rank(i) to all other positions decomposes into left and right prefix contributions, efficiently computed in O(N) using monotonic stacks maintaining running aggregate sums.

## 3. Step-by-Step Algorithm
1. 1. Construct Suffix Array using doubling with 2-pass Radix Sort in O(N log N) time.
2. 2. Construct the LCP array using Kasai's algorithm in O(N) time.
3. 3. Sweep left-to-right over the LCP array with a monotonic stack (value, count) to accumulate left contributions.
4. 4. Sweep right-to-left over the LCP array with a monotonic stack to accumulate right contributions.
5. 5. Combine self-length (N - i) with left and right contributions for each original suffix index.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

// Suffix Array + Kasai's LCP
vector<int> suffix_array(const string& s) {
    int n = s.size();
    vector<int> sa(n), rnk(n), tmp(n);
    for (int i = 0; i < n; i++) {
        sa[i] = i;
        rnk[i] = (unsigned char)s[i];
    }
    sort(sa.begin(), sa.end(), [&](int a, int b) {
        return s[a] < s[b];
    });
    tmp[sa[0]] = 0;
    for (int i = 1; i < n; i++) {
        tmp[sa[i]] = tmp[sa[i - 1]] + (s[sa[i]] != s[sa[i - 1]]);
    }
    rnk = tmp;

    for (int k = 1; k < n; k <<= 1) {
        vector<int> p(n);
        int cur = 0;
        for (int i = n - k; i < n; i++) p[cur++] = i;
        for (int i = 0; i < n; i++) {
            if (sa[i] >= k) p[cur++] = sa[i] - k;
        }

        int max_r = rnk[sa[n - 1]];
        vector<int> head(max_r + 2, 0);
        for (int i = 0; i < n; i++) head[rnk[i] + 1]++;
        for (int i = 0; i <= max_r; i++) head[i + 1] += head[i];
        for (int i = 0; i < n; i++) {
            sa[head[rnk[p[i]]]++] = p[i];
        }

        auto cmp = [&](int i, int j) {
            if (rnk[i] != rnk[j]) return rnk[i] < rnk[j];
            int ri = (i + k < n) ? rnk[i + k] : -1;
            int rj = (j + k < n) ? rnk[j + k] : -1;
            return ri < rj;
        };

        tmp[sa[0]] = 0;
        for (int i = 1; i < n; i++) {
            tmp[sa[i]] = tmp[sa[i - 1]] + (cmp(sa[i - 1], sa[i]) ? 1 : 0);
        }
        rnk = tmp;
        if (rnk[sa[n - 1]] == n - 1) break;
    }
    return sa;
}

vector<int> lcp_array(const string& s, const vector<int>& sa) {
    int n = s.size();
    vector<int> rnk(n);
    for (int i = 0; i < n; i++) rnk[sa[i]] = i;
    vector<int> lcp(n - 1, 0);
    int h = 0;
    for (int i = 0; i < n; i++) {
        if (rnk[i] > 0) {
            int j = sa[rnk[i] - 1];
            while (i + h < n && j + h < n && s[i + h] == s[j + h]) h++;
            lcp[rnk[i] - 1] = h;
            if (h > 0) h--;
        }
    }
    return lcp;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    string s;
    cin >> s;

    vector<int> sa = suffix_array(s);
    vector<int> lcp = lcp_array(s, sa);

    // left contribution to each sa[i]
    vector<long long> left_sum(n, 0);
    {
        vector<pair<long long, long long>> st;
        long long current_total = 0;
        for (int i = 0; i < n - 1; i++) {
            long long v = lcp[i];
            long long cnt = 1;
            while (!st.empty() && st.back().first >= v) {
                current_total -= st.back().first * st.back().second;
                cnt += st.back().second;
                st.pop_back();
            }
            st.push_back({v, cnt});
            current_total += v * cnt;
            left_sum[i + 1] = current_total;
        }
    }

    // right contribution to each sa[i]
    vector<long long> right_sum(n, 0);
    {
        vector<pair<long long, long long>> st;
        long long current_total = 0;
        for (int i = n - 2; i >= 0; i--) {
            long long v = lcp[i];
            long long cnt = 1;
            while (!st.empty() && st.back().first >= v) {
                current_total -= st.back().first * st.back().second;
                cnt += st.back().second;
                st.pop_back();
            }
            st.push_back({v, cnt});
            current_total += v * cnt;
            right_sum[i] = current_total;
        }
    }

    vector<long long> ans(n);
    for (int i = 0; i < n; i++) {
        long long self_len = n - sa[i];
        ans[sa[i]] = self_len + left_sum[i] + right_sum[i];
    }

    for (int i = 0; i < n; i++) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
