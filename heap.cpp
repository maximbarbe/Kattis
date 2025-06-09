#include "heap.h"
#include "vector"
#include "queue"
#include <climits>
std::priority_queue<int> heap ;

int getMax(){
    return heap.top();
}

int getSize(){
    return heap.size();
}

void insert(int element){
    heap.push(element);
}

void removeMax(){
    heap.pop();
}