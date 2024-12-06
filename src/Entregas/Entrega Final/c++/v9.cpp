#include <iostream>
#include <cmath>
#include <unordered_map>

using namespace std;

int gcd(int u, int v) {
    while (v) {
        int t = u;
        u = v;
        v = t % v;
    }
    return (u < 0) ? -u : u;
}

int solve_case(int N, int M, int K) {
    int factor = (pow(2, K) - 2);
    for (int x = 1; x <= N / 2; ++x) {
        int a = x, b = N - x;
        if (a * a + b * b - factor * a * b == M)
            return gcd(a+b, pow(2, K) * a * b);
    }
    return 1;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int T, N, M, K;
    cin >> T;
    while (T--) {
        cin >> N >> M >> K;
        cout << solve_case(N, M, K) << "\n";
    }
}
