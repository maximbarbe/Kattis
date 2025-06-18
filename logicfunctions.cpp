#include "logicfunctions.h"

// Compute xor
void exclusive(bool x, bool y, bool& ans){
    if (x == y) {
        ans = false;
        return; 
    }
    ans = true;
}

// Compute implication
void implies(bool x, bool y, bool& ans){
    if (x == true) {
        ans = y;
        return;
    } 
    ans = true;
}

// Compute equivalence
void equivalence(bool x, bool y, bool& ans){
    ans = x == y;
}