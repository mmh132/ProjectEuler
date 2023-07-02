#include <iostream>
#include <cmath>
#define ll long long
using namespace std;

ll isqrt(ll x){
    if (x == 1){
        return 1;
    }
    ll a = x >> 1;
    ll b = x;
    ll c = 0;
    ll temp = 0;
    while (a < b){
        c = (a + x/a) >> 1;
        temp = a;
        a = c;
        b = temp;
    }
    return b;
}

ll f(ll n){

}

ll h(ll n){
    ll s = 0;
    for (ll i = 1; i <= isqrt(n); i++){
        s += n/i;
    }
    s -= isqrt(n)*isqrt(n)/2;
}

ll g(ll n){

}

int main(){

}