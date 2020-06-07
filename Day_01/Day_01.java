package Day_01;

import Classes.OpFile;
import java.util.List;

public class Day_01{

    static int calculate_fuel(int mass){
        int _mass = mass;
        _mass = _mass - _mass % 3;
        _mass = _mass / 3 - 2;
        return _mass;
    }

    public static void main(String[] args){

        List<String> input = new OpFile("Day_01/input.txt").open_input();
        int fuel_sum = 0;
        int current_fuel_weight = 0;

        for (String module : input) { // Python "for module in input"
            current_fuel_weight = calculate_fuel(Integer.parseInt(module));
            fuel_sum += current_fuel_weight;

            while(current_fuel_weight >= 0){
                current_fuel_weight = calculate_fuel(current_fuel_weight);

                if (current_fuel_weight > 0)
                        fuel_sum += current_fuel_weight;
            }
        }

        System.out.println(fuel_sum);
    }
}