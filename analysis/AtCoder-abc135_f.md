# Problem Analysis: AtCoder-abc135_f — F. Strings of Eternity

**Problem ID**: `AtCoder-abc135_f`  
**Contest**: `abc135`  
**Rating / Difficulty**: 2388  
**URL**: https://atcoder.jp/contests/abc135/tasks/abc135_f  
**VJudge Tag**: `[problem:AtCoder-abc135_f]`  
**Category File**: [`../categories/strings/infinite_string_matching_functional_graph_kmp.md`](../categories/strings/infinite_string_matching_functional_graph_kmp.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching`  
- **Topic (Skill)**: `Knuth Morris Pratt (KMP) and Prefix Automaton`  

---

## 1. Problem Statement & Key Idea
Find maximum repetitions of string t inside s^infinity. Repeating s to length >= |t| + |s| and finding match positions via KMP builds a functional graph on starting positions 0 .. |s|-1 with edge p -> (p + |t|) mod |s|. Detecting cycles (outputting -1) or finding the DAG longest path takes O(|s| + |t|) time.

## 2. Core Observation & Invariant
If string t matches in s^infinity at position p in [0, |s|-1], the next consecutive copy of t must start at (p + |t|) mod |s|. This defines a functional graph on |s| vertices where each vertex has out-degree <= 1. An infinite repetition exists iff there is a directed cycle; otherwise the maximum repetition count is the longest path in the DAG.

## 3. Step-by-Step Algorithm
1. Repeat string s to length at least |t| + |s|.
2. Run KMP prefix function on pattern t + '#' + s_repeated to identify all starting match indices p in [0, |s|-1].
3. Build directed edges p -> (p + |t|) mod |s| for all matching positions p.
4. Perform DFS with 3-color states (unvisited, visiting, visited) to detect cycles (outputting -1) or compute memoized longest paths, returning the maximum path length.

## 4. Complexity Analysis
- **Time Complexity**: `O(|s| + |t|)`
- **Space Complexity**: `O(|s| + |t|)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> prefix_function(const string& s) {
    int n = s.size();
    vector<int> pi(n, 0);
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) j++;
        pi[i] = j;
    }
    return pi;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s, t;
    if (!(cin >> s >> t)) return 0;
    int len_s = s.size(), len_t = t.size();

    int reps = (len_t + len_s - 1) / len_s + 2;
    string s_rep = "";
    for (int i = 0; i < reps; ++i) s_rep += s;

    string pattern = t + "#" + s_rep;
    vector<int> pi = prefix_function(pattern);

    vector<bool> match(len_s, false);
    for (size_t i = len_t + 1; i < pattern.size(); ++i) {
        if (pi[i] == len_t) {
            int start_idx_in_srep = i - 2 * len_t;
            if (start_idx_in_srep < len_s) {
                match[start_idx_in_srep] = true;
            }
        }
    }

    vector<int> to(len_s, -1);
    vector<int> in_deg(len_s, 0);
    for (int i = 0; i < len_s; ++i) {
        if (match[i]) {
            to[i] = (i + len_t) % len_s;
            in_deg[to[i]]++;
        }
    }

    // Detect cycle and find longest path
    // 0: unvisited, 1: visiting, 2: visited
    vector<int> state(len_s, 0);
    vector<int> dp(len_s, 0);
    bool has_cycle = false;

    auto dfs = [&](auto& self, int u) -> int {
        state[u] = 1;
        int max_len = 0;
        if (to[u] != -1) {
            int v = to[u];
            if (state[v] == 1) {
                has_cycle = true;
            } else {
                if (state[v] == 0) self(self, v);
                max_len = 1 + dp[v];
            }
        }
        state[u] = 2;
        dp[u] = max_len;
        return dp[u];
    };

    for (int i = 0; i < len_s; ++i) {
        if (state[i] == 0 && match[i]) {
            dfs(dfs, i);
        }
    }

    if (has_cycle) {
        cout << -1 << "\n";
    } else {
        int ans = 0;
        for (int i = 0; i < len_s; ++i) {
            ans = max(ans, dp[i]);
        }
        cout << ans << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
