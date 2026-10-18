# Problem Analysis: AtCoder-abc312_h — Ex. snukesnuke

**Problem ID**: `AtCoder-abc312_h`  
**Contest**: `abc312`  
**Rating / Difficulty**: 2477  
**URL**: https://atcoder.jp/contests/abc312/tasks/abc312_h  
**VJudge Tag**: `[problem:AtCoder-abc312_h]`  
**Category File**: [`../categories/strings/snukesnuke_kmp_primitive_root_harmonic.md`](../categories/strings/snukesnuke_kmp_primitive_root_harmonic.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching`  
- **Topic (Skill)**: `Knuth Morris Pratt (KMP) and Prefix Automaton`  

---

## 1. Problem Statement & Key Idea
For strings $S_1, \dots, S_N$, find the smallest $k \ge 1$ such that $S_i^k$ has not yet been registered, register it, and output $k$.

## 2. Core Observation & Invariant
Any string $S_i$ has a unique primitive root $T$ such that $S_i = T^c$. Two powers $S_i^k$ and $S_j^{k'}$ are identical iff they share the exact same root $T$ and $c_i \cdot k = c_j \cdot k'$. Group strings by primitive root $T$ (found in $O(|S_i|)$ via KMP $\pi$-table). For each multiplicity $c$, advance a pointer `next_k[c]` while $c \cdot k$ is already in the used set. The total work per root is bounded by the harmonic series $\sum M/c = O(M \log M)$.

## 3. Step-by-Step Algorithm
1. 1. For each string $S_i$, compute the KMP $\pi$-array. Let $p = |S_i| - \pi[|S_i|-1]$. If $|S_i| \% p == 0$, $T = S_i[0 \dots p-1]$ and $c = |S_i| / p$; else $T = S_i, c = 1$.
2. 2. Group strings by primitive root $T$ in a hash map.
3. 3. In group $T$, find the smallest $k \ge \text{next\_k}[c]$ such that $c \cdot k \notin \text{used}$.
4. 4. Output $k$, insert $c \cdot k$ into $\text{used}$, and set $\text{next\_k}[c] = k + 1$.
5. 5. Format all answers separated by spaces on a single line.

## 4. Complexity Analysis
- **Time Complexity**: `O(\sum |S_i| + N \log N)`
- **Space Complexity**: `O(\sum |S_i|)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

pair<string, int> get_primitive(const string &s) {
    int n = s.size();
    vector<int> pi(n, 0);
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) j++;
        pi[i] = j;
    }
    int p = n - pi[n - 1];
    if (n % p == 0) {
        return {s.substr(0, p), n / p};
    }
    return {s, 1};
}

struct Group {
    unordered_set<long long> used;
    unordered_map<int, int> next_k;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    unordered_map<string, int> group_map;
    vector<Group> groups;

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        auto prim = get_primitive(s);
        string t = prim.first;
        int c = prim.second;

        if (group_map.find(t) == group_map.end()) {
            group_map[t] = groups.size();
            groups.emplace_back();
        }
        int gid = group_map[t];
        auto &g = groups[gid];

        int k = 1;
        auto it = g.next_k.find(c);
        if (it != g.next_k.end()) k = it->second;

        while (g.used.find(1LL * c * k) != g.used.end()) {
            k++;
        }
        cout << k << (i + 1 == n ? "" : " ");
        g.used.insert(1LL * c * k);
        g.next_k[c] = k + 1;
    }
    cout << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
