#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>

using namespace std;




typedef long long ll;

int main() {
    ll n;
    cin >> n;
    if (n == 1) {
        cout << 1<<endl;
        return 0;
    }
    vector<ll> increasingFactors = {1};
    vector<ll> decreasingFactors = {n};
    
    for (ll i = 2; i < floor(sqrt(n)) + 1;i++) {
        if (n % i == 0) {
            if (i * i == n) {
                increasingFactors.push_back(i);
            } else {
                increasingFactors.push_back(i);
                decreasingFactors.push_back(n/i);
            }
        }
    }
    for (int i = 0; i < increasingFactors.size(); i++) {
        cout << increasingFactors[i] << endl;
    }
    for (int i = decreasingFactors.size() - 1; i >= 0; i--) {
        cout << decreasingFactors[i] << endl;
    }
    return 0;
}