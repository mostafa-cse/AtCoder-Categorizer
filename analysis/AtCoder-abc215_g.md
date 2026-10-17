# Problem Analysis: AtCoder-abc215_g — G. Colorful Candies 2

**Problem ID**: `AtCoder-abc215_g`  
**Contest**: `abc215`  
**Rating / Difficulty**: 2276  
**URL**: https://atcoder.jp/contests/abc215/tasks/abc215_g  
**VJudge Tag**: `[problem:AtCoder-abc215_g]`  
**Category File**: [`../categories/math/expected_distinct_colors_hypergeometric_frequency_compression.md`](../categories/math/expected_distinct_colors_hypergeometric_frequency_compression.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Given $N$ colored candies with color frequencies $c_1, \dots, c_m$, for each $k = 1, \dots, N$, compute the expected number of distinct colors when choosing $k$ candies uniformly at random modulo 998244353.

## 2. Core Observation & Invariant
By linearity of expectation, the expected number of distinct colors in a sample of size $K$ equals the sum of probabilities that each color is present: $E[C] = \sum_{c} (1 - \binom{N - cnt_c}{K} / \binom{N}{K})$. Grouping colors by frequency compresses the evaluation to at most $\sqrt{2N}$ unique sizes.

## 3. Step-by-Step Algorithm
1. 1. Express the expected number of distinct colors using indicator random variables for each color: $E_K = \sum_{c} P(\text{color } c \text{ is chosen})$.\n2. The probability of choosing color $c$ when sampling $K$ candies uniformly without replacement is $1 - \frac{\binom{N - cnt_c}{K}}{\binom{N}{K}}$, where $cnt_c$ is the number of candies of color $c$.\n3. Summing across all colors gives $E_K = (\text{total distinct colors}) - \frac{1}{\binom{N}{K}} \sum_{c} \binom{N - cnt_c}{K}$.\n4. Since $\sum_{c} cnt_c = N$, the number of distinct frequency values $s \in \{cnt_c\}$ is bounded by $\sqrt{2N} \approx 316$. We compress the sum to $\sum_{s} \text{freq}[s] \cdot \binom{N - s}{K}$, where $\text{freq}[s]$ is the number of colors appearing exactly $s$ times.\n5. For each $K = 1, \dots, N$, compute the sum over all non-zero frequencies in $O(\sqrt{N})$ time. Total time complexity is $O(N \sqrt{N})$, completing comfortably within 0.1s.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \sqrt{N})`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

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

const int MAXN = 50005;
long long fact[MAXN];
long long invFact[MAXN];

void init_fact() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAXN; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAXN - 1] = modInverse(fact[MAXN - 1]);
    for (int i = MAXN - 2; i >= 1; i--) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    init_fact();

    int n;
    if (!(cin >> n)) return 0;

    map<int, int> color_count;
    for (int i = 0; i < n; i++) {
        int c;
        cin >> c;
        color_count[c]++;
    }

    int total_colors = color_count.size();
    map<int, int> freq_count;
    for (auto const& [col, cnt] : color_count) {
        freq_count[cnt]++;
    }

    vector<pair<int, int>> freqs(freq_count.begin(), freq_count.end());

    for (int k = 1; k <= n; k++) {
        long long inv_ways = modInverse(nCr(n, k));
        long long sum_unselected = 0;
        for (auto const& [s, num_cols] : freqs) {
            long long ways = nCr(n - s, k);
            if (ways > 0) {
                sum_unselected = (sum_unselected + 1LL * num_cols * ways) % MOD;
            }
        }
        long long unselected_prob = (sum_unselected * inv_ways) % MOD;
        long long ans = (total_colors - unselected_prob + MOD) % MOD;
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
