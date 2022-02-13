package datatypes;

public class NonPrimitiveDataTypes {
    public static void main(String[] args) {
        String str = "test";
        System.out.println("String is " + str);

        String str1 = new String("test 2");
        System.out.println("Another string is " + str1);

        int arr[];
        arr = new int[2];
        arr[0] = 2;
        arr[1] = 3;
        System.out.println("Array is " + arr);
        System.out.println("Element in Array is " + arr[1]);
    }
}