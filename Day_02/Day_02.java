package Day_02;

import Classes.Intcode;

public class Day_02 {

    public static void main(String[] args) {
//        Intcode intcode = new Intcode("Day_02/input.txt");
        Intcode intcode = new Intcode("1,0,0,0,99", 1);
        System.out.println(intcode.calc());
    }

}
