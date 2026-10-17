#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    int total = n + m;
    vector<int> p(total + 1);
    for (int i = 1; i <= total; ++i) {
        cin >> p[i];
    }

    vector<bool> visited(total + 1, false);
    int c_white = 0, c_black = 0;
    int base_swaps = 0;

    for (int i = 1; i <= total; ++i) {
        if (!visited[i]) {
            int cur = i;
            int len = 0;
            int white_cnt = 0, black_cnt = 0;

            while (!visited[cur]) {
                visited[cur] = true;
                len++;
                if (cur <= n) white_cnt++;
                else black_cnt++;
                cur = p[cur];
            }

            if (len > 1) {
                base_swaps += (len - 1);
                if (white_cnt > 0 && black_cnt == 0) c_white++;
                else if (black_cnt > 0 && white_cnt == 0) c_black++;
            }
        }
    }

    int ans = base_swaps + 2 * max(c_white, c_black);
    cout << ans << "\n";

    return 0;
}
