package Day_01;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Day_01{

    static int calculate_fuel(int mass){
        int _mass = mass;
        _mass = _mass - _mass % 3;
        _mass = _mass / 3 - 2;
        return _mass;
    }

    static List open_input(String path){
        ArrayList list = new ArrayList();

        try {
            BufferedReader reader = new BufferedReader(new FileReader(path));
            String line;

            while ((line = reader.readLine()) != null) {
                list.add(line);
            }
            reader.close();
            return list;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args){

        List<String> input = open_input("Day_01/input.txt");
        int fuel_sum = 0;

        for (String module : input) { // Python "for module in input"
            fuel_sum += calculate_fuel(Integer.parseInt(module));
        }

        System.out.println(fuel_sum);
    }
}