# Problem Analysis: AtCoder-arc145_d — D. Non Arithmetic Progression Set

**Problem ID**: `AtCoder-arc145_d`  
**Contest**: `arc145`  
**Rating / Difficulty**: 2297  
**URL**: https://atcoder.jp/contests/arc145/tasks/arc145_d  
**VJudge Tag**: `[problem:AtCoder-arc145_d]`  
**Category File**: [`../categories/basics/constructive_3_free_set_ternary.md`](../categories/basics/constructive_3_free_set_ternary.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Construct a set of $N$ distinct integers in $[-10^7, 10^7]$ with sum $M$ such that no three elements form an arithmetic progression.

## 2. Core Observation & Invariant
In base 3, any subset whose ternary digits consist strictly of $\{0, 1\}$ contains no 3-term arithmetic progression because $2b = a + c$ forces $a_i = b_i = c_i$ at every ternary digit. Appending a sufficiently large element $X > 2 \max(S')$ and shifting the entire set uniformly preserves the 3-AP free invariant while achieving the exact target sum $M$.

## 3. Step-by-Step Algorithm
1. 1. We need to construct a set of $N$ distinct integers in $[-10^7, 10^7]$ with sum $M$ such that no three elements form an arithmetic progression ($x + z = 2y$).
2. 2. The classic Cantor-like construction selects integers whose base-3 representations only use digits $\{0, 1\}$. In base 3, $2y$ only has digits in $\{0, 2\}$. Since $x, z$ have digits in $\{0, 1\}$, $x_i + z_i = 2 y_i$ without carrying, forcing $x_i = z_i = y_i$ for all $i$, so $x = y = z$. Hence this set is strictly 3-AP free.
3. 3. Take the first $N - 1$ such numbers $S' = \{s_1, \dots, s_{N-1}\}$. For $N \le 10000$, the $(N-1)$-th number in binary-to-ternary is bounded by $K \approx 2.4 \times 10^6$.
4. 4. To choose the $N$-th number $X$ without creating an AP:
5.    - Pick $X > 2K$. Then $x + z \le 2K < 2X$, and $x + X > 2K \ge 2y$ for any $x, y, z \in S'$, so $X$ can never participate in any 3-term AP with elements of $S'!
6.    - To match sum $M$, we choose $X \equiv M - \sum S' \pmod N$ with $X > 2K$.
7. 5. Shift all $N$ elements by $C = (M - (\sum S' + X)) / N$. Shifting preserves differences and thus preserves the 3-AP free property. All values remain well within $[-10^7, 10^7]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, M;
    if (!(cin >> N >> M)) return 0;

    if (N == 1) {
        cout << M << "\n";
        return 0;
    }

    vector<long long> S;
    S.reserve(N);

    // Generate first N - 1 ternary numbers using digits {0, 1}
    for (int i = 0; (int)S.size() < N - 1; ++i) {
        long long val = 0;
        long long power3 = 1;
        int temp = i;
        while (temp > 0) {
            if (temp & 1) {
                val += power3;
            }
            power3 *= 3;
            temp >>= 1;
        }
        S.push_back(val);
    }

    long long sum_S = 0;
    long long max_val = 0;
    for (long long x : S) {
        sum_S += x;
        max_val = max(max_val, x);
    }

    // Pick X > 2 * max_val such that X = (M - sum_S) mod N
    long long rem = (M - sum_S) % N;
    if (rem < 0) rem += N;

    long long X = 2 * max_val + 1;
    long long cur_rem = X % N;
    long long diff = (rem - cur_rem + N) % N;
    X += diff;

    S.push_back(X);
    sum_S += X;

    long long shift = (M - sum_S) / N;
    for (int i = 0; i < N; ++i) {
        S[i] += shift;
    }

    for (int i = 0; i < N; ++i) {
        cout << S[i] << (i == N - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
