class Solution {
    public int longestValidParentheses(String s) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
                //push index value for each open parentheses
            }
            else {
                //pop index value for each close parentheses
                stack.pop();
                if (stack.isEmpty())
                    stack.push(i);
                //new index is added at the end of this valid substring
                else
                    answer = Math.max(answer, i - stack.peek());
            //stack peek looks at integer element at top of stack
            //answer gets updated to whichever string is largest
            }
        }
        return answer;
    }
}