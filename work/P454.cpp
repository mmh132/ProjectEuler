#include <iostream>
#include <cmath>
#include <chrono>
#define ll long long
using namespace std;
using namespace std::chrono;

ll gcd (ll a, ll b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

ll f(ll x){
    ll s = 0;
    for (ll i = 3; i <= int(1.42*sqrt(x)); i++){
        for (ll k = 1; k <= i/2; k++){
            if (gcd(i, k) == 1){
                s += x/i/(i-k);
            }
        }
    }
    return s;
}

int main(){
    auto start = high_resolution_clock::now();
 
    cout << f(pow(10, 12)) << "\n";

    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>(stop - start);
 
    cout << "Time taken by function: " << duration.count()/pow(10,6) << "seconds" << endl;
}

