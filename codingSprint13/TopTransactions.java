/**
 * Objective: implement a TopTransactions class that reads a
 * sequence of transactions from stdin and prints the M
 * largest in descending order to stdout
 *
 *  @author Tiffany Xiao
 *  @version 27 March 2018
 */
import java.util.Scanner;
import java.util.*;
import java.io.*;

public class TopTransactions{

  /* Store the random responses in an array */
  public static ArrayList<Transaction> transactions = new ArrayList<Transaction>();

  /* Constructor */
  public TopTransactions(){
    // do nothing
  }

  /**
   * Method reads the file and creates a transaction for each line (then adds the
   * transaction to transactions [the ArrayList]).
   *
   * @param file the file to read
   */
  public void readFile(String file){
    try (BufferedReader br = new BufferedReader(new FileReader(file))) {
      String line;
      while ((line = br.readLine()) != null) {
        Transaction transaction = new Transaction(line.substring(0, line.lastIndexOf(" ")), Float.parseFloat(line.substring(line.lastIndexOf(" "))));
        transactions.add(transaction);
      }
    } catch(IOException e) {
      System.out.println("File I/O error!");
    }
  }

  /**
   * Main method to ask user for number of transactions to print out, then prints
   * desired number of transactions.
   *
   * @param args command line arguments
   */
  public static void main(String[] args){
    // read the file line by line and add all lines as transactions
    TopTransactions topTransactions = new TopTransactions();
    topTransactions.readFile(args[0]);
    // sort the items in transactions
    Collections.sort(transactions, new SortbyInt());

    // ask the user for number of transactions to print
    System.out.println("Hello :)! How many transactions would you like to see today?");
    Scanner reader = new Scanner(System.in);
    int n = reader.nextInt();
    // check that user put in a valid number
    while(n > transactions.size() || n < 0 || n == 0){
      System.out.println("Whoops! Please try a different number (there are " + transactions.size() + " total transactions).");
      n = reader.nextInt();
    }
    System.out.println("Great! Now printing top "+Integer.toString(n)+" transactions:");

    // print the sorted ArrayList
    int num = 0;
    for (Transaction transaction:transactions){
      transaction.printTransaction();
      num++;
      if (num == n){
        break;
      }
    }
  }

  /**
   * Class for comparator that compares numberPart of the transactions.
   */
  public static class SortbyInt implements Comparator<Transaction>
  {
    /**
     * Compare the two transactions
     *
     *  @param a first transaction to compare
     *  @param b second transaction to compare
     *  @return returns an integer indicating which is the larger transaction
     */
      public int compare(Transaction a, Transaction b)
      {
          return -(Float.compare(a.numberPart, b.numberPart));
      }
  }

  /**
   * Transaction class (composed of two parts: a string (stringPart) and a
   * number (numberPart))
   */
  public class Transaction{
    private String stringPart = "";
    private float numberPart;

    /** Constructor for transaction */
    public Transaction(String stringPart, float numberPart){
      this.stringPart = stringPart;
      this.numberPart = numberPart;
    }

    /** Method to print the transaction */
    public void printTransaction(){
      System.out.println(this.stringPart + " " + Float.toString(this.numberPart));
    }
  }
}
