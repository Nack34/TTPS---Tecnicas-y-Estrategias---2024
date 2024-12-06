#include <iostream>
#include <cmath>
#include <numeric>
#include <cstdio>

using namespace std;

// Función para calcular el máximo común divisor (GCD)
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
    for (int x = 1; x <= N/2; ++x) {  // Recorremos solo hasta N/2
        int a = x, b = N - x;
        if (gcd(a, b) == 1 && a * a + b * b - factor * a * b == M)
            return gcd(N, M);
    }
    return 1;
}

int main() {
    ios::sync_with_stdio(false);  // Desactiva la sincronización de C++ con C
    cin.tie(nullptr);  // Desvincula la cin y la cout para mejorar el rendimiento

    int T, N, M, K;
    cin >> T;
    while (T--) {
        cin >> N >> M >> K;
        cout << solve_case(N, M, K) << "\n";  // Escribe en una sola llamada
    }

    return 0;
}