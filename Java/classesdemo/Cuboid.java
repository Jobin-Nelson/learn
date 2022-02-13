package classesdemo;

public class Cuboid {
    int width;
    int heigth;
    int depth;

    public Cuboid(int width, int heigth, int depth) {
        this.width = width;
        this.heigth = heigth;
        this.depth = depth;
    }

    public Cuboid() {
        this.width = 10;
        this.heigth = 10;
        this.depth = 10;
    }

    public Cuboid(int dim) {
        this.width = dim;
        this.heigth = dim;
        this.depth = dim;
    }

    public Cuboid(int width, int heigth) {
        this.width = width;
        this.heigth = heigth;
        this.depth = 10;
    }

    public int Volume() {
        return width * heigth * depth;
    }

    public static void main(String arg[]) {
        Cuboid stdCuboid = new Cuboid(10, 10, 15);
        int volume = stdCuboid.Volume();
        System.out.println("Volume of the simple cuboid is " + volume);

        Cuboid cuboidWithDefaults = new Cuboid(10, 20);
        volume = cuboidWithDefaults.Volume();
        System.out.println("Volume of the default cuboid is " + volume);

        Cuboid cube = new Cuboid();
        volume = cube.Volume();
        System.out.println("Volume if the cube is " + volume);
    }
}
