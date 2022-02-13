package datatypeconversion;

public class ExplicitDataTypeConversion {
    public static void main(String[] args) {
        double a = 50.5d;
        System.out.println("Double representation: " + a);

        float b = (float) a;
        System.out.println("Float representation: " + b);

        long c = (long) b;
        System.out.println("Long representation: " + c);

        int d = (int) c;
        System.out.println("Integer representation: " + d);
    }
}
