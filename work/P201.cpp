#include <iostream>
#include <cmath>
using namespace std; 

int main(){
    int inset[100];
    int maxsum = 0;
    for (int i = 1; i <= 100; i++){
        inset[i-1] = pow(i, 2);
        maxsum += pow(i, 2);
    }

    int coeffs[51][maxsum];

    for (int val : inset){
        cout << pow(val, 0.5);
        for (int setSize = 49; setSize > -1; setSize--){
            for (int idx = 0; idx < maxsum; idx++){
                coeffs[setSize+1][idx+1] += coeffs[setSize][idx];
            }
        }
    }
    
    int rv;
    for (int i = 0; i < maxsum; i++){
        if (coeffs[50][i] == 1){
            rv += i;
        }
    }
    cout << rv;
    return 0;
}