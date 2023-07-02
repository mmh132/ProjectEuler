#include <iostream>
#include <cmath>
#define ll long long
using namespace std;

ll lpf(ll n){
    ll i = 2;
    while(i < n){
        while(n%i == 0){
            n = n/i;
        }
        ++i;
    }
    if(n == 1){
        return i;
    }else{
        return n;
    }
}
int main(){
    cout << lpf(600851475143);
}