#include <iostream>
#include <cmath>
#define ll long long
using namespace std;

int main(){
    int a = 1, b = 2, c = a+b, s = 2;
    while(c < 4000000){
        if (c%2 == 0){
            s += c;
        }
        a = b;
        b = c;
        c = a+b;
    }
    cout << s;
}