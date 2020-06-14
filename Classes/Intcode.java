package Classes;

import sun.security.util.ArrayUtil;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.List;

public class Intcode extends OpFile{
    String[] program;
    int opcode_index = 0;
    String path = null;

    public Intcode(String path) {
        super(path);
        // TODO: change String to Integer
        List<String> input = new OpFile(path).open_input();
        this.program = input.get(0).split(",");
    }

    public Intcode(String args, Integer mode) { // for testing purposes - direct input
        super(null);
        this.program = args.split(",");
    }

    public Integer opcodeAdd(String opcode_value){  // Input String value, return number to add to opcode index
        String[] add_four = {"1", "2"};
        String[] add_two = {"3", "4"};
        if (Arrays.asList(add_four).contains(opcode_value)){
            return 4;
        }else if (Arrays.asList(add_two).contains(opcode_value)){
            return 2;
        }
        return null;
    }

    public boolean workingOpcode(String opcode_value){ //check if opcode value can be processed
        String[] working_opcodes = {"1", "2", "3", "4"};
        return Arrays.asList(working_opcodes).contains(opcode_value);
    }

    public Integer resultIndex(String opcode_value){ // return result index according to opcode
        String[] add_three = {"1", "2"};
        String[] add_one = {"3", "4"};
        if (Arrays.asList(add_three).contains(opcode_value)){
            return Integer.parseInt(program[opcode_index + 3]);
        }else if (Arrays.asList(add_one).contains(opcode_value)){
            return Integer.parseInt(program[opcode_index + 1]);
        }
        return null;
    }

    public String calc(){
        int opcode_index = 0;
        String opcode_value_string = program[opcode_index];
        int result_index;

        while (workingOpcode(opcode_value_string)){
            result_index = resultIndex(opcode_value_string);


            if (opcode_value_string.equals("1")){
                program[result_index] = String.valueOf(Integer.parseInt(program[opcode_index + 1]) + Integer.parseInt(program[opcode_index + 2]));
            }else if (opcode_value_string.equals("2")) {
                program[result_index] = String.valueOf(Integer.parseInt(program[opcode_index + 1]) * Integer.parseInt(program[opcode_index + 2]));;
            }


            opcode_index += opcodeAdd(opcode_value_string);
            opcode_value_string = program[opcode_index];

        }





//        String[] opcodes_plus_two = {"3", "4"};
//        System.out.println(opcode_add("3"));

        return program[0];


    }}

