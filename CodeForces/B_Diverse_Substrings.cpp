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
#define inputarr(arr) for(auto& it:arr) {cin >> it;}
#define show(arr) for(auto& it:arr) {cout << it << ' ';}
#define yes cout<<"YES"<<endl
#define no cout<<"NO"<<endl
#define ln cout<<endl
#define tc ll test = input(); for(ll T=1;T<=test;T++)
#define NoYoN_Variables ll n,m,a,b,c,x,y,z,i,j,k,sum=0,t=0,count=0,flag=0; string s,s1,s2,s3; bool is = false; double Sum=0;
#define By_NoYoN ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(0);


using namespace std;
ll input() {
    ll x;
    cin >> x;
    return x;
}

int main() {
    By_NoYoN;
    NoYoN_Variables;
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    tc
    {
        /*===========================================================================================*/

        cin>>n>>s;

        sum=0;
        for(ll i=0;i<n;i++)
        {
            ll arr[10]={0}, dis=0,maxf=0;

            for(j=i;j<=i+99 && j<n;j++)
            {
                arr[s[j]-'0']++;
                if(arr[s[j]-'0']==1)
                    dis++;
                maxf = max(maxf,arr[s[j]-'0']);
                if(maxf<=dis)
                sum++;
            }
        }
        cout<<sum<<endl;
        
        /*===========================================================================================*/
    }

}



