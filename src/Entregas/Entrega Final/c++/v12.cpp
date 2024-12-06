#include <iostream>
#include <cmath>

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
    return gcd(N, pow(2, K));
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

