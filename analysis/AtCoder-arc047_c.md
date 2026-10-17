# Problem Analysis: AtCoder-arc047_c — C. N!÷K番目の単語

**Problem ID**: `AtCoder-arc047_c`  
**Contest**: `arc047`  
**Rating / Difficulty**: 2262  
**URL**: https://atcoder.jp/contests/arc047/tasks/arc047_c  
**VJudge Tag**: `[problem:AtCoder-arc047_c]`  
**Category File**: [`../categories/miscellaneous/factorial_number_system_rank_fenwick.md`](../categories/miscellaneous/factorial_number_system_rank_fenwick.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Factorial Number System`  

---

## 1. Problem Statement & Key Idea
We are given integers $N$ ($1 \le N \le 10^5$) and $K$ ($1 \le K \le N$). All $N!$ permutations of $(1, 2, \dots, N)$ are arranged in lexicographical order. We must find the $1$-based $\frac{N!}{K}$-th permutation.

## 2. Core Observation & Invariant
Because $N!$ is astronomical, we represent the rank in the factorial number system (factoradic). At each step with $m$ remaining unchosen elements, the block size of permutations for the current position is $(m-1)!$. The fraction of remaining permutations we seek is maintained as $\frac{rem}{K}$ where $rem < K$. Multiplying by $m$ gives $\frac{rem \times m}{K}$. Its quotient $q = \lfloor \frac{rem \times m}{K} \rfloor$ determines the 0-based choice index among currently available numbers, and the new remainder is $r = (rem \times m) \bmod K$. If $r = 0$, this step lands exactly at the end of block $q-1$, so the current digit is $q-1$ and all subsequent remaining digits take their maximal values $(m-2, m-3, \dots, 0)$. Available numbers are retrieved and removed using a Fenwick Tree with binary lifting in $O(\log N)$.

## 3. Step-by-Step Algorithm
1. Initialize a Fenwick Tree over $[1, N]$ with all elements marked present.
2. Set $rem = 1$ (representing the initial fraction $\frac{1}{K}$ of $N!$).
3. For $m = N, N-1, \dots, 1$:
4. Compute $val = rem \times m, q = val / K, r = val \% K$.
5. If $r == 0$, append digit $q-1$, then append all remaining maximal digits $(m-2, m-3, \dots, 0)$ and break.
6. Otherwise, append digit $q$ and update $rem = r$.
7. For each factoradic digit $d$, query the Fenwick tree using binary lifting for the $d$-th available element, print it, and remove it from the tree.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    int find_kth(int k) { // 0-based k-th available (i.e. prefix sum == k + 1)
        int idx = 0;
        for (int p = 1 << 20; p > 0; p >>= 1) {
            if (idx + p <= n && tree[idx + p] <= k) {
                idx += p;
                k -= tree[idx];
            }
        }
        return idx + 1;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    Fenwick bit(n);
    for (int i = 1; i <= n; ++i) {
        bit.add(i, 1);
    }

    vector<int> digits;
    long long rem = 1;

    for (int m = n; m >= 1; --m) {
        long long val = rem * m;
        long long q = val / k;
        long long r = val % k;
        if (r == 0) {
            digits.push_back((int)(q - 1));
            for (int rem_m = m - 1; rem_m >= 1; --rem_m) {
                digits.push_back(rem_m - 1);
            }
            break;
        } else {
            digits.push_back((int)q);
            rem = r;
        }
    }

    for (int d : digits) {
        int val = bit.find_kth(d);
        cout << val << "\n";
        bit.add(val, -1);
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
