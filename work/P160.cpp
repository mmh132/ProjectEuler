#include <iostream>
#include <cmath>
#define ll long long
using namespace std;


int main(){
    ll ret = 1;
    for (ll i = 2; i <= pow(10, 12); ++i){
        ret *= i;
        while (ret % 10 == 0){
            ret = ret/10;
        }
        ret %= (ll) pow(10, 6);
    }
    cout << ret;
}