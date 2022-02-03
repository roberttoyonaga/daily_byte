/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.*;

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        /*
        List is an interface. ArrayList is mutable. But has amortize O(1) complexity for add. Will eventiallu take O(n) time to copy to new array once allocated space is used up. 
        */
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        /* can't use:
        List<List<Integer>> result = new ArrayList<ArrayList<Integer>>();
        because if you had a List<List<Integer>> then you'd be able to add a LinkedList<Integer> to it.
        But you can't do this for an ArrayList<ArrayList<Integer>>
        
        In java objects only have methods that you can access corresponding to the interface they are declared as. Instead of delcaring as an interface, you can declare as the actual class type if you want to use all the methods.
        */
        if (root == null){
            return result;
        }
        queue.add(root);
        
        boolean leftToRight = false;
        
        while(queue.size() > 0){
            System.out.println("level "+queue.size());
            for (TreeNode treeNode : queue){
                System.out.println(treeNode.val);
            }
            int levelSize = queue.size();
            Deque<Integer> level = new ArrayDeque<Integer>();
            System.out.println("left to right "+leftToRight);
            for (int i=0; i<levelSize; i++){
                TreeNode node = null;
               
                node = queue.poll();
                if (node.left != null){
                    queue.add(node.left);
                }
                if (node.right != null){
                   queue.add(node.right); 
                }
                    
               
               // This is where the zig zagging happens
            
                if (leftToRight){
                    level.addFirst(node.val);
                }
                else{
                    level.add(node.val);
                }
            }
            result.add(new ArrayList(level));
            leftToRight = !leftToRight; //toggle
        }
        return result;
    }
}