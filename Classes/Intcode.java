package Classes;

import java.util.List;

public class Intcode extends OpFile{
    List<String> input = new OpFile("Day_02/input.txt").open_input();

    public Intcode(String path) {
        super(path);
    }

    public String calc(){
        return input.get(0);


    }
}
