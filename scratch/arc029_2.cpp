#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

const double PI = acos(-1.0);

bool can_fit(double A, double B, double C, double D) {
    if (A <= C && B <= D) return true;
    if (B > C || B > D) return false;

    // Binary search angle theta in [0, PI / 2] where W(theta) <= C
    // W(theta) = A * cos(theta) + B * sin(theta) is decreasing from A down to B
    double low = 0.0, high = PI / 2.0;
    for (int iter = 0; iter < 70; ++iter) {
        double mid = (low + high) / 2.0;
        double w = A * cos(mid) + B * sin(mid);
        if (w <= C) {
            high = mid;
        } else {
            low = mid;
        }
    }

    double h = A * sin(high) + B * cos(high);
    return h <= D;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double a, b;
    if (!(cin >> a >> b)) return 0;
    if (a < b) swap(a, b);

    int n;
    if (!(cin >> n)) return 0;

    while (n--) {
        double c, d;
        cin >> c >> d;
        if (can_fit(a, b, c, d) || can_fit(a, b, d, c)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
