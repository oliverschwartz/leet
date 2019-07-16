class MergeInterval {

    /* Merge intervals from left to right */
    public static int[][] merge(int[][] intervals) {
        if (intervals.length == 0) return null;
        
        for (int i = 0; i < intervals.length - 1; i++) {
            if (intervals[i] == null) continue;
            for (int j = i + 1; j < intervals.length; j++) {
                if (intervals[j] == null) continue;

                int i0 = intervals[i][0];
                int i1 = intervals[i][1];
                int j0 = intervals[j][0];
                int j1 = intervals[j][1];
                
                if (i0 == j0) {
                    if (i1 > j1)
                        intervals[j] = null;
                    else
                        intervals[i] = null;
                }
                else if (j0 > i0) {
                    if (i1 >= j0 && j1 >= i1) {
                        intervals[i][1] = j1;
                        intervals[j] = null;
                    }
                    else if (i1 > j1)
                        intervals[j] = null;
                }
                else { // x0 > y0
                    if (j1 >= i0 && i1 >= j1) {
                        intervals[j][1] = i1;
                        intervals[i] = null;
                    }
                    else if (j1 > i1)
                        intervals[i] = null;
                    }
                }
            }            
        return intervals;
    }

    public static void main(String[] args) {
        int[][] intervals = new int[2][2];
        intervals[0][0] = 0;
        intervals[0][1] = 2;
        intervals[1][0] = 1;
        intervals[1][1] = 2;

        intervals[1] = null;

        System.out.println(intervals.length);

        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i] == null) continue;
            for (int j = 0; j < 2; j++)
                System.out.print(intervals[i][j] + " ");
            System.out.println();        
        }
    }
}