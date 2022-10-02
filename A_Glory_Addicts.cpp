/**===========================================================================================
                                B H Yean Hasan (NoYoN)
                    Patuakhali Science and Technology University
                     Faculty of Computer Science and Engineering
                            https://bhyeanhasan.github.io
/*===========================================================================================**/
#include<bits/stdc++.h>
#define pi acos(-1)
#define even(i) (!(i & 1))
#define odd(i) (i & 1)
#define gcd(a, b) __gcd(a,b)
#define lcm(a, b) (((a)/gcd(a,b))*b)
#define fil(arr, value) memset(arr,value,arr.size())
#define vfill(v, value)  v.assign(v.size(),value)
#define ll long long int
#define LN __int128
#define Max LONG_LONG_MAX
#define Min LONG_LONG_MIN
#define pb(x) push_back(x)
#define in(a) scanf("%lld",&a)
#define point(x, d) cout<<fixed<<setprecision(d)<<x
#define print(x) cout<<x<<endl
#define srt(a) sort(a.begin(),a.end())
#define fr(i, n) for(ll i=0;i<n;i++)
#define yes cout<<"YES"<<endl
#define no cout<<"NO"<<endl
#define ln cout<<endl
#define tc ll test = input(); for(ll T=1;T<=test;T++)
#define NoYoN_Variables ll n,m,a,b,c,x,y,z,i,j,k,sum=0,t=0,count=0,flag=0; string s1,s2,s3; bool is = false; double Sum=0;
#define By_NoYoN ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(0);

using namespace std;
ll input() {
    ll x;
    cin >> x;
    return x;
}
// void show(ll ar[], ll first, ll last) {for (ll i = first; i < last; i++) {cout << ar[i] << " ";}cout << endl;}
// void show(vector<ll> ar, ll first, ll last) {for (ll i = first; i < last; i++) {cout << ar[i] << " ";} cout << endl;}

int main() {
    By_NoYoN;
    NoYoN_Variables;
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    tc
    {
        /*===========================================================================================*/


            cin>>n;
            sum=0;

            ll arr[n],brr[n];

            for(int i=0;i<n;i++)
            {
                cin>>x;
                arr[i]=x;
            }
            for(int i=0;i<n;i++)
            {
                cin>>x;
                brr[i]=x;
                sum+=x;
            }

            vector<int> f,z;

            for(int i=0;i<n;i++)
            {
                if(arr[i]==0)
                {
                    f.push_back(brr[i]);
                    
                }
                else{
                    z.push_back(brr[i]);
                }
            }

            sort(f.begin(), f.end(), greater<int>());
            sort(z.begin(), z.end(), greater<int>());


            a = min(f.size(),z.size());

           for(i=0;i<a;i++)
           {
                sum+=f[i]+z[i];
           }

            if(f.size()==z.size())
            {
                
 
                if(z[z.size()-1]>f[f.size()-1])
                {
                    sum-=f[f.size()-1];
                }
                else
                {
                    sum-=z[z.size()-1];
                }
            }

            cout<<sum<<endl;




        /*===========================================================================================*/
    }

}