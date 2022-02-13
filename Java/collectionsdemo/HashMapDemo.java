package collectionsdemo;

import java.util.HashMap;
import java.util.Map.Entry;

public class HashMapDemo {
    public static void main(String arg[]) {
        HashMap<String, Integer> map = new HashMap<>();

        map.put("a", 10);
        map.put("b", 20);
        map.put("c", 30);

        System.out.println("Size of the map is: " + map.size());
        System.out.println(map);

        if (map.containsKey("a")) {
            Integer a = map.get("a");
            System.out.println("Value for key a is: " + a);
        }

        for (String key : map.keySet()) {
            System.out.println("Key: " + key + ", value: " + map.get(key));
        }

        // each entry in a map is of entry class
        for (Entry<String, Integer> entry : map.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", value: " + entry.getValue());
        }
    }
}
