# Automaton Transition Matrix Exponentiation for Banned Substring Avoidance O(V^3 log N)

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Matrix Exponentiation / Automata`  

This workbook contains curated, high-quality competitive programming problems teaching **Automaton Transition Matrix Exponentiation for Banned Substring Avoidance O(V^3 log N)**.

---

## Curated Problems

### `[problem:AtCoder-abc305_g]` — Banned Substrings
- **Rating / Difficulty**: 1989
- **Contest**: `abc305`
- **Analysis**: [`analysis/AtCoder-abc305_g.md`](../../analysis/AtCoder-abc305_g.md)
- **Key Idea**: Since |S_i| <= 6, whether appending a character creates a banned substring depends only on the suffix of length at most 5. Represent the DFA state by the longest valid suffix of length <= 5 (at most 2^5 = 32 states for length 5). Build the transition matrix T where T[u][v] = 1 if appending 'a' or 'b' to state u transitions to valid state v. Compute T^N via binary matrix exponentiation in O(V^3 log N) with V <= 64.
- **Time Complexity**: `O(V^3 log N) where V <= 64`
- **Space Complexity**: `O(V^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

const int MOD = 998244353;

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix& A, const Matrix& B) {
    int n = A.size();
    Matrix C(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < n; ++j) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix power(Matrix A, long long exp) {
    int n = A.size();
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    while (exp > 0) {
        if (exp % 2 == 1) res = multiply(res, A);
        A = multiply(A, A);
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int m;
    if (!(cin >> n >> m)) return 0;

    vector<string> banned(m);
    for (int i = 0; i < m; ++i) {
        cin >> banned[i];
    }

    auto is_valid = [&](const string& s) {
        for (const auto& b : banned) {
            if (s.find(b) != string::npos) return false;
        }
        return true;
    };

    if (n <= 5) {
        int count = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
            string s = "";
            for (int i = 0; i < n; ++i) {
                s += ((mask >> i) & 1) ? 'b' : 'a';
            }
            if (is_valid(s)) count++;
        }
        cout << count << "\n";
        return 0;
    }

    vector<string> states;
    for (int mask = 0; mask < 32; ++mask) {
        string s = "";
        for (int i = 0; i < 5; ++i) {
            s += ((mask >> i) & 1) ? 'b' : 'a';
        }
        if (is_valid(s)) {
            states.push_back(s);
        }
    }

    int V = states.size();
    Matrix T(V, vector<long long>(V, 0));

    for (int i = 0; i < V; ++i) {
        for (char c : {'a', 'b'}) {
            string cand = states[i] + c;
            if (is_valid(cand)) {
                string next_state = cand.substr(1);
                for (int j = 0; j < V; ++j) {
                    if (states[j] == next_state) {
                        T[i][j]++;
                        break;
                    }
                }
            }
        }
    }

    Matrix Tn = power(T, n - 5);

    long long total_ans = 0;
    for (int i = 0; i < V; ++i) {
        for (int j = 0; j < V; ++j) {
            total_ans = (total_ans + Tn[i][j]) % MOD;
        }
    }

    cout << total_ans << "\n";
    return 0;
}
```
