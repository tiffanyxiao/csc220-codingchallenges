import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Program to flag potentially fraudulent transactions in the
 * State of Oklahoma Purchase Card (PCard) Dataset for Fiscal Year 2014.
 *
 * @author Karen Santamaria and Tiffany Xiao
 * @version 4 April 2018
 */
public class FraudDetector {

    /** All the transactions in input file */
    private List<Transaction> transactions;

    /**
     * Read the csv file and call addTransaction to convert the line into a transaction
     * @param filename name of csv
     */
    public void formTransaction(String filename){
        transactions = new ArrayList<>();
        try {
            BufferedReader buff = new BufferedReader(new FileReader(filename));
            Scanner input = new Scanner(buff);
            input.nextLine(); //ignore the column names
            while (input.hasNextLine()) {
                String line = input.nextLine();
                addTransaction(line);
            }
        } catch(IOException e){
            System.err.print("Problem reading file");
        }
    }

    /**
     * Converts the line into an instance of the transaction class, then
     * adds to global transactions list.
     *
     * @param line from csv file that has been read
     */
    public void addTransaction(String line){
        // split line into tokens for transaction fields
        String[] tokens = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);
        String name = tokens[3] + " " + tokens[4];
        // format date neatly (mm/dd/year format)
        Date date = new Date();
        try {
            date = new SimpleDateFormat("MM/dd/yyyy").parse(tokens[8].substring(0,10));
        } catch (ParseException e) {
            e.printStackTrace();
        }
        transactions.add(new Transaction(name, date, Float.parseFloat(tokens[6]), tokens[5], tokens[10], tokens[7]));
    }

    /**
     * Add potentially fraudulent transactions to a list, and return the list.
     *
     * @return possibly fraudulent transactions
     */
    public Set<Transaction> getFraud() {

        Set<Transaction> posFraud = new HashSet<>(); //possibly fraudulent transactions

        //transactions grouped by cardholder
        Map<String, List<Transaction>> transByHolder = transactions.stream().collect(Collectors.groupingBy(Transaction::getCardholder));

        for (String name : transByHolder.keySet()) {
            // the easy things to flag
            for (Transaction t : transByHolder.get(name)){
                if(t.getAmount() > 50000){ // flag if transaction is larger than 50000
                    posFraud.add(t);
                    t.setFraud();
                    t.setFraudReason("Individual transactions exceeding $50,000");
                }
                if(t.getAmount() % 100 == 0 ){ // flag unusually round transactions
                    posFraud.add(t);
                    t.setFraud();
                    t.setFraudReason("Unusually round transaction");
                }
                if(t.getMCC().contains("pawn")|| t.getMCC().contains("casino")|| t.getMCC().contains("resort")){ // flag transactions from casinos, resorts and pawn shops
                    posFraud.add(t);
                    t.setFraud();
                    t.setFraudReason("Transaction from pawn shop, casino or resort");
                }
                // extra credit: check if description is valid
                if(t.getDescription().contains("0") || t.getDescription().isEmpty() || t.getDescription().contains("PCE") || isNumeric(t.getDescription())){
                  posFraud.add(t);
                  t.setFraud();
                  t.setFraudReason("Transaction has invalid description.");
                }
            }

            // flag large transactions in same day by same person
            List<Transaction> transByHolderVal = transByHolder.get(name);
            Map<Date, List<Transaction>> transByHolderDate = transByHolderVal.stream().collect(Collectors.groupingBy(Transaction::getDate));
            for (Date day : transByHolderDate.keySet()) {  //for every day a person had a transaction
                List<Transaction> holderDateVal = transByHolderDate.get(day); //transactions grouped by day
                ArrayList<Transaction> copy = new ArrayList<>(holderDateVal); //create copy to prevent concurrent mod
                copy.removeIf(s -> s.getAmount() <= 20000); //remove all values less than 20,000
                if (copy.size() > 1) { //if there are more than two large purchases, its fraud
                    // set fraud, and add the fraud reason
                    copy.forEach(Transaction::setFraud);
                    copy.forEach((item) -> item.setFraudReason("Multiple large ($>20,000) transactions by a single user in a single day"));
                    posFraud.addAll(copy);
                }
            }
        }

        // flag uncommon airline
        transactions.removeIf(t -> (!t.getMCC().contains("airline")));

        Map<String, List<Transaction>> airlineMap = transactions.stream().collect(Collectors.groupingBy(w -> w.getVendor()
                .split("(?<=\\D)(?=\\d)|(?<=\\d)(?=\\D)")[0])); //split by number because some vendors have unique number for each transaction

        for (String airline : airlineMap.keySet()) {
            if (airlineMap.get(airline).size() < 10) {
                airlineMap.get(airline).forEach(Transaction::setFraud);
                airlineMap.get(airline).forEach((item) -> item.setFraudReason("Infrequently used airlines (fewer than 10 occurrences)"));
                posFraud.addAll(airlineMap.get(airline));
            }
        }
        return posFraud;
    }

    /**
     * Method to detect if the string is a number
     *
     * @return true if string is a number, else false
     */
    public static boolean isNumeric(String str){
      try{
        double d = Double.parseDouble(str);
      }
      catch(NumberFormatException nfe){
        return false;
      }
      return true;
    }

    /**
     * Main method to read csv file and find fraudulent transactions.
     *
     * @param args input in console
     */
    public static void main(String[] args) {
        FraudDetector detector = new FraudDetector();
        // read csv file
        detector.formTransaction(args[0]);
        // create set with fraudulent transactions
        Set<Transaction> posFraud = detector.getFraud();
        // print all fraudulent transactions
        for (Transaction t: posFraud){
            System.out.println(t + " " + " | Reason For Fraud Marking: "+ t.getFraudReason());
        }
    }

    /** Transaction class which contains fields/data on individual transactions */
    private class Transaction implements Comparable<Transaction>{

        /** Cardholder of transaction */
        private final String cardholder;

        /** Date of transaction */
        private final Date date;

        /** Amount of money involved in transaction */
        private final Float amount;

        /** Description of transaction */
        private final String description;

        /** Merchant Category of transaction */
        private final String mcc;

        /** Vendor involved in transaction */
        private final String vendor;

        /** Status of flag for fraud */
        private boolean fraud;

        /** Reason transaction is categorized as fraudulent */
        private String fraudReason;

        /**
         * Constructor for Transaction
         * @param cardholder last name and first initial
         * @param date formatted date
         * @param amount amount as a float
         * @param description type of transaction
         * @param mcc merchant category code
         * @param vendor vendor involved
         */
        Transaction(String cardholder, Date date, Float amount, String description, String mcc, String vendor){
            this.cardholder = cardholder;
            this.date = date;
            this.amount = amount;
            this.description = description;
            this.mcc = mcc.toLowerCase();
            this.vendor = vendor;
            // also set fraud and fraudReason
            this.fraud = false;
            this.fraudReason = "";
        }

        /**
         * Getter for amount
         * @return amount
         */
        private Float getAmount(){
            return amount;
        }

        /**
         * Getter for vendor
         * @return vendor
         */
        private String getVendor(){
            return vendor;
        }

        /**
         * Getter for cardholder
         * @return cardholder name
         */
        private String getCardholder(){
            return cardholder;
        }

        /**
         * Getter for description
         * @return description
         */
        private String getDescription(){
            return description;
        }

        /**
         * Getter for merchant code
         * @return merchant code
         */
        private String getMCC(){
            return mcc;
        }

        /**
         * Getter for date
         * @return date
         */
        private Date getDate(){
            return date;
        }

        /**
         * Getter for fraud status
         * @return fraud status
         */
        private boolean getFraud(){
            return fraud;
        }

        /**
         * Setter for transaction fraud
         */
        private void setFraud(){
            this.fraud = true;
        }



        /**
         * Getter for reason transaction is flagged
         * @return reason for fraud as string, empty if not flagged
         */
        private String getFraudReason(){
            return fraudReason;
        }

        /**
         * Setter for fraud reason
         * @param string reason transaction is flagged
         */
        private void setFraudReason(String string){
            if (this.fraudReason.equals("")){
                this.fraudReason = string;
            } else {
                this.fraudReason += " & " + string;
            }
        }

        /**
         * Convert transaction to string
         * @return transaction as a string
         */
        public String toString() {
            return "Transaction: "+date.toString().substring(4,10) + " | Cardholder: " + cardholder + " | Amount: " + amount ;

        }

        @Override
        public int compareTo(Transaction other){
            return Float.compare(amount, other.amount);
        }
    }

}
