# Orthogonal Vector Slope Pairing with Mutually Exclusive Subset Combinatorics

**Domain**: `Combinatorics`  
**Subtopic**: `Slope Equivalence Classes`  

This workbook contains curated, high-quality competitive programming problems teaching **Orthogonal Vector Slope Pairing with Mutually Exclusive Subset Combinatorics**.

---

## Curated Problems

### `[problem:AtCoder-abc168_e]` — ∙ (Bullet)
- **Rating / Difficulty**: 1896
- **Contest**: `abc168`
- **Analysis**: [`analysis/AtCoder-abc168_e.md`](../../analysis/AtCoder-abc168_e.md)
- **Key Idea**: Two vectors (A_1, B_1) and (A_2, B_2) are orthogonal iff their slopes are negative reciprocals. Reduce each vector by dividing by gcd(|A|, |B|) and canonicalizing to the upper half-plane. Vectors partition into orthogonal pairs of classes with counts c_1 and c_2.
- **Time Complexity**: `O(N log(max_val))`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <numeric>

using namespace std;

const int MOD = 1000000007;

long long gcd(long long a, long long b) {
    return b == 0 ? abs(a) : gcd(b, a % b);
}

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int zero_count = 0;
    map<pair<long long, long long>, int> counts;

    for (int i = 0; i < n; ++i) {
        long long a, b;
        cin >> a >> b;
        if (a == 0 && b == 0) {
            zero_count++;
            continue;
        }

        long long g = gcd(a, b);
        a /= g;
        b /= g;

        if (b < 0 || (b == 0 && a < 0)) {
            a = -a;
            b = -b;
        }

        counts[{a, b}]++;
    }

    map<pair<long long, long long>, bool> visited;
    long long total_ans = 1;

    for (auto& [vec, count1] : counts) {
        if (visited[vec]) continue;

        long long a = vec.first, b = vec.second;
        // Orthogonal vector: (-b, a) canonicalized
        long long oa = -b, ob = a;
        if (ob < 0 || (ob == 0 && oa < 0)) {
            oa = -oa;
            ob = -ob;
        }

        visited[vec] = true;
        int count2 = 0;
        if (counts.count({oa, ob})) {
            count2 = counts[{oa, ob}];
            visited[{oa, ob}] = true;
        }

        long long ways1 = power(2, count1);
        long long ways2 = power(2, count2);
        long long combined = (ways1 + ways2 - 1 + MOD) % MOD;

        total_ans = (total_ans * combined) % MOD;
    }

    total_ans = (total_ans - 1 + zero_count + MOD) % MOD;
    cout << total_ans << "\n";
    return 0;
}
```
