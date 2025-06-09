#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <climits>
#include <sstream>
#include <list>
#include <tuple>
#include <queue>




int main() {
    
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::map<int, int> frequencies;
    int n, k;
    std::cin>>n>>k;
    int val;
    for (int i = 0; i<n;i ++){
        std::cin>>val;
        frequencies[val] ++;
    }
    std::priority_queue<int> heap;
    std::map<int, int>::iterator key;
    for (key = frequencies.begin(); key != frequencies.end(); key++) {
        heap.push(key->second);
    }
    while (k != 0) {
        int cur = heap.top();
        heap.pop();
        cur -= 1;
        k -= 1;
        if (cur != 0) {
            heap.push(cur);
        }
    }
    if (heap.empty()) {
        std::cout<<0<<std::endl;
    } else {
        std::cout<<heap.top()<<std::endl;
    }

}