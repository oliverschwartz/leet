import java.util.ArrayList;

class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int N = gas.length;
        
        int[] visitCost = new int[N];
        ArrayList<Integer> starts = new ArrayList<Integer>();
        
        for (int i = 0; i < N; i++) {
            visitCost[i] = gas[i] - cost[i];
            if (visitCost[i] >= 0) {
                starts.add(i);
            }
        }
        
        for (int s : starts) {
            if (validPath(s, visitCost)) {
                return s;
            }
        }
            
        // should only reach this line if there is no solution
        return -1;   
    }
    
    private boolean validPath(int start, int[] visitCost) {
        int sum = 0;
        int index = start;
        for (int i = 0; i < visitCost.length; i++) {
            sum += visitCost[index];
            if (sum < 0) return false;
            if (index == visitCost.length - 1) index = 0;
            else index++;
        }
        return true;
    }
}