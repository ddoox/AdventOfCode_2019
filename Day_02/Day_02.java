package Day_02;

import Classes.Intcode;

import java.util.Arrays;
import java.util.List;

public class Day_02 {

    public static void main(String[] args) {
        Intcode intcode = new Intcode("Day_02/input.txt");

//        List<Integer> input = Arrays.asList(1,1,1,4,99,5,6,0,99);

//        Intcode intcode = new Intcode(input, 1);
        System.out.println(intcode.calc());
    }

}
