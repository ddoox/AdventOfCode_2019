package Classes.Tests;

import Classes.Intcode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class IntcodeTest {

//    private Intcode intcode = new Intcode("Classes/Tests/dummyinput.txt");
    private Intcode intcode = new Intcode("1,0,0,0,99",1);

    @Test
    void opcodeAddTest() {
        assertEquals(2, intcode.opcodeAdd("3"));
        assertEquals(2, intcode.opcodeAdd("4"));
        assertEquals(4, intcode.opcodeAdd("1"));
        assertEquals(4, intcode.opcodeAdd("2"));
    }

    @Test
    void workingOpcodesTest() {
        assertTrue(intcode.workingOpcode("1"));
        assertTrue(intcode.workingOpcode("2"));
        assertTrue(intcode.workingOpcode("3"));
        assertTrue(intcode.workingOpcode("4"));
        assertFalse(intcode.workingOpcode("5"));
        assertFalse(intcode.workingOpcode("6"));
        assertFalse(intcode.workingOpcode("7"));
        assertFalse(intcode.workingOpcode("8"));
        assertFalse(intcode.workingOpcode("9"));
    }
}