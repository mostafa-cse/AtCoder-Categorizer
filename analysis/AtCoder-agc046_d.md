# Problem Analysis: AtCoder-agc046_d — D. Secret Passage

**Problem ID**: `AtCoder-agc046_d`  
**Contest**: `agc046`  
**Rating / Difficulty**: 2911  
**URL**: https://atcoder.jp/contests/agc046/tasks/agc046_d  
**VJudge Tag**: `[problem:AtCoder-agc046_d]`  
**Category File**: [`../categories/dynamic_programming/prefix_extraction_multiset_insertion_suffix_dp.md`](../categories/dynamic_programming/prefix_extraction_multiset_insertion_suffix_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Substring DP`  

---

## 1. Problem Statement & Key Idea
Given a binary string S, repeatedly remove the first 2 characters, save one to a multiset pool, and optionally insert characters from the pool anywhere. Count the number of distinct reachable strings modulo 998244353.

## 2. Core Observation & Invariant
Any reachable string consists of a suffix of S, say S[i ... |S|], combined with some counts of '0's and '1's harvested into the pool from the consumed prefix. To avoid overcounting strings that can be formed in multiple ways, establish a canonical parsing: greedily match characters from the suffix S[i...] whenever possible, and only draw from the pool (c0, c1) when forced. Reachable configurations (i, c0, c1) are found via forward DP, and distinct strings are counted via backward DP.

## 3. Step-by-Step Algorithm
1. 1. Forward DP: reach[i][c0][c1] = true if suffix S[i...] can be reached with c0 zeros and c1 ones in the pool.
2. 2. Initialize reach[0][0][0] = true, and transition by popping 2 characters and keeping 1 in the pool.
3. 3. Backward DP: dp[i][c0][c1] = number of distinct valid strings formed from suffix i with pool (c0, c1).
4. 4. Transitions branch on whether the next character of the generated string is '0' or '1' (matched from S or taken from pool).
5. 5. Return dp[0][0][0] modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|^3)`
- **Space Complexity**: `O(|S|^3)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll=long long;
#define int ll

#define rng(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,b) rng(i,0,b)
#define gnr(i,a,b) for(int i=int(b)-1;i>=int(a);i--)
#define per(i,b) gnr(i,0,b)
#define pb push_back
#define eb emplace_back
#define a first
#define b second
#define bg begin()
#define ed end()
#define all(x) x.bg,x.ed
#define si(x) int(x.size())
#ifdef LOCAL
#define dmp(x) cerr<<__LINE__<<" "<<#x<<" "<<x<<endl
#else
#define dmp(x) void(0)
#endif

template<class t,class u> void chmax(t&a,u b){if(a<b)a=b;}
template<class t,class u> void chmin(t&a,u b){if(b<a)a=b;}

template<class t> using vc=vector<t>;
template<class t> using vvc=vc<vc<t>>;

using pi=pair<int,int>;
using vi=vc<int>;

template<class t,class u>
ostream& operator<<(ostream& os,const pair<t,u>& p){
	return os<<"{"<<p.a<<","<<p.b<<"}";
}

template<class t> ostream& operator<<(ostream& os,const vc<t>& v){
	os<<"{";
	for(auto e:v)os<<e<<",";
	return os<<"}";
}

#define mp make_pair
#define mt make_tuple
#define one(x) memset(x,-1,sizeof(x))
#define zero(x) memset(x,0,sizeof(x))
#ifdef LOCAL
void dmpr(ostream&os){os<<endl;}
template<class T,class... Args>
void dmpr(ostream&os,const T&t,const Args&... args){
	os<<t<<" ";
	dmpr(os,args...);
}
#define dmp2(...) dmpr(cerr,__LINE__,##__VA_ARGS__)
#else
#define dmp2(...) void(0)
#endif

using uint=unsigned;
using ull=unsigned long long;

template<class t,size_t n>
ostream& operator<<(ostream&os,const array<t,n>&a){
	return os<<vc<t>(all(a));
}

template<int i,class T>
void print_tuple(ostream&,const T&){
}

template<int i,class T,class H,class ...Args>
void print_tuple(ostream&os,const T&t){
	if(i)os<<",";
	os<<get<i>(t);
	print_tuple<i+1,T,Args...>(os,t);
}

template<class ...Args>
ostream& operator<<(ostream&os,const tuple<Args...>&t){
	os<<"{";
	print_tuple<0,tuple<Args...>,Args...>(os,t);
	return os<<"}";
}

template<class t>
void print(t x,int suc=1){
	cout<<x;
	if(suc==1)
		cout<<"\n";
	if(suc==2)
		cout<<" ";
}

ll read(){
	ll i;
	cin>>i;
	return i;
}

vi readvi(int n,int off=0){
	vi v(n);
	rep(i,n)v[i]=read()+off;
	return v;
}

template<class T>
void print(const vector<T>&v,int suc=1){
	rep(i,v.size())
		print(v[i],i==int(v.size())-1?suc:2);
}

string readString(){
	string s;
	cin>>s;
	return s;
}

template<class T>
T sq(const T& t){
	return t*t;
}

//#define CAPITAL
void yes(bool ex=true){
	#ifdef CAPITAL
	cout<<"YES"<<"\n";
	#else
	cout<<"Yes"<<"\n";
	#endif
	if(ex)exit(0);
}
void no(bool ex=true){
	#ifdef CAPITAL
	cout<<"NO"<<"\n";
	#else
	cout<<"No"<<"\n";
	#endif
	if(ex)exit(0);
}
void possible(bool ex=true){
	#ifdef CAPITAL
	cout<<"POSSIBLE"<<"\n";
	#else
	cout<<"Possible"<<"\n";
	#endif
	if(ex)exit(0);
}
void impossible(bool ex=true){
	#ifdef CAPITAL
	cout<<"IMPOSSIBLE"<<"\n";
	#else
	cout<<"Impossible"<<"\n";
	#endif
	if(ex)exit(0);
}

constexpr ll ten(int n){
	return n==0?1:ten(n-1)*10;
}

const ll infLL=LLONG_MAX/3;

#ifdef int
const int inf=infLL;
#else
const int inf=INT_MAX/2-100;
#endif

int topbit(signed t){
	return t==0?-1:31-__builtin_clz(t);
}
int topbit(ll t){
	return t==0?-1:63-__builtin_clzll(t);
}
int botbit(signed a){
	return a==0?32:__builtin_ctz(a);
}
int botbit(ll a){
	return a==0?64:__builtin_ctzll(a);
}
int popcount(signed t){
	return __builtin_popcount(t);
}
int popcount(ll t){
	return __builtin_popcountll(t);
}
bool ispow2(int i){
	return i&&(i&-i)==i;
}
ll mask(int i){
	return (ll(1)<<i)-1;
}

bool inc(int a,int b,int c){
	return a<=b&&b<=c;
}

template<class t> void mkuni(vc<t>&v){
	sort(all(v));
	v.erase(unique(all(v)),v.ed);
}

ll rand_int(ll l, ll r) { //[l, r]
	#ifdef LOCAL
	static mt19937_64 gen;
	#else
	static mt19937_64 gen(chrono::steady_clock::now().time_since_epoch().count());
	#endif
	return uniform_int_distribution<ll>(l, r)(gen);
}

template<class t>
void myshuffle(vc<t>&a){
	rep(i,si(a))swap(a[i],a[rand_int(0,i)]);
}

template<class t>
int lwb(const vc<t>&v,const t&a){
	return lower_bound(all(v),a)-v.bg;
}

using uint=unsigned;
using ull=unsigned long long;

struct modinfo{uint mod,root;};
template<modinfo const&ref>
struct modular{
	static constexpr uint const &mod=ref.mod;
	static modular root(){return modular(ref.root);}
	uint v;
	//modular(initializer_list<uint>ls):v(*ls.bg){}
	modular(ll vv=0){s(vv%mod+mod);}
	modular& s(uint vv){
		v=vv<mod?vv:vv-mod;
		return *this;
	}
	modular operator-()const{return modular()-*this;}
	modular& operator+=(const modular&rhs){return s(v+rhs.v);}
	modular&operator-=(const modular&rhs){return s(v+mod-rhs.v);}
	modular&operator*=(const modular&rhs){
		v=ull(v)*rhs.v%mod;
		return *this;
	}
	modular&operator/=(const modular&rhs){return *this*=rhs.inv();}
	modular operator+(const modular&rhs)const{return modular(*this)+=rhs;}
	modular operator-(const modular&rhs)const{return modular(*this)-=rhs;}
	modular operator*(const modular&rhs)const{return modular(*this)*=rhs;}
	modular operator/(const modular&rhs)const{return modular(*this)/=rhs;}
	modular pow(int n)const{
		modular res(1),x(*this);
		while(n){
			if(n&1)res*=x;
			x*=x;
			n>>=1;
		}
		return res;
	}
	modular inv()const{return pow(mod-2);}
	/*modular inv()const{
		int x,y;
		int g=extgcd(v,mod,x,y);
		assert(g==1);
		if(x<0)x+=mod;
		return modular(x);
	}*/
	friend modular operator+(int x,const modular&y){
		return modular(x)+y;
	}
	friend modular operator-(int x,const modular&y){
		return modular(x)-y;
	}
	friend modular operator*(int x,const modular&y){
		return modular(x)*y;
	}
	friend modular operator/(int x,const modular&y){
		return modular(x)/y;
	}
	friend ostream& operator<<(ostream&os,const modular&m){
		return os<<m.v;
	}
	friend istream& operator>>(istream&is,modular&m){
		ll x;is>>x;
		m=modular(x);
		return is;
	}
	bool operator<(const modular&r)const{return v<r.v;}
	bool operator==(const modular&r)const{return v==r.v;}
	bool operator!=(const modular&r)const{return v!=r.v;}
	explicit operator bool()const{
		return v;
	}
};

extern constexpr modinfo base{998244353,3};
//extern constexpr modinfo base{1000000007,0};
//modinfo base{1,0};
using mint=modular<base>;

const int vmax=(1<<18)+10;
mint fact[vmax],finv[vmax],invs[vmax];
void initfact(){
	fact[0]=1;
	rng(i,1,vmax){
		fact[i]=fact[i-1]*i;
	}
	finv[vmax-1]=fact[vmax-1].inv();
	for(int i=vmax-2;i>=0;i--){
		finv[i]=finv[i+1]*(i+1);
	}
	for(int i=vmax-1;i>=1;i--){
		invs[i]=finv[i]*fact[i-1];
	}
}
mint choose(int n,int k){
	return fact[n]*finv[n-k]*finv[k];
}
mint binom(int a,int b){
	return fact[a+b]*finv[a]*finv[b];
}
mint catalan(int n){
	return binom(n,n)-(n-1>=0?binom(n-1,n+1):0);
}

const int S=310;

mint dp[2][S][S];
int waf[S][S];
bool ok[3][S][S];

signed main(){
	cin.tie(0);
	ios::sync_with_stdio(0);
	cout<<fixed<<setprecision(20);
	
	initfact();
	
	string s;cin>>s;
	int n=si(s);
	
	{
		rep(i,S)rep(j,S)waf[i][j]=inf;
		waf[0][0]=0;
		int cur=0;
		ok[cur][0][0]=1;
		rep(step,n){
			int nx=(cur+1)%3;
			int my=(cur+2)%3;
			rep(i,n+1)rep(j,n+1)if(ok[cur][i][j]){
				if(i&&s[step]=='1'){
					ok[nx][i-1][j+1]=true;
				}
				if(i&&s[step]=='0'){
					ok[nx][i][j]=true;
				}
				if(j&&s[step]=='0'){
					ok[nx][i+1][j-1]=true;
				}
				if(j&&s[step]=='1'){
					ok[nx][i][j]=true;
				}
				if(step+1<n){
					rep(tar,2){
						if(s[step]-'0'==tar||s[step+1]-'0'==tar){
							ok[my][i+(tar==0)][j+(tar==1)]=true;
						}
					}
				}
			}
			
			zero(ok[cur]);
			cur=nx;
			
			rep(i,n+1)rep(j,n+1)if(ok[cur][i][j])
				chmin(waf[i][j],step+1);
		}
	}
	
	mint ans;
	
	reverse(all(s));
	
	int cur=0;
	dp[cur][0][0]=1;
	rep(head,n){
		int nx=cur^1;
		zero(dp[nx]);
		
		rep(i,head+1)rep(j,head-i+1){
			int u=s[head-i-j]-'0';
			if(u==0)dp[nx][i][j]+=dp[cur][i][j];
			else dp[nx][i+1][j]+=dp[cur][i][j];
			if(u==1)dp[nx][i][j]+=dp[cur][i][j];
			else dp[nx][i][j+1]+=dp[cur][i][j];
		}
		
		cur=nx;
		
		mint w;
		rep(i,head+2)rep(j,head-i+2){
			int rem=head+1-i-j;
			if(waf[i][j]<=n-rem)
				w+=dp[cur][i][j];
		}
		ans+=w;
	}
	
	print(ans);
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
