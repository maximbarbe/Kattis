#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>


int main() {
    
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n;
    std::cin>>n;
    std::string res = "";
    std::string input;
    for (int i = 0; i < n; i++) {
        std::cin>>input;
        res.append(input);
    }
    std::reverse(res.begin(), res.end());
    std::cout<<res<<"\n";
}