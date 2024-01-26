class Solution {
    public int uniquePaths(int m, int n) {
        int[][] tab = new int[m][n];
        for (int i = 0; i < m; i++)
            tab[i][n - 1] = 1;
        for (int i = 0; i < n; i++)
            tab[m - 1][i] = 1;
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                tab[i][j] = tab[i + 1][j] + tab[i][j + 1];
            }
        }
        return tab[0][0];
    }
}