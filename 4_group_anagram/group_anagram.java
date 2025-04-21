import java.util.*;

public class GroupAnagrams {
    
    public static List<List<String>> groupAnagrams(String[] strs) {
        // Map where key is the sorted word and value is the list of anagrams
        HashMap<String, List<String>> anagramMap = new HashMap<>();

        for (String word : strs) {
            // Convert the word to a char array and sort it
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);

            // If the sorted word is not already a key, add a new list
            if (!anagramMap.containsKey(sortedWord)) {
                anagramMap.put(sortedWord, new ArrayList<>());
            }

            // Add the original word to the corresponding list
            anagramMap.get(sortedWord).add(word);
        }

        // Return the grouped values as a list of lists
        return new ArrayList<>(anagramMap.values());
    }

    // Example usage
    public static void main(String[] args) {
        String[] input = {"act", "pots", "tops", "cat", "stop", "hat"};
        List<List<String>> grouped = groupAnagrams(input);
        System.out.println(grouped);
    }
}
