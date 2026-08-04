/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode n1 = head;
        if(head == null) return head;

        ListNode n2 = head.next;

        n1.next = null;
        if(n2 == null) return head; // single element linked list

        ListNode n3 = n2.next;

        while (n3 != null) {
            // System.out.println("n1: " + n1.val + " n2: " + n2.val + " n3: " + n3.val);


            n2.next = n1;
            n1 = n2;
            n2 = n3;
            n3 = n3.next;
        }

        n2.next = n1;


        return n2;

    }
}
