# Matrix Exponentiation

**Domain**: `Math`  
**Subtopic**: `Matrices`  

This workbook contains curated, high-quality competitive programming problems teaching **Matrix Exponentiation**.

---

## Curated Problems

### `[problem:AtCoder-arc020_3]` — A mod B Problem
- **Rating / Difficulty**: 2141
- **Contest**: `arc020`
- **Analysis**: [`analysis/AtCoder-arc020_3.md`](../../analysis/AtCoder-arc020_3.md)
- **Key Idea**: Repeating an integer A with d digits L times transforms a current value x via x' = x * 10^{dL} + A * (10^{dL} - 1) / (10^d - 1). Because B may not be coprime to 10^d - 1, modular division is invalid. Instead, we express the affine state transition [x, 1]^T -> [x * 10^d + A, 1]^T as multiplication by a 2x2 matrix M = [[10^d, A], [0, 1]]. Repeating L times is computing M^L via standard 2x2 matrix exponentiation modulo B.
- **Time Complexity**: `O(N * log L)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

long long B;

struct Matrix {
    long long mat[2][2];
    Matrix() {
        mat[0][0] = mat[0][1] = mat[1][0] = mat[1][1] = 0;
    }
};

Matrix multiply(const Matrix& a, const Matrix& b) {
    Matrix c;
    for (int i = 0; i < 2; ++i) {
        for (int k = 0; k < 2; ++k) {
            for (int j = 0; j < 2; ++j) {
                c.mat[i][j] = (c.mat[i][j] + (__int128)a.mat[i][k] * b.mat[k][j]) % B;
            }
        }
    }
    return c;
}

Matrix power(Matrix a, long long exp) {
    Matrix res;
    res.mat[0][0] = res.mat[1][1] = 1;
    while (exp > 0) {
        if (exp & 1) res = multiply(res, a);
        a = multiply(a, a);
        exp >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n), l(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> l[i];
    }
    cin >> B;

    long long cur_x = 0;

    for (int i = 0; i < n; ++i) {
        long long temp = a[i];
        long long p10 = 1;
        while (temp > 0) {
            p10 = (p10 * 10) % B;
            temp /= 10;
        }

        Matrix m;
        m.mat[0][0] = p10;
        m.mat[0][1] = a[i] % B;
        m.mat[1][0] = 0;
        m.mat[1][1] = 1;

        Matrix m_pow = power(m, l[i]);
        cur_x = ((__int128)m_pow.mat[0][0] * cur_x + m_pow.mat[0][1]) % B;
    }

    cout << cur_x << "\n";
    return 0;
}
```
