# Prime Factor Bitmask DP over Bounded Interval Differences

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Bit Related DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Prime Factor Bitmask DP over Bounded Interval Differences**.

---

## Curated Problems

### `[problem:AtCoder-abc195_f]` — Coprime Present
- **Rating / Difficulty**: 2068
- **Contest**: `abc195`
- **Analysis**: [`analysis/AtCoder-abc195_f.md`](../../analysis/AtCoder-abc195_f.md)
- **Key Idea**: Two numbers x, y in [A, B] can share a common prime factor p only if p <= |x - y| <= B - A <= 72. There are exactly 20 primes <= 72. Any prime factor > 72 can divide at most one number in [A, B]. Therefore, a subset is pairwise coprime if and only if their masks of prime factors <= 72 are pairwise disjoint. With 20 primes (2^20 ~ 10^6 states) and at most 73 numbers, we use standard bitmask DP: for each number x, iterate over submasks disjoint from mask(x) and transition.
- **Time Complexity**: `O((B - A) * 2^20)`
- **Space Complexity**: `O(2^20)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71};
const int NUM_PRIMES = 20;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long A, B;
    if (!(cin >> A >> B)) return 0;

    int total_masks = 1 << NUM_PRIMES;
    vector<long long> dp(total_masks, 0);
    dp[0] = 1;

    for (long long x = A; x <= B; ++x) {
        int m = 0;
        for (int i = 0; i < NUM_PRIMES; ++i) {
            if (x % primes[i] == 0) {
                m |= (1 << i);
            }
        }

        int sub = (total_masks - 1) ^ m;
        for (int mask = sub; ; mask = (mask - 1) & sub) {
            dp[mask | m] += dp[mask];
            if (mask == 0) break;
        }
    }

    long long ans = 0;
    for (int mask = 0; mask < total_masks; ++mask) {
        ans += dp[mask];
    }

    cout << ans << "\n";
    return 0;
}
```
