/**
 * Objective: write a program to flag potentially fraudulent transactions in the
 * State of Oklahoma Purchase Card (PCard) Dataset for Fiscal Year 2014.
 *
 *  @author Tiffany Xiao
 *  @version 29 March 2018
 */
import java.util.Scanner;
import java.util.*;
import java.io.*;

public class FraudDetector{

  /* Store the transaction in an array */
  public static ArrayList<Transaction> transactions = new ArrayList<Transaction>();

  /* Constructor */
  public FraudDetector(){
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
      int n = 0;
      while ((line = br.readLine()) != null) {
        // don't do anything for the first line
        if (n != 0){
          String[] tokens = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);
          Transaction transaction = new Transaction(Integer.parseInt(tokens[0]), Integer.parseInt(tokens[1]), tokens[2], tokens[3], tokens[4], tokens[5], Float.parseFloat(tokens[6]), tokens[7], tokens[8], tokens[9], tokens[10]);
          transactions.add(transaction);
        }
        n++;
      }
    } catch(IOException e) {
      System.out.println("File I/O error!");
    }
  }

  /**
   * Method detects all individual transactions exceeding $50,000
   *
   * @return returns an arraylist of all transactions exceeding $50,0000
   */
  public ArrayList<Transaction> transExceed(){
    ArrayList<Transaction> transactionsExceed = new ArrayList<Transaction>();
    for (Transaction transaction:transactions){
      if(transaction.getAmount() > 50000){
        transactionsExceed.add(transaction);
      }
    }
    return transactionsExceed;
  }

  /**
   * Method detects all individual transactions from pawn shops, casinos and resorts
   *
   * @return returns an arraylist of all transactions from pawn shops, casinos and resorts
   */
  public ArrayList<Transaction> transPawn(){
    ArrayList<Transaction> transactionsPawn = new ArrayList<Transaction>();
    for (Transaction transaction:transactions){
      // check if the mcc contains the word "pawn shop", "casino" or "resort"
      String mcc = transaction.getMCC().toUpperCase();
      if(mcc.contains("PAWN SHOP") || mcc.contains("CASINO") || mcc.contains("RESORT") ){
        transactionsPawn.add(transaction);
      }
    }
    return transactionsPawn;
  }

  /**
   * Method detects all individual transactions that are unusually round.
   * Here, we will use if the number is evenly divisible by 100.
   *
   * @return returns an arraylist of all transactions that are unusually round.
   */
  public ArrayList<Transaction> transRound(){
    ArrayList<Transaction> transactionsRound = new ArrayList<Transaction>();
    for (Transaction transaction:transactions){
      if(transaction.getAmount()%100== 0){
        transactionsRound.add(transaction);
      }
    }
    return transactionsRound;
  }

  /**
   * Method to populate a map with the cardholders and their transactions in
   * the global transactions ArrayList
   */
  public Map<String, List<Transaction>> createCardholders(){
    Map<String, List<Transaction>> cardholders = new HashMap<String, List<Transaction>>();
    String name = "";
    // add all unique names into cardholders
    for (Transaction transaction:transactions){
      List<Transaction> cardholderTrans = new ArrayList<Transaction>();
      name = transaction.getCardholderFirst()+" "+transaction.getCardholderLast();
      if (!cardholders.containsKey(name)){
        cardholders.put(name,cardholderTrans);
      }
    }
    // now add all transactions as values for their name key
    for (Transaction transaction:transactions){
      name = transaction.getCardholderFirst()+" "+transaction.getCardholderLast();
      List<Transaction> tempList = new ArrayList<Transaction>();
      tempList = cardholders.get(name);
      tempList.add(transaction);
      cardholders.put(name, tempList);
    }
    return cardholders;
  }

  /**
   * Method to flag users with multiple large ($>20,000) transactions by a single
   * user in a single day
   */
  public ArrayList<String> multipleLarge(Map<String, List<Transaction>> cardholders){
    ArrayList<String> cardholdersLarge = new ArrayList<String>();
    for (String cardholder: cardholders.keySet()) {
      // intialize variable to count number of transactions over $20,000
      int count = 0;
      for(Transaction transaction: cardholders.get(cardholder)){
        if (transaction.getAmount() > 20000){
          count++;
        }
      }
      if (count > 1){
        cardholdersLarge.add(cardholder);
      }
    }
    return cardholdersLarge;
  }

  /**
   * Method to populate a map with the airlines and their transactions from
   * the global transactions ArrayList
   */
  public Map<String, List<Transaction>> createAirlines(){
    Map<String, List<Transaction>> cardholders = new HashMap<String, List<Transaction>>();
    String name = "";
    // add all unique names into cardholders
    for (Transaction transaction:transactions){
      List<Transaction> cardholderTrans = new ArrayList<Transaction>();
      name = transaction.getCardholderFirst()+" "+transaction.getCardholderLast();
      if (!cardholders.containsKey(name)){
        cardholders.put(name,cardholderTrans);
      }
    }
    // now add all transactions as values for their name key
    for (Transaction transaction:transactions){
      name = transaction.getCardholderFirst()+" "+transaction.getCardholderLast();
      List<Transaction> tempList = new ArrayList<Transaction>();
      tempList = cardholders.get(name);
      tempList.add(transaction);
      cardholders.put(name, tempList);
    }
    return cardholders;
  }

  /**
   * Main method to ask user for number of transactions to print out, then prints
   * desired number of transactions.
   *
   * @param args command line arguments
   */
  public static void main(String[] args){
    // read the file line by line and add all lines as transactions
    FraudDetector fraudDetector = new FraudDetector();
    fraudDetector.readFile(args[0]);

    // find all transactions that exceed $50,000
    ArrayList<Transaction> transactionsExceed = fraudDetector.transExceed();

    // print all transactions that exceed $50,000
    System.out.println("Individual transactions exceeding over $50,000:");
    for (Transaction transaction:transactionsExceed){
      transaction.printTransaction();
      System.out.print(" Transaction Amount: "+Float.toString(transaction.getAmount()));
      System.out.println();
    }
    System.out.println("Total transactions that exceed over $50,000: "+Integer.toString(transactionsExceed.size()));
    System.out.println("------------------------------------------------------");

    // find all transactions that are pawn shops, casinos and resorts
    ArrayList<Transaction> transactionsPawn = fraudDetector.transPawn();

    // print all transactions that are pawn shops, casinos and resorts
    System.out.println("Individual transactions that are from pawn shops, casinos and resorts:");
    for (Transaction transaction:transactionsPawn){
      transaction.printTransaction();
      System.out.print(" MCC: "+transaction.getMCC());
      System.out.println();
    }
    System.out.println("Total transactions that are from pawn shops, casinos and resorts: "+Integer.toString(transactionsPawn.size()));
    System.out.println("------------------------------------------------------");

    // find all transactions that are unusually round
    ArrayList<Transaction> transactionsRound = fraudDetector.transRound();

    // print all transactions that are unusually round
    System.out.println("Individual transactions that are unusually round:");
    for (Transaction transaction:transactionsRound){
      transaction.printTransaction();
      System.out.print(" Transaction Amount: "+Float.toString(transaction.getAmount()));
      System.out.println();
    }
    System.out.println("Total transactions that are unusually round: "+Integer.toString(transactionsRound.size()));
    System.out.println("------------------------------------------------------");

    // create a map of cardholders to compile transactions (one cardholder, multiple transactions)
    Map<String, List<Transaction>> cardholders = fraudDetector.createCardholders();

    // search through users and identify users who have multiple large ($>20,000) transactions in a single day
    ArrayList<String> cardholdersLarge = fraudDetector.multipleLarge(cardholders);

    System.out.println("Cardholders With Multiple Large Transactions:");
    for (String cardholder: cardholdersLarge) {
      System.out.println(cardholder);
    }
    System.out.println("Total cardholders with multiple large transactions: "+Integer.toString(cardholdersLarge.size()));
    System.out.println("------------------------------------------------------");

    // determine which transactions feature airlines
    Map<String, List<Transaction>> airlines = fraudDetector.createAirlines();

    // // sort the items in transactions
    // Collections.sort(transactions, new SortbyInt());
    //
    // // ask the user for number of transactions to print
    // System.out.println("Hello :)! How many transactions would you like to see today?");
    // Scanner reader = new Scanner(System.in);
    // int n = reader.nextInt();
    // // check that user put in a valid number
    // while(n > transactions.size() || n < 0 || n == 0){
    //   System.out.println("Whoops! Please try a different number (there are " + transactions.size() + " total transactions).");
    //   n = reader.nextInt();
    // }
    // System.out.println("Great! Now printing top "+Integer.toString(n)+" transactions:");
    //
    // // print the sorted ArrayList
    // int num = 0;
    // for (Transaction transaction:transactions){
    //   transaction.printTransaction();
    //   num++;
    //   if (num == n){
    //     break;
    //   }
    // }
  }

  /**
   * Transaction class (composed of 11 parts: 2 ints (yearMonth and agencyNumber),
   * 1 float (amount), 8 strings (agencyName, cardholderLast, cardholderFirst,
   * description, vendor, transactionDate, postedDate, mcc)
   *
   */
  public class Transaction{
    // create fields for all components of the transaction (each column in csv)
    private int yearMonth;
    private int agencyNumber;
    private String agencyName;
    private String cardholderLast;
    private String cardholderFirst;
    private String description;
    private float amount;
    private String vendor;
    private String transactionDate;
    private String postedDate;
    private String mcc;

    /** Constructor for transaction */
    public Transaction( int yearMonth, int agencyNumber, String agencyName, String cardholderLast, String cardholderFirst, String description, float amount, String vendor, String transactionDate, String postedDate, String mcc){
      this.yearMonth = yearMonth;
      this.agencyNumber = agencyNumber;
      this.agencyName = agencyName;
      this.cardholderLast = cardholderLast;
      this.cardholderFirst = cardholderFirst;
      this.description = description;
      this.amount = amount;
      this.vendor = vendor;
      this.transactionDate = transactionDate;
      this.postedDate = postedDate;
      this.mcc = mcc;
    }

    /** Method to print the transaction */
    public void printTransaction(){
      System.out.print("Cardholder Full Name: ");
      System.out.print(this.cardholderLast + " " + this.cardholderFirst);
    }

    /** Getter for yearMonth */
    public int getYearMonth(){
      return this.yearMonth;
    }

    /** Setter for yearMonth */
    public void setYearMonth(int newYear){
      this.yearMonth = newYear;
    }

    /** Getter for agencyNumber */
    public int getAgencyNumber(){
      return this.agencyNumber;
    }

    /** Setter for agencyNumber */
    public void setAgencyNumber(int newAgency){
      this.agencyNumber = newAgency;
    }

    /** Getter for agencyName */
    public String getAgencyName(){
      return this.agencyName;
    }

    /** Setter for agencyName */
    public void setAgencyName(String newString){
      this.agencyName = newString;
    }

    /** Getter for cardholderLast */
    public String getCardholderLast(){
      return this.cardholderLast;
    }

    /** Setter for cardholderLast */
    public void setCardholderLast(String newString){
      this.cardholderLast = newString;
    }

    /** Getter for cardholderFirst */
    public String getCardholderFirst(){
      return this.cardholderFirst;
    }

    /** Setter for cardholderFirst */
    public void setCardholderFirst(String newString){
      this.cardholderFirst = newString;
    }

    /** Getter for description */
    public String getDescription(){
      return this.description;
    }

    /** Setter for cardholderFirst */
    public void setDescription(String newString){
      this.description = newString;
    }

    /** Getter for amount */
    public float getAmount(){
      return this.amount;
    }

    /** Setter for amount */
    public void setAmount(float newNumber){
      this.amount = newNumber;
    }

    /** Getter for vendor */
    public String getVendor(){
      return this.vendor;
    }

    /** Setter for vendor */
    public void setVendor(String newString){
      this.vendor = newString;
    }

    /** Getter for transactionDate */
    public String getTransactionDate(){
      return this.transactionDate;
    }

    /** Setter for transactionDate */
    public void setTransactionDate(String newString){
      this.transactionDate = newString;
    }

    /** Getter for postedDate */
    public String getPostedDate(){
      return this.postedDate;
    }

    /** Setter for postedDate */
    public void setPostedDate(String newString){
      this.postedDate = newString;
    }

    /** Getter for mcc */
    public String getMCC(){
      return this.mcc;
    }

    /** Setter for mcc */
    public void setMCC(String newString){
      this.mcc = newString;
    }
  }
}
