#include <iostream>

using namespace std;

int n;
int num[100];
bool dp_flag[21][100] = {0};
long long dp[21][100] = {0};

long long dfs(int x, int d){
	if (d == n-2){
		if (x == num[n-1]) return 1;
		else return 0;
	}
	
	if (dp_flag[x][d]) return dp[x][d];
	else{
		if (x+num[d+1] >= 0 && x+num[d+1] <= 20)
			dp[x][d] += dfs(x+num[d+1], d+1);
		if (x-num[d+1] >= 0 && x-num[d+1] <= 20)
			dp[x][d] += dfs(x-num[d+1], d+1);
		dp_flag[x][d] = true;
		return dp[x][d];
	}
}

int main() {
	cin >> n;
	for(int i=0; i<n; i++)
		cin >> num[i];
	
	cout << dfs(num[0], 0) << endl;
  return 0;
}
