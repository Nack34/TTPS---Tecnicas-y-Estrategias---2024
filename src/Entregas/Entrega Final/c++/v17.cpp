#include <iostream>
#include <string>
using namespace std;

string divide_by_two(string N) {
    string res;
    int carry = 0;
    for (char c : N) {
        int num = carry * 10 + (c - '0');
        res += num / 2 + '0';
        carry = num % 2;
    }
    return res[0] == '0' ? res.substr(1) : res;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string N, M;
        int K, exp = 0;
        cin >> N >> M >> K;
        while (exp < K && (N.back() - '0') % 2 == 0) {
            N = divide_by_two(N);
            exp++;
        }
        cout << (1 << exp) << endl;
    }
    return 0;
}
