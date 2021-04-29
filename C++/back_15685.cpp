#pragma warning(disable:4996)
#include<iostream>
#define endl "\n"
#define MAX 100

using namespace std;

int M[MAX][MAX] = { 0, };

int dx[4] = { 0, -1, 0, 1 };
int dy[4] = { 1, 0, -1, 0 };


int main(void)
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	// 입출력 최적화

	int n = 0;
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		int x, y, d, g;
		cin >> y >> x >> d >> g;
		
		int curve[1024] = { 0, };
		int len = 1;
		curve[0] = d;

		M[x][y] = 1;
		for (int j = 0; j < g; j++)
		{
			for (int k = len - 1; k > -1; k--)
			{
				curve[len++] = (curve[k] + 1) % 4;
			}
		}
		//cout << "len = " << len << endl;
		
		for (int i = 0; i < len; i++)
		{
			x = dx[curve[i]] + x;
			y = dy[curve[i]] + y;
			//cout << "next x :" << x << " next y :" << y << endl;
			M[x][y] = 1;

			//for (int k = 0; k < 100; k++) {
			//	for (int j = 0; j < 100; j++)
			//	{
			//		if (M[k][j])
			//		{
			//			cout << "□ ";
			//		}
			//		else
			//		{
			//			cout << "■ ";
			//		}

			//	}
			//	cout << endl;
			//}
		}

		

	}
	
	int count = 0;
	for (int i = 0; i < 99; i++) {
		for (int j = 0; j < 99; j++)
		{
			if (M[i][j])
			{
				if (M[i + 1][j] && M[i][j + 1] && M[i + 1][j + 1])
				{
					count++;
				}
			}

		}
	}
	cout << count << endl;;
}