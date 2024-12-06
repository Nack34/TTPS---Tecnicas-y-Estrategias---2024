#include <iostream>
#include <vector>
#include <string>
#include <sstream>

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

int main() {
    int T;
    cin >> T;
    cin.ignore(); // Ignorar el salto de línea después de T
    
    vector<int> results;

    for (int i = 0; i < T; ++i) {
        string line;
        getline(cin, line);

        stringstream ss(line);
        int N, M, K;
        ss >> N >> M >> K;

        results.push_back(gcd(N, M));
    }

    for (const auto& result : results) {
        cout << result << endl;
    }
    cout << endl;


    return 0;
}
