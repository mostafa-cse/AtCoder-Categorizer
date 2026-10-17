# Formal Grammar String Rewriting Casework and Fibonacci Transition Invariants

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Grammar Rewriting / Matrix DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Formal Grammar String Rewriting Casework and Fibonacci Transition Invariants**.

---

## Curated Problems

### `[problem:AtCoder-arc108_d]` — AB
- **Rating / Difficulty**: 1987
- **Contest**: `arc108`
- **Analysis**: [`analysis/AtCoder-arc108_d.md`](../../analysis/AtCoder-arc108_d.md)
- **Key Idea**: If N <= 3, the answer is 1. For N >= 4, the first step produces 'AcB' where c = rule('AB'). If c == 'A': the next insertions can only place rule('AA') between 'A' and 'A', or rule('AB') between 'A' and 'B'. Symmetrically analyze the cases: depending on rule('AA') and rule('BA'), the number of obtainable strings either remains 1, reaches 2^{N-3}, or follows the Fibonacci recurrence F_{N-1} (when consecutive blocks of 'B' are restricted to size 1).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

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

    char c_aa, c_ab, c_ba, c_bb;
    cin >> c_aa >> c_ab >> c_ba >> c_bb;

    if (n <= 3) {
        cout << 1 << "\n";
        return 0;
    }

    vector<long long> fib(n + 1, 0);
    fib[1] = 1;
    fib[2] = 1;
    for (int i = 3; i <= n; ++i) {
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;
    }

    if (c_ab == 'A') {
        if (c_aa == 'A') {
            cout << 1 << "\n";
        } else {
            if (c_ba == 'A') {
                cout << fib[n - 1] << "\n";
            } else {
                cout << power(2, n - 3) << "\n";
            }
        }
    } else {
        if (c_bb == 'B') {
            cout << 1 << "\n";
        } else {
            if (c_ba == 'B') {
                cout << fib[n - 1] << "\n";
            } else {
                cout << power(2, n - 3) << "\n";
            }
        }
    }

    return 0;
}
```
