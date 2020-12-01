package PasswordEncryptor;

import java.awt.Point;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class PasswordEncryptor {
    private static final char[] morse = {'K', 'S', 'T', 'R', 'E', 'V'};
    private Column[] col;
    private Column[] colAlpha;
    private char[][] grid = ((char[][]) Array.newInstance(Character.TYPE, morse.length, morse.length));
    private String key;

    public PasswordEncryptor(String key2) {
        ArrayList<Character> al = new ArrayList<>(Arrays.asList('9', 'T', 'G', 'Y', '6', 'E', 'R', 'N', 'A', 'Q', 'P', '5', 'X', 'K', 'H', '4', 'U', 'W', 'I', 'M', '1', 'C', 'V', '7', '3', 'S', 'O', 'D', '2', 'J', 'L', '8', '0', 'B', 'T', 'F', 'Z'));
        int index = 35;
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                if (!al.isEmpty()) {
                    this.grid[i][j] = al.remove(index).charValue();
                    index--;
                }
            }
        }
        setKey(key2);
    }

    public void setKey(String key2) {
        if (key2 == null) {
            this.key = "";
            return;
        }
        char[] digit = key2.toCharArray();
        int len = digit.length;
        for (int i = 0; i < len - 1; i++) {
            for (int j = i + 1; j < len; j++) {
                if (digit[i] == digit[j]) {
                    this.key = "";
                    return;
                }
            }
        }
        this.key = key2;
        this.col = new Column[len];
        this.colAlpha = new Column[len];
        for (int i2 = 0; i2 < len; i2++) {
            this.col[i2] = new Column(digit[i2]);
            this.colAlpha[i2] = this.col[i2];
        }
        Arrays.sort(this.colAlpha);
    }

    public String encode(String clear) {
        char[] digit = PasswordEncryptorToProcess(clear, true);
        if (digit.length == 0) {
            return "";
        }
        siapinKolyuk(digit.length * 2);
        int length = digit.length;
        int i = 0;
        int k = 0;
        while (i < length) {
            Point p = hayuk(digit[i]);
            this.col[k].add(morse[p.x]);
            int k2 = (k + 1) % this.col.length;
            this.col[k2].add(morse[p.y]);
            i++;
            k = (k2 + 1) % this.col.length;
        }
        StringBuilder sb = new StringBuilder(digit.length * 2);
        for (Column c2 : this.colAlpha) {
            sb.append(c2.toString());
        }
        char[] digit2 = sb.toString().toCharArray();
        StringBuilder sb2 = new StringBuilder(digit2.length + (digit2.length / 2));
        sb2.append(digit2[0]);
        sb2.append(digit2[1]);
        for (int i2 = 2; i2 < digit2.length; i2 += 2) {
            sb2.append(' ');
            sb2.append(digit2[i2]);
            sb2.append(digit2[i2 + 1]);
        }
        return sb2.toString();
    }

    private char[] PasswordEncryptorToProcess(String str, boolean coding) {
        if (str == null) {
            return new char[0];
        }
        if (this.key.length() == 0) {
            return new char[0];
        }
        StringBuilder sb = new StringBuilder(this.key.length());
        char[] charArray = str.toUpperCase().toCharArray();
        for (char c : charArray) {
            if (!coding) {
                char[] cArr = morse;
                int length = cArr.length;
                int i = 0;
                while (true) {
                    if (i >= length) {
                        break;
                    } else if (cArr[i] == c) {
                        sb.append(c);
                        break;
                    } else {
                        i++;
                    }
                }
            } else if ((c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
                sb.append(c);
            }
        }
        char[] digit = sb.toString().toCharArray();
        if (digit.length == 0 || coding || digit.length % 2 == 0) {
            return digit;
        }
        return new char[0];
    }

    private void siapinKolyuk(int len) {
        int nbPerCol = len / this.col.length;
        int[] nb = new int[this.col.length];
        for (int i = 0; i < this.col.length; i++) {
            nb[i] = nbPerCol;
        }
        int reminder = len - (this.col.length * nbPerCol);
        for (int j = 0; j < reminder; j++) {
            nb[j] = nb[j] + 1;
        }
        for (int j2 = 0; j2 < this.col.length; j2++) {
            this.col[j2].setSize(nb[j2]);
        }
    }

    private Point hayuk(char c) {
        for (int x = 0; x < 6; x++) {
            for (int y = 0; y < 6; y++) {
                if (c == this.grid[x][y]) {
                    return new Point(x, y);
                }
            }
        }
        throw new IllegalStateException("Character " + c + " not found in Grid");
    }

    public char[][] getGrid() {
        return this.grid;
    }

    public char[] getMorse() {
        return morse;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Masukkan Kunci: ");
        PasswordEncryptor aaaaaa = new PasswordEncryptor(scan.nextLine());

        System.out.print("Masukkan Pesan: ");
        String PasswordEncryptor2 = scan.nextLine();
        
        aaaaaa.encode(PasswordEncryptor2);
        System.out.println("Hasil : " + aaaaaa.encode(PasswordEncryptor2));
    }

    /* access modifiers changed from: private */
    public class Column implements Comparable<Column> {
        private char header;
        private int index;
        private char[] letters;

        Column(char header2) {
            this.header = header2;
        }

        /* access modifiers changed from: package-private */
        public void setSize(int size) {
            this.letters = new char[size];
            this.index = 0;
        }

        /* access modifiers changed from: package-private */
        public int getSize() {
            return this.letters.length;
        }

        /* access modifiers changed from: package-private */
        public void add(char c) {
            char[] cArr = this.letters;
            int i = this.index;
            this.index = i + 1;
            cArr[i] = c;
        }

        /* access modifiers changed from: package-private */
        public char getChar(int n) {
            return this.letters[n];
        }

        public String toString() {
            return new String(this.letters);
        }

        public int compareTo(Column other) {
            return this.header - other.header;
        }
    }
}
