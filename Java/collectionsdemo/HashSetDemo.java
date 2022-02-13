package collectionsdemo;

import java.util.*;

public class HashSetDemo {
    public static void main(String arg[]) {
        Set<String> hashSet = new HashSet<>();

        hashSet.add("A");
        hashSet.add("B");
        hashSet.add("C");
        hashSet.add("C");

        System.out.println(hashSet);

        System.out.println("List contains C or not? " + hashSet.contains("C"));

        hashSet.remove("A");
        System.out.println("List after removing A: " + hashSet);

        for (String i : hashSet) {
            System.out.println(i);
        }
    }
}
