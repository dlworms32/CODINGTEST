#pragma warning(disable:4996)
#include<iostream>
#define endl "\n"
#define MAX 1024

using namespace std;

int dp[MAX + 1][MAX + 1] = { 0, };


int main(void)
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	// I / O optimization
	
	int N, M;
	int x1 = 0, y1 = 0, x2 = 0, y2 = 0;
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int num = 0;
			cin >> num;
			dp[i + 1][j + 1] = dp[i][j + 1] + num + dp[i + 1][j] - dp[i][j];
		}
	}

	for (int i = 0; i < M; i++)
	{
		cin >> x1 >> y1 >> x2 >> y2;
		cout << dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1] << endl;
	}
}