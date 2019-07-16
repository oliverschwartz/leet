/* BubbleSort.java                            */
/* Author: Oliver Schwartz                    */
/**********************************************/
/* This algorithm is a basic sorting algorithm which 'bubbles' elements
   to one end of the array. In the worst case, this algorithm runs in 
   n^2 time (i.e. if the elements are in reverse order). It's performance
   is O(n^2) - quadratic - time. */

class BubbleSort {

	// Bubble-sort the array in-place.
	private static void sort(int[] a) {
		boolean sorted = false;
		int end = a.length - 1;

		while (!sorted) {
			sorted = true;
			for (int i = 0; i < end; i++) {
				if (a[i] > a[i+1]) {
					sorted = false;
					swap(a, i, i+1);
				}
			}
			end--;
		}
	}

	// Swap two elements in place.
	private static void swap(int[] a, int i, int j) {
		assert i >= 0 && i < a.length;
		assert j >= 0 && j < a.length;

		int tmp = a[i];
		a[i] = a[j];
		a[j] = tmp;
	}

	// Unit testing
	public static void main(String[] args) {
		int[] a = new int[]{-1, 5, 5, 3, 2, 1, 8, 10, 9, -2, 20, 11, 19, 1000, -999, 0};
		
		System.out.println("unsorted array:");
		for (int i = 0; i < a.length; i++)
			System.out.print(a[i] + " ");
		System.out.println("\n");

		System.out.println("sorted array:");
		sort(a);
		for (int i = 0; i < a.length; i++)
			System.out.print(a[i] + " ");
		System.out.println();
	}
}
