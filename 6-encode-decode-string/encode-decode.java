import java.util.*;

public class Codec {

    // Encode a list of strings to a single string
    public String encode(List<String> strs) {
        // StringBuilder encoded = new StringBuilder();
        // for (String str : strs) {
        //     encoded.append(str.length()).append("#").append(str);
        // }
        // return encoded.toString();

        StringBuilder encoded = new StringBuilder();
        for(String str: strs){
            encoded.append(str.length()).append('#').append(str)
        }
        return encoded.toString();
    }

    // Decode the encoded string back to list of strings
    public List<String> decode(String s) {
        List<String> decoded = new ArrayList<>();
        int i = 0;

        while (i < s.length()) {
            int j = i;
            // Find the delimiter #
            while (s.charAt(j) != '#') {
                j++;
            }

            int length = Integer.parseInt(s.substring(i, j));
            j++; // Skip '#'
            String word = s.substring(j, j + length);
            decoded.add(word);

            i = j + length; // Move to the next word
        }

        return decoded;
    }
}
