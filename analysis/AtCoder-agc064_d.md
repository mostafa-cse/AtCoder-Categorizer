# Problem Analysis: AtCoder-agc064_d — D - Red and Blue Chips

**Problem ID**: `AtCoder-agc064_d`  
**Contest**: `agc064`  
**Rating / Difficulty**: 2808  
**URL**: https://atcoder.jp/contests/agc064/tasks/agc064_d  
**VJudge Tag**: `[problem:AtCoder-agc064_d]`  
**Category File**: [`../categories/miscellaneous/colored_chips_functional_graph_cycles.md`](../categories/miscellaneous/colored_chips_functional_graph_cycles.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Functional Graphs`  

---

## 1. Problem Statement & Key Idea
Given an N-character string S of R and B chips with square N guaranteed to be blue, chips at square i are repeatedly merged onto higher-indexed blue squares j. Determine the number of distinct color sequences in the final stack at square N modulo 998244353.

## 2. Core Observation & Invariant
Deleting the last B and stripping trailing Rs leaves S = R^{c_B} B ... R^{c_1} B. The final pile corresponds to partitioning the R chips into B blocks of sizes (l_1, ..., l_B) extracted greedily. Sorting l into descending order l'_1 >= ... >= l'_B >= 0, dominance inequalities require sum_{q=0}^p l'_q >= sum_{q=0}^p c_q for all p, where l'_0 = R - sum l'_i. Equivalently, the suffix sums of l' are bounded by the suffix sums of c. Counting permutations with multiplicity factor B! / prod(f_i!) reduces to an integer partition DP in O(R^3) time.

## 3. Step-by-Step Algorithm
1. 1. Strip the final 'B' and all trailing 'R's from S. If empty or no 'B' remains, return 1.
2. 2. Split the remaining string by 'B' to extract block sizes c_1, ..., c_B of 'R's and compute total R.
3. 3. Compute suffix sums suf_c[m] = sum_{q=B-m+1}^B c_q.
4. 4. Define dp[m][s] as the coefficient sum over placing m elements with sum s <= suf_c[m].
5. 5. For each value v from 0 to R, transition by choosing cnt copies of v, updating next_dp[m + cnt][s + cnt * v] += dp[m][s] / cnt!.
6. 6. Multiply dp[B][s] by B! and sum over valid total sums s <= suf_c[B] modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(R^3) = O(N^3)`
- **Space Complexity**: `O(B * R) = O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <numeric>

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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    string s;
    cin >> s;

    // Delete last 'B'
    size_t last_b = s.rfind('B');
    if (last_b == string::npos) {
        cout << 1 << "\n";
        return 0;
    }
    s = s.substr(0, last_b);

    // Strip trailing 'R's
    while (!s.empty() && s.back() == 'R') {
        s.pop_back();
    }
    if (s.empty() || s.find('B') == string::npos) {
        cout << 1 << "\n";
        return 0;
    }

    // Split by 'B'
    // S = R^{c_B} B R^{c_{B-1}} B ... R^{c_1} B
    vector<int> c_list;
    int current_r = 0;
    for (char ch : s) {
        if (ch == 'R') {
            current_r++;
        } else {
            c_list.push_back(current_r);
            current_r = 0;
        }
    }
    int B = (int)c_list.size();
    vector<int> c(B + 1, 0);
    for (int i = 1; i <= B; ++i) {
        c[i] = c_list[B - i];
    }
    int R = 0;
    for (int i = 1; i <= B; ++i) R += c[i];

    vector<int> suf_c(B + 1, 0);
    for (int m = 1; m <= B; ++m) {
        suf_c[m] = suf_c[m - 1] + c[B - m + 1];
    }

    vector<long long> fact(B + 1, 1), inv(B + 1, 1);
    for (int i = 1; i <= B; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[B] = modInverse(fact[B]);
    for (int i = B - 1; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    // dp[m][s]
    vector<vector<int>> dp(B + 1, vector<int>(R + 1, 0));
    // For v = 0, we can take cnt copies of 0:
    for (int cnt = 0; cnt <= B; ++cnt) {
        dp[cnt][0] = inv[cnt];
    }

    for (int v = 1; v <= R; ++v) {
        vector<vector<int>> next_dp = dp;
        for (int cnt = 1; cnt <= B && cnt * v <= R; ++cnt) {
            long long term = inv[cnt];
            int v_sum = cnt * v;
            for (int m = 0; m <= B - cnt; ++m) {
                int max_s = suf_c[m];
                int nm = m + cnt;
                int max_ns = suf_c[nm];
                for (int s = 0; s <= max_s; ++s) {
                    if (!dp[m][s]) continue;
                    int ns = s + v_sum;
                    if (ns <= max_ns) {
                        next_dp[nm][ns] = (next_dp[nm][ns] + dp[m][s] * term) % MOD;
                    }
                }
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int s = 0; s <= suf_c[B]; ++s) {
        ans = (ans + dp[B][s]) % MOD;
    }
    ans = (ans * fact[B]) % MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
