#pragma GCC optimize("Ofast") 
#pragma GCC target("avx,avx2,fma")


#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <unordered_map>
#include <math.h>
using namespace std;




int main() {
    int n, b;
    while (true) {
        cin >> n >> b;
        if (n == -1 && b == -1) {
            break;
        }
        b -= n;
        priority_queue<tuple<double, int, int>> heap;

        int quant;
        for (int i = 0; i < n; i++) {
            cin >> quant;

            heap.push({(double)quant, 1, quant});
        }
        if (n == 1) {
            cout << ceil(quant/(double)(b+1)) << endl;
            cin.ignore();
            continue;
        }
        
        while (b != 0) {
            tuple<double, int, int> cur = heap.top();
            heap.pop();
            quant = get<2>(cur);
            int number_to_add = 0;
            int start = 1;
            int end = b;
            int mid;
            while (start <= end) {
                mid = (start + end)/2;
                int new_quant = ceil(quant/(double)(get<1>(cur)+ mid));
                if (new_quant >= get<0>(heap.top())) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
            b -= mid;

            heap.push({ceil(quant/(double)(get<1>(cur) + mid)), get<1>(cur) + mid ,quant});
        }
        cout << get<0>(heap.top())<<endl;
        cin.ignore();
    }
    
}