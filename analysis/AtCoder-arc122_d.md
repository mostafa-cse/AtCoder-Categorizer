# Problem Analysis: AtCoder-arc122_d — D. XOR Game

**Problem ID**: `AtCoder-arc122_d`  
**Contest**: `arc122`  
**Rating / Difficulty**: 2331  
**URL**: https://atcoder.jp/contests/arc122/tasks/arc122_d  
**VJudge Tag**: `[problem:AtCoder-arc122_d]`  
**Category File**: [`../categories/data_structures/trie_divide_and_conquer_xor_game.md`](../categories/data_structures/trie_divide_and_conquer_xor_game.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Trie`  
- **Topic (Skill)**: `Trie on Strings and Bits`  

---

## 1. Problem Statement & Key Idea
In a game where Alice and Bob pair up $2N$ integers to minimize/maximize the maximum pair XOR, bitwise divide-and-conquer partitions elements by MSB. If both subsets are even, they decouple; if odd, a crossover pair is forced and found via binary Trie in $O(N \log (\max A))$.

## 2. Core Observation & Invariant
Bitwise divide-and-conquer from MSB: if both subsets $S_0, S_1$ have even cardinality, Alice and Bob can pair elements internally without crossing bit $b$, decoupling the subproblems into $\max(\text{solve}(S_0), \text{solve}(S_1))$. If odd, Alice forces a cross, and the minimum possible outcome is $2^b + \min_{x \in S_0, y \in S_1}(x \oplus y)$.

## 3. Step-by-Step Algorithm
1. Recursively solve on bit $b$ from 29 down to 0. Partition the current multiset $S$ into $S_0$ (bit $b=0$) and $S_1$ (bit $b=1$).
2. If $|S_0|$ is even, recursively return $\max(\text{solve}(S_0, b-1), \text{solve}(S_1, b-1))$.
3. If $|S_0|$ is odd, query the minimum XOR pair between $S_0$ and $S_1$ by inserting $S_0$ into a binary Trie and querying each $y \in S_1$ in $O(N \log(\max A))$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log (\max A))`
- **Space Complexity**: `O(N \log (\max A))`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Trie {
    struct Node {
        int next[2];
        Node() {
            next[0] = next[1] = -1;
        }
    };
    vector<Node> t;
    Trie() {
        t.emplace_back();
    }
    void insert(int val, int bit) {
        int u = 0;
        for (int b = bit; b >= 0; --b) {
            int c = (val >> b) & 1;
            if (t[u].next[c] == -1) {
                t[u].next[c] = (int)t.size();
                t.emplace_back();
            }
            u = t[u].next[c];
        }
    }
    int min_xor(int val, int bit) {
        int u = 0;
        int res = 0;
        for (int b = bit; b >= 0; --b) {
            int c = (val >> b) & 1;
            if (t[u].next[c] != -1) {
                u = t[u].next[c];
            } else {
                res |= (1 << b);
                u = t[u].next[1 - c];
            }
        }
        return res;
    }
};

int solve(vector<int> a, int bit) {
    if (a.empty() || bit < 0) return 0;
    vector<int> s0, s1;
    for (int x : a) {
        if ((x >> bit) & 1) s1.push_back(x);
        else s0.push_back(x);
    }
    if (s0.size() % 2 == 0) {
        return max(solve(s0, bit - 1), solve(s1, bit - 1));
    }
    Trie tr;
    for (int x : s0) {
        tr.insert(x, bit - 1);
    }
    int min_cross = (1 << 30) - 1;
    for (int y : s1) {
        min_cross = min(min_cross, tr.min_xor(y, bit - 1));
    }
    return (1 << bit) | min_cross;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(2 * n);
    for (int i = 0; i < 2 * n; ++i) {
        cin >> a[i];
    }

    cout << solve(a, 29) << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
