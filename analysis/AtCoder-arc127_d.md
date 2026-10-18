# Problem Analysis: AtCoder-arc127_d — D. Sum of Min of Xor

**Problem ID**: `AtCoder-arc127_d`  
**Contest**: `arc127`  
**Rating / Difficulty**: 2593  
**URL**: https://atcoder.jp/contests/arc127/tasks/arc127_d  
**VJudge Tag**: `[problem:AtCoder-arc127_d]`  
**Category File**: [`../categories/data_structures/sum_of_min_of_xor_trie_canonical_subcube_dp.md`](../categories/data_structures/sum_of_min_of_xor_trie_canonical_subcube_dp.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Trie`  
- **Topic (Skill)**: `Trie on Strings and Bits`  

---

## 1. Problem Statement & Key Idea
Compute $\sum_{1 \le i < j \le N} \min(A_i \oplus A_j, B_i \oplus B_j)$ for sequences $A$ and $B$ with values $< 2^{18}$.

## 2. Core Observation & Invariant
The bits of $A_i \oplus A_j$ and $B_i \oplus B_j$ match at bit $d$ iff $(A_i \oplus B_i)_d = (A_j \oplus B_j)_d$. Thus, the highest bit where the two XORs differ is the highest bit where $C_i = A_i \oplus B_i$ differs from $C_j$. Splitting by bits of $C$, the choice between $A$ and $B$ is uniquely determined for all cross pairs.

## 3. Step-by-Step Algorithm
1. 1. Compute $C_i = A_i \oplus B_i$ for all $i$.
2. 2. Divide and conquer on bit depth $d = 17 \dots 0$ of $C$.
3. 3. Split indices into $L$ ($(C_i)_d = 0$) and $R$ ($(C_i)_d = 1$).
4. 4. Sub-partition $L$ and $R$ by bit $d$ of $A$. Cross contributions between $(L_0, R_0)$ and $(L_1, R_1)$ use $A$; $(L_0, R_1)$ and $(L_1, R_0)$ use $B$.
5. 5. Compute XOR sums across sets using bitwise frequencies in $O(18)$. Recursively process $L$ and $R$.

## 4. Complexity Analysis
- **Time Complexity**: `O(18^2 \cdot N)`
- **Space Complexity**: `O(18 \cdot N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<int> A(N), B(N), C(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];
    for (int i = 0; i < N; ++i) C[i] = A[i] ^ B[i];

    long long total_ans = 0;

    auto calc_cross_sum = [&](const vector<int>& U, const vector<int>& V, const vector<int>& arr) -> long long {
        if (U.empty() || V.empty()) return 0;
        long long u_len = U.size();
        long long v_len = V.size();
        long long res = 0;
        for (int b = 0; b < 18; ++b) {
            long long u_ones = 0;
            for (int i : U) if ((arr[i] >> b) & 1) u_ones++;
            long long v_ones = 0;
            for (int j : V) if ((arr[j] >> b) & 1) v_ones++;
            long long u_zeros = u_len - u_ones;
            long long v_zeros = v_len - v_ones;
            long long diff_pairs = u_ones * v_zeros + u_zeros * v_ones;
            res += (1LL << b) * diff_pairs;
        }
        return res;
    };

    auto rec = [&](auto& self, const vector<int>& indices, int d) -> void {
        if (indices.size() <= 1) return;
        if (d < 0) {
            long long m = indices.size();
            for (int b = 0; b < 18; ++b) {
                long long ones = 0;
                for (int i : indices) if ((A[i] >> b) & 1) ones++;
                long long zeros = m - ones;
                total_ans += (1LL << b) * (ones * zeros);
            }
            return;
        }

        vector<int> L, R;
        for (int i : indices) {
            if ((C[i] >> d) & 1) R.push_back(i);
            else L.push_back(i);
        }

        if (!L.empty() && !R.empty()) {
            vector<int> L0, L1, R0, R1;
            for (int i : L) {
                if ((A[i] >> d) & 1) L1.push_back(i);
                else L0.push_back(i);
            }
            for (int j : R) {
                if ((A[j] >> d) & 1) R1.push_back(j);
                else R0.push_back(j);
            }

            total_ans += calc_cross_sum(L0, R0, A);
            total_ans += calc_cross_sum(L0, R1, B);
            total_ans += calc_cross_sum(L1, R0, B);
            total_ans += calc_cross_sum(L1, R1, A);
        }

        self(self, L, d - 1);
        self(self, R, d - 1);
    };

    vector<int> all_indices(N);
    for (int i = 0; i < N; ++i) all_indices[i] = i;
    rec(rec, all_indices, 17);

    cout << total_ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
