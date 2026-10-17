# Problem Analysis: AtCoder-arc194_d — D. Reverse Brackets

**Problem ID**: `AtCoder-arc194_d`  
**Contest**: `arc194`  
**Rating / Difficulty**: 2164  
**URL**: https://atcoder.jp/contests/arc194/tasks/arc194_d  
**VJudge Tag**: `[problem:AtCoder-arc194_d]`  
**Category File**: [`../categories/miscellaneous/tree_isomorphism_bracket_multinomial_counting.md`](../categories/miscellaneous/tree_isomorphism_bracket_multinomial_counting.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Tree Isomorphism`  

---

## 1. Problem Statement & Key Idea
Given a valid parenthesis sequence S, reversing balanced subsegments bijects to rooted ordered trees where contiguous reversals generate the full symmetric group of sibling subtrees. Distinct reachable strings correspond to all valid permutations of sibling subtrees, counted via tree isomorphism hashing and multinomial coefficients.

## 2. Core Observation & Invariant
Enclosing S as ( + S + ) forms a single rooted tree where each matched pair () is a node and nested pairs are children. Consecutive reversals of child subsegments allow arbitrary reordering of a node's children. If node u has k children with isomorphism counts c_1, ..., c_m, the number of distinct ordered sequences is k! / (c_1! * ... * c_m!). The total count is the product of these multinomial coefficients across all vertices.

## 3. Step-by-Step Algorithm
1. Parse the bracket sequence into an explicit rooted tree with parent-child adjacency.
2. Traverse bottom-up (post-order DFS) to compute a canonical isomorphism hash/ID for each subtree by sorting the IDs of its children and memoizing in a map<vector<int>, int>.
3. At each node with k children, count multiplicities of isomorphic child subtree IDs, multiplying the answer by k! / prod(c_i!).
4. Compute all factorials and modular inverses under modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    string S;
    cin >> S;

    string s = "(" + S + ")";
    int total_chars = (int)s.size();

    vector<long long> fact(total_chars + 1, 1), inv(total_chars + 1, 1);
    for (int i = 1; i <= total_chars; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[total_chars] = modInverse(fact[total_chars]);
    for (int i = total_chars - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    vector<vector<int>> adj;
    adj.push_back({});
    vector<int> stack = {0};

    for (int i = 1; i < total_chars; ++i) {
        if (s[i] == '(') {
            int new_id = (int)adj.size();
            adj.push_back({});
            adj[stack.back()].push_back(new_id);
            stack.push_back(new_id);
        } else {
            stack.pop_back();
        }
    }

    map<vector<int>, int> memo;
    long long ans = 1;

    auto dfs = [&](auto& self, int u) -> int {
        vector<int> child_labels;
        for (int v : adj[u]) {
            child_labels.push_back(self(self, v));
        }
        int k = (int)child_labels.size();
        sort(child_labels.begin(), child_labels.end());

        long long term = fact[k];
        int count = 0;
        for (int i = 0; i < k; ++i) {
            count++;
            if (i + 1 == k || child_labels[i] != child_labels[i + 1]) {
                term = (term * inv[count]) % MOD;
                count = 0;
            }
        }
        ans = (ans * term) % MOD;

        if (memo.find(child_labels) == memo.end()) {
            int new_label = (int)memo.size() + 1;
            memo[child_labels] = new_label;
        }
        return memo[child_labels];
    };

    dfs(dfs, 0);
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
