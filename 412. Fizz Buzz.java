class Solution {
    public List<String> fizzBuzz(int n) {
        //Maybe I should've done this with lists rather than arrays but being inflexible comes with speed
        String[] answer = new String[n];
        for(int i=1; i< n+1; i++){
            answer[i-1] = String.valueOf(i); //i.toString();
        }
        for(int t=2; t<n; t+=3){
            answer[t] = "Fizz";
        }
        for(int f=4; f<n; f+=5){
            if((f+1)%3 == 0){
                answer[f] = "FizzBuzz";
            }
            else{
                answer[f] = "Buzz";
            }
        }
        return Arrays.asList(answer);
    }
}