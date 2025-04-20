public class two_sum{
    public class static int[] twoSum(int[] nums, target){

        // with the help of nested loop and by brute force approach

        // for(int i = 0; i<nums.length; i++){
        //     for(int j=i+1; j<nums.length; j++){
        //         if(nums[i] + nums[j] == target){
        //             return new int[]{i,j}
        //         }
        //     }
        // }
        // return null

        HashMap<Integer> seen = HashMap<>();
        for(int i = 0; i<nums.length;i++){
            int comp = target - nums[i];
            if(seen.containsKay(com)){
                return new int[]{map.get(comp), i};
            }
            seen.put(nums[i],i)
        }
    }
}