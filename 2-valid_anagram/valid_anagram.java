// valid anagram 
// in sorting of string we need to convert into array first and then we have to sort that array 

import java.util.Arrays;


public class AnagramChecker {
    // by sorting string 

//     public static boolean isAnagramSorting(String s, String t) {
//         if (s.length() != t.length()) {
//             return false;
//         }

//         char[] arr1 = s.toCharArray();
//         char[] arr2 = t.toCharArray();

//         Arrays.sort(arr1);
//         Arrays.sort(arr2);

//         return Arrays.equals(arr1, arr2);
//     }

//  by dictionary 

    public static boolean isAnagramSorting(String s, String t){
        if(s.length() != t.length()){
            return false
        }

        HashMap<Charcter, Integer> map = HashMap<>();

        for(int i = 0; i<s.length(); i++){
            map.put(s.ChatAt(i), map.GetOrDefault(s.ChatAt(i),0) + 1);
            map.put(t.ChatAt(i), map.GetOrDefault(t.ChatAt(i),0) - 1);
        }

        for(val: count.values()){
            if(val != 0){
                return false
            }
        }
        return true
    }
}
