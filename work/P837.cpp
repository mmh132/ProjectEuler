#include <iostream>
#define ll long long
using namespace std;

ll modexp(ll b, ll e, ll mod){
    ll rv = 1;
    while (e){
        if (e&1){
            rv*=b;
            rv%=mod;
        }
        b*=b;
        b%=mod;
        e>>=1;
    }
    return rv;
}

ll inv(ll a, ll mod) {
    return a <= 1 ? a : mod - (mod/a) * inv(mod % a, mod) % mod;
}

int main() {
    ll MOD = 1234567891;
    ll N = 123456789;
    ll M = 987654321;


}