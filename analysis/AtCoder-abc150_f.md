# Problem Analysis: AtCoder-abc150_f — F. Xor Shift

**Problem ID**: `AtCoder-abc150_f`  
**Contest**: `abc150`  
**Rating / Difficulty**: 2281  
**URL**: https://atcoder.jp/contests/abc150/tasks/abc150_f  
**VJudge Tag**: `[problem:AtCoder-abc150_f]`  
**Category File**: [`../categories/strings/kmp_cyclic_xor_difference_matching.md`](../categories/strings/kmp_cyclic_xor_difference_matching.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching`  
- **Topic (Skill)**: `Knuth Morris Pratt (KMP) and Prefix Automaton`  

---

## 1. Problem Statement & Key Idea
Given two sequences $a$ and $b$ of length $N$, find all pairs $(k, x)$ with $0 \le k < N$ and $0 \le x < 2^{30}$ such that cyclically shifting $a$ left by $k$ positions and bitwise XORing with $x$ yields $b$.

## 2. Core Observation & Invariant
The relation $a_{(i+k) \bmod N} \oplus x = b_i$ eliminates $x$ upon taking adjacent circular XOR differences $A'_j = a_{(j+1) \bmod N} \oplus a_j$ and $B'_i = b_{(i+1) \bmod N} \oplus b_i$. A valid cyclic shift $k$ corresponds exactly to an exact match of pattern $B'$ in the doubled text $A' A'$, found via KMP in $O(N)$.

## 3. Step-by-Step Algorithm
1. 1. The problem asks for all pairs $(k, x)$ such that $a_{(i+k) \bmod N} \oplus x = b_i$ for all $0 \le i < N$.\n2. For $i = 0$, $x = a_k \oplus b_0$. For any adjacent pair of indices, XORing equations gives $a_{(i+1+k) \bmod N} \oplus a_{(i+k) \bmod N} = b_{i+1} \oplus b_i$, completely eliminating $x$.\n3. Define difference sequences $A'_j = a_{(j+1) \bmod N} \oplus a_j$ and $B'_i = b_{(i+1) \bmod N} \oplus b_i$. A shift $k$ is valid if and only if $A'_{(i+k) \bmod N} = B'_i$ for all $0 \le i < N$. Once this holds, setting $x = a_k \oplus b_0$ satisfies all equations by induction.\n4. Finding all valid shifts $k$ is equivalent to finding all occurrences of pattern $B'$ of length $N$ in the doubled text $A' A'$ of length $2N - 1$.\n5. Run the Knuth-Morris-Pratt (KMP) algorithm over integer arrays in $O(N)$ time and space, printing each $(k, a_k \oplus b_0)$ in ascending order of $k$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> compute_pi(const vector<int>& p) {
    int m = p.size();
    vector<int> pi(m, 0);
    for (int i = 1; i < m; i++) {
        int j = pi[i - 1];
        while (j > 0 && p[i] != p[j]) {
            j = pi[j - 1];
        }
        if (p[i] == p[j]) j++;
        pi[i] = j;
    }
    return pi;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    vector<int> diff_a(2 * n);
    vector<int> diff_b(n);

    for (int i = 0; i < n; i++) {
        diff_a[i] = a[(i + 1) % n] ^ a[i];
        diff_a[i + n] = diff_a[i];
        diff_b[i] = b[(i + 1) % n] ^ b[i];
    }

    vector<int> pi = compute_pi(diff_b);

    int j = 0;
    for (int i = 0; i < 2 * n - 1; i++) {
        while (j > 0 && diff_a[i] != diff_b[j]) {
            j = pi[j - 1];
        }
        if (diff_a[i] == diff_b[j]) {
            j++;
        }
        if (j == n) {
            int k = i - n + 1;
            if (k < n) {
                int x = a[k] ^ b[0];
                cout << k << " " << x << "\n";
            }
            j = pi[j - 1];
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
