class Result {

    /*
     * Complete the 'doesCircleExist' function below.
     *
     * The function is expected to return a STRING_ARRAY.
     * The function accepts STRING_ARRAY commands as parameter.
     */

    public static List<String> doesCircleExist(List<String> commands) {
    // Write your code here
    int x = 0, y = 0; 
    int dir = 0; 
    char[] path = new char[commands.size()];
    ArrayList<String> solution = new ArrayList<String>();

    for(int j = 0;j< commands.size();j++){
    x = 0; 
    y =0;
    dir = 0;
    path = commands.get(j).toCharArray();
    for (int i=0; i < path.length; i++) 
    { 
        
        char move = path[i]; 
    
        if (move == 'R') 
        dir = (dir + 1)%4; 
        else if (move == 'L') 
        dir = (4 + dir - 1) % 4; 

        
        else 
        { 
        if (dir == 0) 
            y++; 
        else if (dir == 1) 
            x++; 
        else if (dir == 2) 
            y--; 
        else // dir == 3 
            x--; 
        } 
    } 

    //return (x == 0 && y == 0);

    if (x == 0 && y == 0) 
    solution.add("YES"); 
    else
    solution.add("NO"); 
    }
    return solution;
        

        }
    
}