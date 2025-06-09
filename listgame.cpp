#pragma GCC optimize("Ofast") 
#pragma GCC target("avx,avx2,fma")



#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <algorithm>
#include <math.h>
#include <string>
#include <queue>
#include <string>
#include <unordered_map>
typedef long long ll;



using namespace std;







int main() {
    unordered_map<int, int> factors;
    int n;
    cin >> n;
    while (n % 2 == 0) {
        factors[2] ++;
        n /= 2;
    }
    for (int i = 3; i < floor(sqrt(n)) + 1; i += 2) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
                factors[i] += 1;
            }
        }
        if (n < i) {
            break;
        }
    }
    if (n != 1) {
        factors[n] += 1;
    }
    int res = 0;
    for (auto &key:factors) {
        res += key.second;
    }
    cout<<res<<endl;

}