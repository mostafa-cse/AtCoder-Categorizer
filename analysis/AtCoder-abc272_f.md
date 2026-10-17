# Problem Analysis: AtCoder-abc272_f — Two Strings

**Problem ID**: `AtCoder-abc272_f`  
**Contest**: `abc272`  
**Rating / Difficulty**: 2238  
**URL**: https://atcoder.jp/contests/abc272/tasks/abc272_f  
**VJudge Tag**: `[problem:AtCoder-abc272_f]`  
**Category File**: [`../categories/strings/suffix_array_cyclic_shifts_comparison_two_strings.md`](../categories/strings/suffix_array_cyclic_shifts_comparison_two_strings.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Suffix Structures`  
- **Topic (Skill)**: `Suffix Array`  

---

## 1. Problem Statement & Key Idea
Count pairs (i, j) of cyclic shifts of strings S and T of length N <= 2 * 10^5 such that shift i of S is lexicographically <= shift j of T.

## 2. Core Observation & Invariant
Every cyclic shift of S is a length-N prefix of a suffix of S + S starting at index i in [0, N-1], and similarly for T. Construct concatenated string X = S + S + 0^N + T + T + 200^N + sentinel where delimiters guarantee that identical length-N prefixes are broken with S strictly before T. In the suffix array of X, shift i of S is <= shift j of T iff suffix i precedes suffix (3N + j) in the suffix array. A single linear sweep over the suffix array counts valid pairs.

## 3. Step-by-Step Algorithm
1. 1. Construct integer array representing S + S, followed by N zeros (value 1), T + T, N high sentinels (value 50), and terminal 0.
2. 2. Compute the Suffix Array of this length 6N + 1 sequence using O(L log L) prefix doubling.
3. 3. Sweep through the suffix array maintaining a running count cnt_S of S-suffixes (indices in [0, N-1]).
4. 4. Whenever a T-suffix is encountered (indices in [3N, 4N-1]), add cnt_S to the answer.
5. 5. Output total count.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

// O(L log L) Suffix Array via prefix doubling and counting sort
vector<int> build_sa(const vector<int>& s, int alphabet_size) {
    int n = s.size();
    vector<int> sa(n), rnk(n), head(max(n, alphabet_size) + 1, 0);

    for (int i = 0; i < n; ++i) head[s[i] + 1]++;
    for (int i = 1; i <= alphabet_size; ++i) head[i] += head[i - 1];
    for (int i = 0; i < n; ++i) sa[head[s[i]]++] = i;

    rnk[sa[0]] = 0;
    for (int i = 1; i < n; ++i) {
        rnk[sa[i]] = rnk[sa[i - 1]] + (s[sa[i]] != s[sa[i - 1]]);
    }

    for (int len = 1; len < n; len <<= 1) {
        vector<int> p(n);
        int cur = 0;
        for (int i = n - len; i < n; ++i) p[cur++] = i;
        for (int i = 0; i < n; ++i) {
            if (sa[i] >= len) p[cur++] = sa[i] - len;
        }

        fill(head.begin(), head.begin() + n + 1, 0);
        for (int i = 0; i < n; ++i) head[rnk[p[i]] + 1]++;
        for (int i = 1; i <= n; ++i) head[i] += head[i - 1];
        for (int i = 0; i < n; ++i) sa[head[rnk[p[i]]]++] = p[i];

        vector<int> new_rnk(n);
        new_rnk[sa[0]] = 0;
        for (int i = 1; i < n; ++i) {
            pair<int, int> prev = {rnk[sa[i - 1]], (sa[i - 1] + len < n ? rnk[sa[i - 1] + len] : -1)};
            pair<int, int> now = {rnk[sa[i]], (sa[i] + len < n ? rnk[sa[i] + len] : -1)};
            new_rnk[sa[i]] = new_rnk[sa[i - 1]] + (prev != now);
        }
        rnk = move(new_rnk);
        if (rnk[sa.back()] == n - 1) break;
    }
    return sa;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    string S, T;
    cin >> S >> T;

    // Build vector:
    // S + S (2N)
    // N zeros (value 1, below 'a')
    // T + T (2N)
    // N large (value 200, above 'z')
    // 1 sentinel 0 (value 0, smallest)
    // Shift chars: 'a'..'z' -> 2..27
    vector<int> vec;
    vec.reserve(6 * n + 1);

    for (char c : S) vec.push_back((c - 'a') + 2);
    for (char c : S) vec.push_back((c - 'a') + 2);
    for (int i = 0; i < n; ++i) vec.push_back(1);

    int T_offset = vec.size();
    for (char c : T) vec.push_back((c - 'a') + 2);
    for (char c : T) vec.push_back((c - 'a') + 2);
    for (int i = 0; i < n; ++i) vec.push_back(50);

    vec.push_back(0); // smallest sentinel

    int alphabet_size = 55;
    vector<int> sa = build_sa(vec, alphabet_size);

    long long cnt_S = 0;
    long long ans = 0;

    for (int idx : sa) {
        if (idx < n) {
            cnt_S++;
        } else if (idx >= T_offset && idx < T_offset + n) {
            ans += cnt_S;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
