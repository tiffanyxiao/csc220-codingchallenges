/**
 *  Objective: write a Java program that reads in a yes/no question from the user
 *  and returns a random prediction
 *
 *  @author Tiffany Xiao
 *  @version 24 March 2018
 */
import java.util.Scanner;
import java.util.Random;

public class codingSprint12{

  /* Store the random responses in an array */
  public static String[] responses = {"definitely", "ehhh ... probably not", "nah", "i don't think so","perhaps", "most likely", "yaaas gurl definitely!", "for sure", "maybe next time"};

  /**
   * Method asks user for their question, then generates random response
   *
   * @param i the question/round number
   * @param reader the scanner for reading input
   */
  public static void generateResponse(int i, Scanner reader){
    // ask the user for their question
    System.out.println("Enter Question "+i+" below: ");
    String response = reader.nextLine();
    // generate a random response with a random number (response from array)
    Random rand = new Random();
    int n = rand.nextInt(responses.length-1)+0;
    System.out.println(responses[n]);
  }

  /**
   * Main method to ask user for number of questions, then calls generateResponse()
   *
   * @param args command line arguments
   */
  public static void main(String[] args){
    // ask user how many times they'd like to play the game
    Scanner reader = new Scanner(System.in);
    System.out.println("Welcome to the miraculous magic 8 ball (property of Tiffany Xiao).");
    System.out.println("Enter number of questions you'd like to ask this great ball: ");
    int n = reader.nextInt();
    reader.nextLine();

    for (int i = 0; i<n; i++){
      generateResponse(i, reader);
    }
  }
}
