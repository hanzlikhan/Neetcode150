class Static Is_duplicate{
    class boolean Is_duplicate(int[] arr, int n){
        // with for loop and its time complexity O(n^2)
        for (int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(arr[i] == arr[j]){
                    return true;
                }
            }
        }
        return false;

    }
    // with sorting method and time complexity O(nlogn)

    class boolean Is_duplicate_sorting(int[] arr, int n){
        Arrays.sort(arr);
        for (int i=0;i<n-1;i++){
            if(arr[i] == arr[i+1]){
                return true;
            }
        }
        return false;
    }
    // with HashSet and time complexity O(n)
    class boolean Is_duplicate_hashset(int[] arr, int n){
        // HashSet<Integer> set = new HashSet<>();
        HashSet<Integer> set = new HashSet<>();
        for(int i=0;i<n;i++){
            if(set.contains(arr[i])){
                return true;
            }
            set.add(arr[i]);
        }
        return false;
    }
    // with HashMap and time complexity O(n)
    class boolean Is_duplicate_hashmap(int[] arr, int n){
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0;i<n;i++){
            if(map.containsKey(arr[i])){
                return true;
            }
            map.put(arr[i], 1);
        }
        return false;
    }
}
