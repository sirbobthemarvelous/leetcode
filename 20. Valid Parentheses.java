class Solution {
    public boolean isValid(String s) {
        Stack<Character> bracket = new Stack<>();
        for (char brace : s.toCharArray()) {
             switch (brace) {
                case '(': bracket.push(brace); break;
                case '{': bracket.push(brace); break;
                case '[': bracket.push(brace); break;
                case ')': if (bracket.empty() || bracket.peek()!='(') return false; else bracket.pop(); break;
                case '}': if (bracket.empty() || bracket.peek()!='{') return false; else bracket.pop(); break;
                case ']': if (bracket.empty() || bracket.peek()!='[') return false; else bracket.pop(); break;
                default: ; 
            }
        }
        return bracket.isEmpty();
    }
}