#include <iostream>
#include <cmath>

using namespace std;

int solve_case(int N, int M, int K) {
    int cant = 0;
    while (K-- && N%2 == 0){
        N/=2;
        cant++;
    }

    return pow(2, cant);
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

