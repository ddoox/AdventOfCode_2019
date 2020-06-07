package Classes;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

/**
 * The OpFile return ArrayList which contain data from file in given path
 */

public class OpFile {
    String path = null;

    public OpFile(String path){
        this.path = path;
    }

    public ArrayList open_input(){
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
}
