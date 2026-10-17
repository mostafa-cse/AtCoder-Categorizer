#include <iostream>
#include <vector>

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

    int h;
    long long w;
    if (!(cin >> h >> w)) return 0;

    int num_states = (1 << h);
    Matrix T(num_states, vector<long long>(num_states, 0));

    auto dfs = [&](auto& self, int row, int in_mask, int out_mask, int orig_in) -> void {
        if (row == h) {
            T[orig_in][out_mask]++;
            return;
        }

        if (in_mask & (1 << row)) {
            // Already covered by incoming horizontal tile
            self(self, row + 1, in_mask, out_mask, orig_in);
        } else {
            // Option 1: 1x1 tile
            self(self, row + 1, in_mask, out_mask, orig_in);
            // Option 2: 1x2 horizontal tile (protrudes to next col)
            self(self, row + 1, in_mask, out_mask | (1 << row), orig_in);
            // Option 3: 2x1 vertical tile
            if (row + 1 < h && !(in_mask & (1 << (row + 1)))) {
                self(self, row + 2, in_mask, out_mask, orig_in);
            }
        }
    };

    for (int mask = 0; mask < num_states; ++mask) {
        dfs(dfs, 0, mask, 0, mask);
    }

    Matrix Tw = power(T, w);
    cout << Tw[0][0] << "\n";

    return 0;
}
