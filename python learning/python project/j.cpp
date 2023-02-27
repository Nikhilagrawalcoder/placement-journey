
#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define MOD 1000000007
#define SIZE 1e6+2
#define endl "\n"


void solve(){
    ll n,x; cin>>n>>x;
    ll tot=(n+1);
    if((1-n)<=x and x<=(n+1)){
        if(x<0){
            ll ms=abs(x)+1;
            ll mul=n-ms;
            while(ms--) cout<<"-";
            while(mul--) cout<<"*";
            cout<<endl;
            return;
        }
        if(x>0){
            ll pl=abs(x)-1;
            ll mul=n-pl;
            while(pl--) cout<<"+";
            while(mul--) cout<<"*";
            cout<<endl;
            return;
        }
        if(x==0){
            ll mul=(n-1);
            while(mul--) cout<<"*";
            cout<<"-"<<endl;
            return;
        }
    }
    cout<<-1<<endl;
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    ll t; cin>>t;
    while(t--){
        solve();
    }
    return 0;
}

