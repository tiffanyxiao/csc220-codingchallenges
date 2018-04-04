import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

public class FormTransaction {

    private ArrayList<Transaction> transactions;


    public FormTransaction(String filename){

        ArrayList<Transaction> info = new ArrayList<>();
        try {
            BufferedReader extBuff = new BufferedReader(new FileReader(filename));
            Scanner input = new Scanner(extBuff);



            /* this is just for my sake */

            String line0 = input.nextLine();

            String[] tokens = line0.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);

            for (int i = 0; i < tokens.length; i++){
                System.out.println(i + " " + tokens[i]);
            }


            /* end of it */


//            input.nextLine();

            while (input.hasNextLine()) {

                String line = input.nextLine();

                info.add(createTransaction(line));

            }
        } catch(IOException e){
            System.err.print("Problem reading file");

        }


        transactions = info;
    }

    private Transaction createTransaction(String line){

        String[] tokens = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);

        String name = tokens[3] + " " + tokens[4];
        Date date = new Date();

        try {
            date = new SimpleDateFormat("MM/dd/yyyy").parse(tokens[8].substring(0,10));

        } catch (ParseException e) {
            e.printStackTrace();
        }

        Float amount = Float.parseFloat(tokens[6]);
        String vendor = tokens[7] ;
        String description = tokens[5];


        return new Transaction(name, date, amount, vendor, description, tokens[10]);

    }


    public ArrayList<Transaction> getTransactions(){
        return transactions;
    }

}
