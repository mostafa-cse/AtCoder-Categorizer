# Problem Analysis: AtCoder-abc459_f — -1, +1

**Problem ID**: `AtCoder-abc459_f`  
**Contest**: `abc459`  
**Rating / Difficulty**: 2163  
**URL**: https://atcoder.jp/contests/abc459/tasks/abc459_f  
**VJudge Tag**: `[problem:AtCoder-abc459_f]`  
**Category File**: [`../categories/basics/monotonic_block_merging_sequence_equalization.md`](../categories/basics/monotonic_block_merging_sequence_equalization.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Minimum operations (A_i - 1, A_{i+1} + 1) to make A strictly increasing. Transformed to non-decreasing via A_i <- A_i - i. Solved via monotonic block merging in O(N).

## 2. Core Observation & Invariant
Under A_i <- A_i - i, the target sequence B must be non-decreasing. An operation at i increases the index-weighted sum sum_{j=0}^{N-1} j * A_j by exactly 1 while keeping sum A_j invariant. Within each leveled block of size len and sum s, elements are B_j = floor((s + j) / len). Monotonically merge adjacent blocks whenever left_max > right_min.

## 3. Step-by-Step Algorithm
1. Transform A_i = A_i - i for all 0 <= i < N.
2. Maintain a stack of blocks (len, sum). For each element, push (1, A_i).
3. While stack top has left_max = floor((tail.sum + tail.len - 1) / tail.len) > right_min = floor(now.sum / now.len), merge now with tail.
4. Reconstruct final sequence B from the merged blocks.
5. Total operations equals sum_{i=0}^{N-1} i * (B_i - A_i).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Block {
    long long len;
    long long sum;
};

void solve() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] -= i;
    }

    vector<Block> st;
    auto floor_div = [](long long num, long long den) {
        long long res = num / den;
        long long rem = num % den;
        if (rem != 0 && ((num < 0) ^ (den < 0))) res--;
        return res;
    };

    for (int i = 0; i < n; ++i) {
        Block now = {1, a[i]};
        while (!st.empty()) {
            Block tail = st.back();
            long long left_max = floor_div(tail.sum + tail.len - 1, tail.len);
            long long right_min = floor_div(now.sum, now.len);

            if (left_max <= right_min) break;

            now.len += tail.len;
            now.sum += tail.sum;
            st.pop_back();
        }
        st.push_back(now);
    }

    unsigned long long ans = 0;
    int cur_idx = 0;

    for (const auto& blk : st) {
        for (long long j = 0; j < blk.len; ++j) {
            long long b_val = floor_div(blk.sum + j, blk.len);
            ans += (unsigned long long)cur_idx * (b_val - a[cur_idx]);
            cur_idx++;
        }
    }

    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
