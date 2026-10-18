# Problem Analysis: AtCoder-arc201_d — D. Match, Mod, Minimize

**Problem ID**: `AtCoder-arc201_d`  
**Contest**: `arc201`  
**Rating / Difficulty**: 2389  
**URL**: https://atcoder.jp/contests/arc201/tasks/arc201_d  
**VJudge Tag**: `[problem:AtCoder-arc201_d]`  
**Category File**: [`../categories/basics/modular_sum_split_reversal_matching.md`](../categories/basics/modular_sum_split_reversal_matching.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Binary Search`  

---

## 1. Problem Statement & Key Idea
Sort A and B. Optimal matching splits elements into a non-wrapping prefix and a wrapping suffix, each paired in anti-monotonic order. Monotonicity reduces candidates to k = k2 (found via binary search) and k = N in O(N log N) total time.

## 2. Core Observation & Invariant
When A and B are sorted ascending, any optimal permutation pairs a prefix of size k without wrapping (A[i] + B[k-1-i] < M) and a suffix of size N-k with wrapping (A[k+j] + B[N-1-j] >= M). To minimize maximum sums, both parts are paired in reverse order. Furthermore, the condition A[k+j] + B[N-1-j] >= M is monotonically non-decreasing in k, leaving only k = k2 (the minimal valid k) and k = N as candidate optimal split points.

## 3. Step-by-Step Algorithm
1. Sort A and B ascending.
2. Find the minimum index k2 in [0, N] such that A[k2+j] + B[N-1-j] >= M for all j < N-k2 via binary search in O(N log N).
3. Evaluate the maximum modulo sum for k = k2 (if k2 < N) and k = N in O(N).
4. Output the minimum of these candidate costs.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    int N;
    ll M;
    if (!(cin >> N >> M)) return;
    vector<ll> A(N), B(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    for (int i = 0; i < N; i++) cin >> B[i];
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    int low = 0, high = N, k2 = N;
    while (low <= high) {
        int mid = (low + high) / 2;
        bool ok = true;
        for (int j = 0; j < N - mid; j++) {
            if (A[mid + j] + B[N - 1 - j] < M) {
                ok = false;
                break;
            }
        }
        if (ok) {
            k2 = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    auto get_cost = [&](int k) -> ll {
        ll cur = 0;
        for (int i = 0; i < k; i++) {
            ll s = A[i] + B[k - 1 - i];
            if (s >= M) return 2e18;
            cur = max(cur, s);
        }
        for (int j = 0; j < N - k; j++) {
            ll s = A[k + j] + B[N - 1 - j];
            if (s < M) return 2e18;
            cur = max(cur, s - M);
        }
        return cur;
    };

    ll ans = 2e18;
    if (k2 < N) ans = min(ans, get_cost(k2));
    ans = min(ans, get_cost(N));
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
