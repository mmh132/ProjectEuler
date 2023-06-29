#include <iostream>
#include <cmath>
using namespace std; 

int coeffs[295426][51];

int main(){
    int inset[100];
    int maxsum = 0;
    for (int i = 1; i <= 100; i++){
        inset[i-1] = pow(i, 2);
        maxsum += pow(i, 2);
    }

    for (int val : inset){
        cout << pow(val, 0.5);
        for (int setSize = 49; setSize > -1; setSize--){
            for (int idx = 0; idx < maxsum; idx++){
                coeffs[idx+1][setSize+1] += coeffs[idx][setSize];
            }
        }
    }
    
    int rv;
    for (int i = 0; i < maxsum; i++){
        if (coeffs[i][50] == 1){
            rv += i;
        }
    }
    cout << rv;
    return 0;
}