package Classes;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Intcode extends OpFile{
    List<Integer> program;
    int opcode_index = 0;

    public Intcode(String path) {
        super(path);
        List<String> inputFile = new OpFile(path).open_input();
        List<Integer> inputInt = new ArrayList<Integer>(inputFile.size());
        for(String str : inputFile.get(0).split(",")) {
            inputInt.add(Integer.valueOf(str));
        }
        this.program = inputInt;
    }

    public Intcode(List<Integer> inputDirect, Integer mode) { // for testing purposes - direct input
        super(null);
        this.program = inputDirect;
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

    public boolean workingOpcode(String opcode_value){ // check if opcode value can be processed
        String[] working_opcodes = {"1", "2", "3", "4"};
        return Arrays.asList(working_opcodes).contains(opcode_value);
    }

    public Integer resultIndex(String opcode_value){ // return result index according to opcode
        String[] add_three = {"1", "2"};
        String[] add_one = {"3", "4"};
        if (Arrays.asList(add_three).contains(opcode_value)){
            return program.get(opcode_index + 3);
        }else if (Arrays.asList(add_one).contains(opcode_value)){
            return program.get(opcode_index + 1);
        }
        return null;
    }

    public List<Integer> getEndState(){ // run program and return it's state - useful for testing
        calc();
        return program;
    }

    public Integer calc(){
//        Integer opcode_value_int = program.get(opcode_index); // future use
        String opcode_value_string = String.valueOf(program.get(opcode_index));
        int result_index;

        while (workingOpcode(opcode_value_string)){
            result_index = resultIndex(opcode_value_string);

            if (opcode_value_string.equals("1")){
                program.set(result_index, program.get(program.get(opcode_index + 1)) + program.get(program.get(opcode_index + 2)));
            }else if (opcode_value_string.equals("2")) {
                program.set(result_index, program.get(program.get(opcode_index + 1)) * program.get(program.get(opcode_index + 2)));
            }

            opcode_index += opcodeAdd(opcode_value_string);
            opcode_value_string = String.valueOf(program.get(opcode_index));
        }

        return program.get(0);
    }}

