# Problem Analysis: AtCoder-abc237_h — Ex - Hakata

**Problem ID**: `AtCoder-abc237_h`  
**Contest**: `abc237`  
**Rating / Difficulty**: 2807  
**URL**: https://atcoder.jp/contests/abc237/tasks/abc237_h  
**VJudge Tag**: `[problem:AtCoder-abc237_h]`  
**Category File**: [`../categories/graph_theory/palindromic_substrings_dilworth_antichain.md`](../categories/graph_theory/palindromic_substrings_dilworth_antichain.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Partially Ordered Set (POSET)`  
- **Topic (Skill)**: `POSET ft Dilworth's and Mirsky's Theorem`  

---

## 1. Problem Statement & Key Idea
Find the maximum size of a subset of distinct palindromic substrings of S such that no chosen substring is a substring of another chosen substring.

## 2. Core Observation & Invariant
A string of length N has at most N distinct palindromic substrings. Substring inclusion forms a partially ordered set (poset) on these palindromes. The problem seeks the maximum antichain of this poset. By Dilworth's Theorem, the maximum antichain size equals the minimum path cover of the comparability DAG, which is computed via maximum bipartite matching as |P| - max_matching.

## 3. Step-by-Step Algorithm
1. 1. Extract all distinct palindromic substrings using an Eertree or expanding centers + hash set (at most |S| substrings).
2. 2. Construct the containment DAG: directed edge u -> v if palindrome u is a strict substring of palindrome v.
3. 3. Build bipartite graph with vertices L = {1..K} and R = {1..K}, connecting u in L to v in R if u -> v in the transitive closure.
4. 4. Find maximum bipartite matching via Hopcroft-Karp or Dinic.
5. 5. Maximum antichain size = K - max_matching.

## 4. Complexity Analysis
- **Time Complexity**: `O(K^2 * |S| + K^2.5) where K <= |S| <= 200`
- **Space Complexity**: `O(K^2 + |S|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

bool dfs(int u, const vector<vector<int>>& adj, vector<int>& match, vector<bool>& vis) {
    for (int v : adj[u]) {
        if (!vis[v]) {
            vis[v] = true;
            if (match[v] == -1 || dfs(match[v], adj, match, vis)) {
                match[v] = u;
                return true;
            }
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    if (!(cin >> S)) return 0;

    int n = S.size();
    set<string> pal_set;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            string sub = S.substr(i, j - i);
            bool is_pal = true;
            int len = sub.size();
            for (int k = 0; k < len / 2; ++k) {
                if (sub[k] != sub[len - 1 - k]) {
                    is_pal = false;
                    break;
                }
            }
            if (is_pal) {
                pal_set.insert(sub);
            }
        }
    }

    vector<string> pals(pal_set.begin(), pal_set.end());
    int K = pals.size();

    vector<vector<int>> adj(K);
    for (int i = 0; i < K; ++i) {
        for (int j = 0; j < K; ++j) {
            if (i != j && pals[i].size() < pals[j].size()) {
                if (pals[j].find(pals[i]) != string::npos) {
                    adj[i].push_back(j);
                }
            }
        }
    }

    vector<int> match(K, -1);
    int matching_size = 0;
    for (int i = 0; i < K; ++i) {
        vector<bool> vis(K, false);
        if (dfs(i, adj, match, vis)) {
            matching_size++;
        }
    }

    // Dilworth's Theorem: Maximum Antichain = K - Maximum Bipartite Matching
    cout << (K - matching_size) << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
