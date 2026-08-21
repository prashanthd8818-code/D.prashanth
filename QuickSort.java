import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class QuickSort {

    public static void quickSort(int[] a, int l, int r) {
        if (l < r) {
            int s = partition(a, l, r);
            quickSort(a, l, s - 1);
            quickSort(a, s + 1, r);
        }
    }

    public static int partition(int[] a, int l, int r) {
        int p = a[l];
        int i = l;
        int j = r + 1;

        while (true) {

            do {
                i++;
            } while (i <= r && a[i] < p);

            do {
                j--;
            } while (j >= l && a[j] > p);

            if (i >= j)
                break;

            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }

        int temp = a[l];
        a[l] = a[j];
        a[j] = temp;

        return j;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        System.out.println("Enter the array size");
        int n = sc.nextInt();

        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            // a[i] = sc.nextInt();
            a[i] = rand.nextInt(100) + 1; 
        }

        System.out.println("Generated Array:");
        System.out.println(Arrays.toString(a));

        long start = System.nanoTime();
        quickSort(a, 0, a.length - 1);
        long end = System.nanoTime();

        System.out.println("Sorted Array:");
        System.out.println(Arrays.toString(a));

        System.out.println("Time taken = " + (end - start) + " ns");

        sc.close();
    }
}