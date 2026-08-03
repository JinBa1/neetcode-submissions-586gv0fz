class Solution {

    public boolean isOpen(String a) {
        Boolean isOpen = switch(a){
            case "(" -> true;
            case "{" -> true;
            case "[" -> true;
            default -> false;
        };

        return isOpen;
    }


    public boolean isValid(String s) {
        var stack = new Stack<String>();

        for(int i = 0; i < s.length(); i++) {
            String curr = String.valueOf(s.charAt(i));

            if (isOpen(curr)) {
                stack.push(curr);
            } else {
                if (stack.isEmpty()) return false;
                String poped = stack.pop();
                Boolean isLegal = switch(poped + curr) {
                    case "()" -> true;
                    case "[]" -> true;
                    case "{}" -> true;
                    default -> false;
                };

                if (!isLegal) return false;
            }

        }

        return stack.isEmpty();

    }
}
