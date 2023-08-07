#include <iostream>
#include <cmath>
using namespace std;

#define ll long long
// this solution is 16 off for whatever reason, python one works and is basically the same
ll eval(ll n){
    if (n < 243){
        if (n < 54){
            if (n < 24){
                if (n < 6){
                    return 0;
                }
                return 1;
            }
            return 2;
        }
        return 3;
    }
    ll ret = 0;
    int k = 1;
    while (3*pow(2, k) <= n){
        k += 3;
        ret++;
    }
    k = 2;
    while (pow(3, k) <= n){
        k += 3;
        ret++;
    }
    return ret;
}

ll cr(ll n){
    return n - n/2 - n/3 + n/6;
}

ll solve(ll n){
    ll out;
    for (ll i = 1; i <= (ll) sqrt(n); i++){
        if (i % 6 == 1 || i % 6 == 5){
            out += eval(n/i);
        }
    }
    for (ll z = 1; z <= (ll) sqrt(n); z++){
        if (n/z == z){
            continue;
        }
        out += (cr(n/z) - cr(n/(z+1)))*eval(z);
    }
    return n-out;
}

int main(){
    cout << solve(pow(10,16));
}