package dp;

import java.util.logging.Logger;

public class CoinChange {
    
    private static final Logger log = Logger.getLogger(CoinChange.class.getName());
    
    public static void main(String[] args){
        log.info("" + solve(new int[]{3, 2}, 11));
    }
    
    public static int solve(int[] coins, int amount){
        return dp1(coins,0,amount,0);
    }
    
    
    
    
    public static int dp1(int[] coins, int coin, int target, int count){
        if(target == 0) return count;
        if(coin >= coins.length) return -1;
        int result1;
        int result2 = -1;
        
        if(target > coins[coin]){
            result1 = dp1(coins, coin,target-coins[coin],count+1);
            result2 = dp1(coins, coin+1, target, count);
        }else{
            result1 = dp1(coins,coin+1,target,count);
        }
        
        return (result1!=-1 && result2!=-1) ? Math.min(result1,result2) : Math.max(result1,result2);
    }
}
