# Markov Chain Expected Value Transition via Matrix Exponentiation

**Domain**: `Math`  
**Subtopic**: `Linear Algebra`  

This workbook contains curated, high-quality competitive programming problems teaching **Markov Chain Expected Value Transition via Matrix Exponentiation**.

---

## Curated Problems

### `[problem:AtCoder-abc199_f]` — Graph Smoothing
- **Rating / Difficulty**: 2065
- **Contest**: `abc199`
- **Analysis**: [`analysis/AtCoder-abc199_f.md`](../../analysis/AtCoder-abc199_f.md)
- **Key Idea**: Because the averaging operation is linear, expectations transition linearly: E[A'^{(t+1)}] = T * E[A'^{(t)}]. For vertex u, an incident edge (u, v) is chosen with probability 1/M, setting u's value to (A_u + A_v)/2. Non-incident edges leave A_u unchanged. Thus T_{u, u} = 1 - deg(u)/(2M) and T_{u, v} = 1/(2M) for (u, v) in E. The state after K steps is E[A^{(K)}] = T^K * A^{(0)}, computable via binary matrix exponentiation in O(N^3 log K).
- **Time Complexity**: `O(N^3 log K)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

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

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix& A, const Matrix& B, int n) {
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

Matrix matPower(Matrix A, long long p, int n) {
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    while (p > 0) {
        if (p & 1) res = multiply(res, A, n);
        A = multiply(A, A, n);
        p >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<vector<int>> adj(n);
    vector<int> deg(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    long long inv2m = modInverse(2LL * m % MOD);

    Matrix T(n, vector<long long>(n, 0));
    for (int u = 0; u < n; ++u) {
        long long diag = (1 - (1LL * deg[u] % MOD * inv2m % MOD) + MOD) % MOD;
        T[u][u] = diag;
        for (int v : adj[u]) {
            T[u][v] = inv2m;
        }
    }

    Matrix Tk = matPower(T, k, n);

    for (int i = 0; i < n; ++i) {
        long long ans = 0;
        for (int j = 0; j < n; ++j) {
            ans = (ans + Tk[i][j] * a[j]) % MOD;
        }
        cout << ans << "\n";
    }
    return 0;
}
```
