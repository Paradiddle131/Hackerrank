import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BinarySearch {
    private static int BinSearch(int[] numbers, int target){
        int mid = Math.round(numbers.length/2);
        while (numbers[mid] > target){
            mid = numbers[Math.round(mid/2)];
            Arrays.copyOfRange(int[] numbers, )

        }

        return numbers[mid];
    }

    public static void main(String[] args) {
        int[] numbers = new int[10];
        for (int i = 0; i < 10; i++) {
            numbers[i] = i;
        }
        System.out.println(BinSearch(numbers, 2));
    }
}
