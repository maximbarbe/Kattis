#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <tuple>
#include <math.h>
using namespace std;


#define all(x) begin(x), end(x);

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double PI = acos(-1);


class UFDS {

    private:
        vi parents;
        vi size;
    public:

        UFDS(int n) {
            for (int i = 0; i < n; i++) {
                this -> parents.push_back(i);
                this -> size.push_back(1);
            }
        }

        void join(int idx1, int idx2) {
            int p1 = getParent(idx1);
            int p2 = getParent(idx2);
            if (p1 == p2) {
                return;
            } else {
                if (this -> size[p1] < this -> size[p2]) {
                    this->parents[p2] = p1;
                    this -> size[p1] += p2;
                    this -> size[p2] = p1;
                } else {
                    this->parents[p1] = p2;
                    this -> size[p2] += p1;
                    this -> size[p1] = p2;
                }
            }
        };

        int getParent(int idx1) {
            if (this -> parents[idx1] != idx1) {
                this -> parents[idx1] = getParent(this -> parents[idx1]);
                return this -> parents[idx1];
            }
            return this -> parents[idx1];
        }

        bool isSameSet(int a, int b) {
            return getParent(a) == getParent(b);
        }

};



int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n, q, a, b;
    char c;
    cin >> n >> q;
    UFDS ufds = UFDS(n);
    for (int i = 0; i < q; i++) {
        cin >> c >> a >> b;
        if (c == '?') {
            if (ufds.isSameSet(a, b)) {
                printf("yes\n");
            } else {
                printf("no\n");
            }
        } else {
            ufds.join(a, b);
        }
    }

}