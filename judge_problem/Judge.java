class Solution {

    // Approach: the judge must be trusted by N - 1
    // people. Therefore, we store how many times 
    // a given person is trusted or trusts, and then
    // use this to determine if the judge can be found.
    public int findJudge(int N, int[][] trust) {
        if (trust.length < N - 1) return -1;
        
        // arrays representing the frequency with which person i
        // trusts someone or is trusted by others
        int[] receives = new int[N];
        int[] gives = new int[N];
        
        for (int i = 0; i < trust.length; i++) {
            gives[trust[i][0] - 1]++;
            receives[trust[i][1] - 1]++;
        }
        
        for (int i = 0; i < receives.length; i++) {
            if (receives[i] >= N - 1 && gives[i] == 0) return i + 1;
        }
        
        return -1;
    }
}