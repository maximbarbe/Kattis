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

typedef long long ll;



using namespace std;



int main() {
    string line;
    int n;
    while (cin >> line) {
        int res = 0;
        n = stoi(line.substr(2));

        for (int x = 1; x < n; x++) {
            if (( x * n)%(x - n) == 0) {
                res += 1;
            } 
        }
        cout << res + 1 << endl;
    }

}