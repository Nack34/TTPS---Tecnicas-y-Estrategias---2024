#include <iostream>
#include <vector>
#include <cmath>
#include <numeric> // Para std::gcd
#include <sstream>

using namespace std;

// Función para resolver un caso
int solve_case(int N, int M, int K) {
    int factor = (pow(2, K) - 2);
    for (int x = 1; x < N; ++x) {
        int a = x;
        int b = N - x;
        if (gcd(a, b) == 1) {
            int calculated_M = a * a + b * b - factor * a * b;
            if (calculated_M == M) {
                return gcd(N, M);
            }
        }
    }
    return 1;  // Valor predeterminado si no se encuentra un par válido (casos límite)
}

int main() {
    int T;
    cin >> T;
    cin.ignore(); // Ignorar salto de línea después de T

    vector<int> results;

    for (int i = 0; i < T; ++i) {
        string line;
        getline(cin, line);

        stringstream ss(line);
        int N, M, K;
        ss >> N >> M >> K;

        results.push_back(solve_case(N, M, K));
    }

    // Imprimir todos los resultados
    for (const auto& result : results) {
        cout << result << endl;
    }

    return 0;
}
