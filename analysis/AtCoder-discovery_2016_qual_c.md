# Problem Analysis: AtCoder-discovery_2016_qual_c — C - アメージングな文字列は、きみが作る！

**Problem ID**: `AtCoder-discovery_2016_qual_c`  
**Contest**: `discovery_2016_qual`  
**Rating / Difficulty**: 2527  
**URL**: https://atcoder.jp/contests/discovery_2016_qual/tasks/discovery_2016_qual_c  
**VJudge Tag**: `[problem:AtCoder-discovery_2016_qual_c]`  
**Category File**: [`../categories/strings/amazing_string_suffix_array_prefix_greedy.md`](../categories/strings/amazing_string_suffix_array_prefix_greedy.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Suffix Structures`  
- **Topic (Skill)**: `Suffix Array`  

---

## 1. Problem Statement & Key Idea
Find the lexicographically smallest string obtainable by applying exactly $K$ operations (delete, replace, insert) to string $S$.

## 2. Core Observation & Invariant
If the total count of 'a' in $S$ plus $K$ is at least $|S|$, we can reduce the string to all 'a's of minimal length $\max(1, |S| - K)$. Otherwise, we must maximize the number of leading 'a's. Replacing all non-'a' characters in prefix $S[0 \dots i-1]$ with 'a' and prepending any remaining operations as 'a's produces $K + \text{cnt\_a}(i)$ leading 'a's, provided $\text{cnt\_nona}(i) \le K$. To minimize the resulting string, we select the candidate index $i$ that maximizes leading 'a's and minimizes the remaining suffix $S[i \dots |S|-1]$. The optimal suffix is selected in $O(1)$ using the Suffix Array.

## 3. Step-by-Step Algorithm
1. 1. If $\text{cnt\_a}(S) + K \ge |S|$, output `'a'` repeated $\max(1, |S| - K)$ times.
2. 2. Compute prefix counts of 'a' and non-'a' characters in $S$.
3. 3. Find all indices $i$ with $\text{cnt\_nona}(i) \le K$ that achieve the maximum number of leading 'a's $\max_a$.
4. 4. Build the Suffix Array and rank array of $S$ in $O(|S| \log |S|)$ time.
5. 5. Among all candidate indices $i$, pick the one with the smallest rank in the Suffix Array.
6. 6. Output `'a'` repeated $K + \max_a$ times followed by suffix $S[i \dots |S|-1]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| \log |S|)`
- **Space Complexity**: `O(|S|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Suffix Array using doubling
vector<int> build_sa(const string& S) {
    int n = S.length();
    vector<int> sa(n), rank(n), tmp(n);
    for (int i = 0; i < n; ++i) {
        sa[i] = i;
        rank[i] = S[i];
    }
    for (int k = 1; k < n; k *= 2) {
        auto cmp = [&](int i, int j) {
            if (rank[i] != rank[j]) return rank[i] < rank[j];
            int ri = (i + k < n ? rank[i + k] : -1);
            int rj = (j + k < n ? rank[j + k] : -1);
            return ri < rj;
        };
        sort(sa.begin(), sa.end(), cmp);
        tmp[sa[0]] = 0;
        for (int i = 1; i < n; ++i) {
            tmp[sa[i]] = tmp[sa[i - 1]] + (cmp(sa[i - 1], sa[i]) ? 1 : 0);
        }
        for (int i = 0; i < n; ++i) rank[i] = tmp[i];
        if (rank[sa[n - 1]] == n - 1) break;
    }
    return sa;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    int K;
    if (!(cin >> S >> K)) return 0;
    int N = S.length();

    int cnt_a_tot = 0;
    for (char c : S) if (c == 'a') cnt_a_tot++;

    if (cnt_a_tot + K >= N) {
        int len = max(1, N - K);
        cout << string(len, 'a') << "\n";
        return 0;
    }

    vector<int> pref_nona(N + 1, 0), pref_a(N + 1, 0);
    for (int i = 0; i < N; ++i) {
        pref_nona[i + 1] = pref_nona[i] + (S[i] != 'a' ? 1 : 0);
        pref_a[i + 1] = pref_a[i] + (S[i] == 'a' ? 1 : 0);
    }

    vector<int> valid_i;
    int max_a = -1;
    for (int i = 0; i < N; ++i) {
        if (pref_nona[i] <= K) {
            valid_i.push_back(i);
            max_a = max(max_a, pref_a[i]);
        }
    }

    vector<int> best_cands;
    for (int i : valid_i) {
        if (pref_a[i] == max_a) {
            best_cands.push_back(i);
        }
    }

    // Build suffix array
    vector<int> sa = build_sa(S);
    vector<int> rank(N);
    for (int i = 0; i < N; ++i) rank[sa[i]] = i;

    int best_i = best_cands[0];
    int best_rank = rank[best_i];
    for (int i : best_cands) {
        if (rank[i] < best_rank) {
            best_rank = rank[i];
            best_i = i;
        }
    }

    string ans = string(K + max_a, 'a') + S.substr(best_i);
    cout << ans << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
