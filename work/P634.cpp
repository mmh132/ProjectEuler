#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define len sizeof

ll isqrt(ll n){
    if (n == 1){
        return n;
    }
    ll a = n >> 1;
    ll b = n;
    ll c;
    while (a < b){
        c = (a + n/a) >> 1;
        a,b = c,a;
    }   
    return b;
}

ll solve(ll n){
    ll rv = 0;
    bool sq[(int) pow(n, 0.3333334)];
    for (ll i = 2; i < len(sq); i++){
        for (ll k = i*i; k < len(sq); k++){
            sq[k] = false;
        }
    }
    for (int b = 2; b < len(sq); b++){
        if (sq[b] = 0){
            continue;
        }
        rv += (int) sqrt(n/b/b/b) - 1;
    }
    return rv;
}

int main(){
    cout << solve(2*pow(10, 4));
}