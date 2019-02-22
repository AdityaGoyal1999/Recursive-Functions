
/**
 * Write a description of class Recursion here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Recursion
{
    public void Recurion()
    {
    }
    
    public int factorial(int n)
    {
        if(n == 1)
            return 1;
        else
        {
            int a = n;
            a *= factorial(n-1);
            return a;
        }
    }
    public static void main(String args[])
    {
        Recursion r = new Recursion();
        System.out.println(r.factorial(5));
    } 
}

