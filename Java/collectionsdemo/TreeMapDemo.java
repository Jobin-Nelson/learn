package collectionsdemo;

import java.util.TreeMap;

public class TreeMapDemo {
    public static void main(String arg[]) {
        TreeMap<Integer, String> treeMap = new TreeMap<>();

        treeMap.put(3, "A");
        treeMap.put(2, "B");
        treeMap.put(1, "C");
        treeMap.put(0, "D");

        System.out.println(treeMap);
    }
}
