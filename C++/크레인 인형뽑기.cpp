#include <iostream>
#include <string>
#include <vector>
#include <stack>

#define endl '\n'

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    stack<int> st;
    int cnt = 0;
    int moves_idx = 0;
    while (moves_idx < moves.size())
    {
        for (int i = 0; i < board.size(); i++) // 정사각형
        {
            int pick_item = board[i][moves[moves_idx] - 1];
            if (pick_item)
            {
                if (st.size() && st.top() == pick_item) {
                    cnt += 2;
                    st.pop();
                }
                else
                {
                    st.push(board[i][moves[moves_idx] - 1]);
                }
                board[i][moves[moves_idx] - 1] = 0;
                break;
            }
        }
        moves_idx++;
    }
    return cnt;
}

int main()
{
    //cin.tie(NULL);
    //cout.tie(NULL);
    //ios_base::sync_with_stdio(false);
    freopen_s(new FILE*, "input.txt", "r", stdin);

    int n = 0;
    cin >> n;
    vector<vector<int>> board(n, vector<int>(n));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> board[i][j];
        }
    }
    int m = 0;
    cin >> m;
    vector<int> moves(m);
    for (int i = 0; i < m; i++)
        cin >> moves[i];

    cout << solution(board, moves);
    return 0;
}