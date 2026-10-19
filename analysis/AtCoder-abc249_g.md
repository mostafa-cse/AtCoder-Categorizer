# Problem Analysis: AtCoder-abc249_g — G - Xor Cards

**Problem ID**: `AtCoder-abc249_g`  
**Contest**: `abc249`  
**Rating / Difficulty**: 2757  
**URL**: https://atcoder.jp/contests/abc249/tasks/abc249_g  
**VJudge Tag**: `[problem:AtCoder-abc249_g]`  
**Category File**: [`../categories/math/xor_cards_linear_basis_prefix.md`](../categories/math/xor_cards_linear_basis_prefix.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Vector Space and XOR Basis`  

---

## 1. Problem Statement & Key Idea
Given N cards with A_i on the front and B_i on the back, choose one or more cards such that XOR(A_i) <= K, maximizing XOR(B_i).

## 2. Core Observation & Invariant
Represent each card as a 60-bit vector (A_i << 30) | B_i and perform Gaussian elimination over GF(2) to obtain a row echelon basis of at most 60 cards. The cards partition into those with A_i != 0 (at most 30 cards, with strictly decreasing MSBs) and those with A_i == 0. When considering whether to pick card i with MSB 2^k, the remaining cards can only affect bits < k. If (A' | (2^k - 1)) <= K, any choice of remaining cards is guaranteed to keep the front XOR <= K, allowing us to freely maximize B using the remaining cards as a linear basis. Otherwise, we uniquely follow the branch that matches bit k of K.

## 3. Step-by-Step Algorithm
1. 1. Insert each (A_i << 30) | B_i into a 60-bit linear basis.
2. 2. Separate the basis into cards with A != 0 and cards with A == 0, sorting cards with A != 0 by MSB descending.
3. 3. Search the unique path of length <= 30 matching the bits of K:
4.    a. If omitting card i guarantees A <= K, greedily maximize B on remaining cards.
5.    b. If choosing card i guarantees A <= K, greedily maximize B on remaining cards.
6.    c. Otherwise, continue along the unique branch matching bit k of K.
7. 4. Enforce the non-empty card selection rule, returning -1 if no non-empty subset is valid.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * W + W^3) where W = 60`
- **Space Complexity**: `O(N + W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Card {
    long long a, b;
};

long long max_B(long long init_B, const vector<long long>& avail_B, bool must_pick_non_empty) {
    vector<long long> basis;
    for (long long x : avail_B) {
        long long val = x;
        for (long long r : basis) {
            val = min(val, val ^ r);
        }
        if (val > 0) {
            basis.push_back(val);
            sort(basis.rbegin(), basis.rend());
        }
    }

    long long cur = init_B;
    bool picked_any = false;
    for (long long r : basis) {
        if ((cur ^ r) > cur) {
            cur ^= r;
            picked_any = true;
        }
    }

    if (must_pick_non_empty && !picked_any) {
        if (basis.empty()) return -1;
        long long best_ne = -1;
        for (long long v : basis) {
            long long val = init_B ^ v;
            for (long long r : basis) {
                if (r != v && (val ^ r) > val) {
                    val ^= r;
                }
            }
            best_ne = max(best_ne, val);
        }
        return best_ne;
    }
    return cur;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> rows;
    bool has_kernel = false;

    for (int i = 0; i < n; ++i) {
        long long a, b;
        cin >> a >> b;
        long long val = (a << 30) | b;
        for (long long r : rows) {
            val = min(val, val ^ r);
        }
        if (val > 0) {
            rows.push_back(val);
            sort(rows.rbegin(), rows.rend());
        } else {
            has_kernel = true;
        }
    }

    vector<Card> cards_A;
    vector<long long> cards_B;

    for (long long val : rows) {
        long long a = val >> 30;
        long long b = val & ((1LL << 30) - 1);
        if (a > 0) {
            cards_A.push_back({a, b});
        } else {
            cards_B.push_back(b);
        }
    }

    // Sort cards_A by leading bit descending
    sort(cards_A.begin(), cards_A.end(), [](const Card& x, const Card& y) {
        return x.a > y.a;
    });

    long long best_ans = -1;

    auto search = [&](auto& self, int i, long long cur_A, long long cur_B, int picked_count) -> void {
        if (i == (int)cards_A.size()) {
            if (cur_A <= k) {
                bool must_ne = (picked_count == 0 && !has_kernel);
                long long val = max_B(cur_B, cards_B, must_ne);
                best_ans = max(best_ans, val);
            }
            return;
        }

        long long a = cards_A[i].a;
        long long b = cards_A[i].b;
        int msb = 0;
        long long temp = a;
        while (temp >>= 1) msb++;
        long long mask = (1LL << msb) - 1;

        // Option 1: do not pick card i
        if ((cur_A | mask) <= k) {
            vector<long long> avail_B;
            for (size_t j = i + 1; j < cards_A.size(); ++j) avail_B.push_back(cards_A[j].b);
            for (long long x : cards_B) avail_B.push_back(x);
            bool must_ne = (picked_count == 0 && !has_kernel);
            long long val = max_B(cur_B, avail_B, must_ne);
            best_ans = max(best_ans, val);
        }

        // Option 2: pick card i
        if (((cur_A ^ a) | mask) <= k) {
            vector<long long> avail_B;
            for (size_t j = i + 1; j < cards_A.size(); ++j) avail_B.push_back(cards_A[j].b);
            for (long long x : cards_B) avail_B.push_back(x);
            long long val = max_B(cur_B ^ b, avail_B, false);
            best_ans = max(best_ans, val);
        }

        int k_bit = (k >> msb) & 1;
        int bit_not_pick = (cur_A >> msb) & 1;
        if (bit_not_pick == k_bit && !((cur_A | mask) <= k)) {
            self(self, i + 1, cur_A, cur_B, picked_count);
        }
        int bit_pick = ((cur_A ^ a) >> msb) & 1;
        if (bit_pick == k_bit && !(((cur_A ^ a) | mask) <= k)) {
            self(self, i + 1, cur_A ^ a, cur_B ^ b, picked_count + 1);
        }
    };

    search(search, 0, 0, 0, 0);

    cout << best_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
