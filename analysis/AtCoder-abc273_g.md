# Problem Analysis: AtCoder-abc273_g — G. Row Column Sums 2

**Problem ID**: `AtCoder-abc273_g`  
**Contest**: `abc273`  
**Rating / Difficulty**: 2521  
**URL**: https://atcoder.jp/contests/abc273/tasks/abc273_g  
**VJudge Tag**: `[problem:AtCoder-abc273_g]`  
**Category File**: [`../categories/math/row_column_sums_2_generating_functions_dp.md`](../categories/math/row_column_sums_2_generating_functions_dp.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Generating Functions`  

---

## 1. Problem Statement & Key Idea
Count $N \times N$ matrices with entries in $\{0, 1, 2\}$ having prescribed row sums $R_i \in \{0, 1, 2\}$ and column sums $C_j \in \{0, 1, 2\}$. If $\sum R_i \ne \sum C_j$, the answer is 0. Since rows and columns are symmetric with respect to their sum values, count the number of rows with sum 1 ($r_1$) and sum 2 ($r_2$), and process columns sequentially.

## 2. Core Observation & Invariant
During column processing, track the number of rows $j$ that still need 2 points. The number of rows that still need 1 point is uniquely determined by $\text{remaining\_sum} - 2j$. When placing a column with sum 0, 1, or 2, choose which rows receive 1 or 2 points, updating $j$. Transition coefficients are simple binomial coefficients representing choices among available rows.

## 3. Step-by-Step Algorithm
1. 1. Count $r_1, r_2$ from row sums, and $c_1, c_2$ from column sums.
2. 2. If $\sum R_i \ne \sum C_j$, output 0.
3. 3. Initialize $DP[r_2] = 1$, all other $DP[j] = 0$.
4. 4. Process all columns with sum 2 ($c_2$ columns):
5.    - Transition from $j$ rows needing 2: can place a 2 into one row needing 2 ($j \to j - 1$); place two 1s into two rows needing 2 ($j \to j - 2$); place one 1 in row needing 2 and one 1 in row needing 1 ($j \to j - 1$); or place two 1s into rows needing 1 ($j \to j$).
6. 5. Process all columns with sum 1 ($c_1$ columns):
7.    - Place a 1 in a row needing 2 ($j \to j - 1$), or place a 1 in a row needing 1 ($j \to j$).
8. 6. Final answer is $DP[0] \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O((c_1 + c_2) \cdot r_2) = O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> r(n), c(n);
    long long sum_r = 0, sum_c = 0;
    int r1 = 0, r2 = 0;
    for (int i = 0; i < n; ++i) {
        cin >> r[i];
        sum_r += r[i];
        if (r[i] == 1) r1++;
        else if (r[i] == 2) r2++;
    }

    int c1 = 0, c2 = 0;
    for (int i = 0; i < n; ++i) {
        cin >> c[i];
        sum_c += c[i];
        if (c[i] == 1) c1++;
        else if (c[i] == 2) c2++;
    }

    if (sum_r != sum_c) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> dp(r2 + 1, 0);
    dp[r2] = 1;

    vector<int> cols;
    cols.reserve(c2 + c1);
    for (int i = 0; i < c2; ++i) cols.push_back(2);
    for (int i = 0; i < c1; ++i) cols.push_back(1);

    long long rem_sum = sum_c;

    for (int col : cols) {
        vector<long long> nxt(r2 + 1, 0);
        for (int j = 0; j <= r2; ++j) {
            long long ways = dp[j];
            if (!ways) continue;

            long long cur_r1 = rem_sum - 2LL * j;
            if (cur_r1 < 0) continue;

            if (col == 1) {
                if (cur_r1 > 0) {
                    nxt[j] = (nxt[j] + ways * (cur_r1 % MOD)) % MOD;
                }
                if (j > 0) {
                    nxt[j - 1] = (nxt[j - 1] + ways * j) % MOD;
                }
            } else {
                if (j > 0) {
                    nxt[j - 1] = (nxt[j - 1] + ways * j) % MOD;
                }
                if (cur_r1 >= 2) {
                    long long cnt = (cur_r1 * (cur_r1 - 1) / 2) % MOD;
                    nxt[j] = (nxt[j] + ways * cnt) % MOD;
                }
                if (cur_r1 >= 1 && j >= 1) {
                    long long cnt = (cur_r1 * j) % MOD;
                    nxt[j - 1] = (nxt[j - 1] + ways * cnt) % MOD;
                }
                if (j >= 2) {
                    long long cnt = ((long long)j * (j - 1) / 2) % MOD;
                    nxt[j - 2] = (nxt[j - 2] + ways * cnt) % MOD;
                }
            }
        }
        dp = move(nxt);
        rem_sum -= col;
    }

    cout << dp[0] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
