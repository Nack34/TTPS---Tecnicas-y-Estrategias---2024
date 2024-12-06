#include <iostream>
#include <string>
using namespace std;

string divide_by_two(const string& N) {
    string result;
    int remainder = 0;
    for(char digit : N) {
        int current = (digit - '0') + 10 * remainder;
        int quotient = current / 2;
        remainder = current % 2;
        result += to_string(quotient);
    }
    // Remove leading zeros
    size_t start_pos = result.find_first_not_of('0');
    if(start_pos == string::npos) {
        return "0";
    }
    return result.substr(start_pos);
}

int count_exponent_of_two(const string& N, int K) {
    int exponent = 0;
    string current_N = N;
    while(exponent < K && (current_N.back() - '0') % 2 == 0) {
        current_N = divide_by_two(current_N);
        exponent++;
    }
    return exponent;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        string N, M;
        int K;
        cin >> N >> M >> K;
        int exponent = count_exponent_of_two(N, K);
        cout << (1 << exponent) << endl;
    }
    return 0;
}