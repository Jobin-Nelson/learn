package streamsdemo;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class StreamDemo {
    public static void main(String arg[]) {
        List<Integer> numbersList = new ArrayList<>();
        numbersList.add(10);
        numbersList.add(20);
        numbersList.add(30);
        numbersList.add(40);

        System.out.println(numbersList);

        // List <Integer> squaresList = new ArrayList<>();
        // for (int i : squaresList) {
        // squareList.add(i*i);
        // }

        // to list with stream
        List<Integer> squaresList = numbersList.stream().map(x -> x * x).collect(Collectors.toList());
        System.out.println("Converted to square list: " + squaresList);

        // Set<Integer> squareSet = new HashSet<>();
        // for (int i : numbersList){
        // squareset.add(i*i);
        // }

        // to set with stream
        Set<Integer> squareSet = numbersList.stream().map(x -> x * x).collect(Collectors.toSet());
        System.out.println("Converted to square set: " + squareSet);

        List<String> languages = new ArrayList<>();
        languages.add("Scala");
        languages.add("Java");
        languages.add("Python");
        languages.add("Javascript");
        languages.add("Basic");
        System.out.println(languages);

        // List<String> filterResult = new ArrayList<>();
        // for (String s : languages){
        // if (s.startsWith("P")){
        // filterResult.add(s);
        // }
        // }

        // filtering with stream
        List<String> filterResult = languages.stream().filter(x -> x.startsWith("P")).collect(Collectors.toList());
        System.out.println("Languages starting with P: " + filterResult);

        // sorting with stream
        List<String> sortedList = languages.stream().sorted().collect(Collectors.toList());
        System.out.println("Languages sorted alphabetically: " + sortedList);

        // iterating with stream
        System.out.println("\nPrinting all elements one by one");
        languages.stream().forEach(x -> System.out.println("element is: " + x));

        // demonstration of reduce method
        // Identity - an element that is the initial value of the reduce operation and
        // the default result if the stream is empty

        // Accumulator - a function that takes two parameters, a partial result of the
        // reduce operation and the next element of the stream

        // Combiner - a function used to combine the partial result when the reduction
        // is parallelized, or when there's a mismatch between the types of accumulator
        // arguments and the types of accumulator implementation
        int sum = numbersList.stream().reduce(0, (ans, x) -> ans + x);
        System.out.println("Sum of all elements in the number list is " + sum);
    }
}
