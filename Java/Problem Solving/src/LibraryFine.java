public class LibraryFine {
    static int libraryFine(int d1, int m1, int y1, int d2, int m2, int y2) {
        if(y2 < y1){
            return 10000;
        }
        else if(y2 > y1){
            return 0;
        }
        else{
            if(m2 < m1){
                return Math.abs(m2-m1)*500;
            }
            else if(m2 > m1){
                return 0;
            }
            else{
                if(d2 < d1){
                    return Math.abs(d2-d1)*15;
            }
                else return 0;
        }
    }
    }

    public static void main(String[] args) {
        System.out.println(libraryFine(9,6,2015,6,6,2015)); // 45
        System.out.println(libraryFine(6,6,2015,6,6,2015)); // 0
        System.out.println(libraryFine(6,6,2011,6,6,2015)); // 0
        System.out.println(libraryFine(15,7,2014,1,7,2015)); // 0
        System.out.println(libraryFine(28,2,2015,15,4,2015)); // 0
    }
}
