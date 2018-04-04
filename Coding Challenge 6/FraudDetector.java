import java.util.*;
import java.util.stream.Collectors;


public class FraudDetector {



    /**
     Individual transactions exceeding $50,000
     Pawn shops, casinos and resorts
     Transactions whose value is unusually "round" (i.e. evenly divisible by $100)
     */
//    private static ArrayList<Transaction> findFraud(ArrayList<Transaction> transactions){
//        ArrayList<Transaction> posFraud = new ArrayList<>();
//
//        for (Transaction t : transactions){
//            if(t.getAmount() > 50000 || t.getAmount() % 100 == 0 || t.getMCC().contains("pawn") || t.getMCC().contains("casino")){
//                posFraud.add(t);
//            }
//
//
//        }
//
//        return  posFraud;
//    }

    private static ArrayList<Transaction> groupedFraud(ArrayList<Transaction> transactions){

        ArrayList<Transaction> posFraud = new ArrayList<>();

        Map<String, List<Transaction>> hmap = transactions.stream().collect(Collectors.groupingBy(w -> w.getCardholder()));

        for (String name: hmap.keySet()){

            /*the easy things to flag */
            for (Transaction t : hmap.get(name)){
                if(t.getAmount() > 50000){
                    posFraud.add(t);
                    t.setFraud(true);
                    t.setFraudReason("Individual transactions exceeding $50,000");
                }
                if(t.getAmount() % 100 == 0 ){
                    posFraud.add(t);
                    t.setFraud(true);
                    t.setFraudReason("Unusually round transaction");
                }
                if(t.getMCC().contains("pawn")|| t.getMCC().contains("casino")|| t.getMCC().contains("resort")){
                    posFraud.add(t);
                    t.setFraud(true);
                    t.setFraudReason("Transaction from pawn shop, casino or resort");
                }
            }

            /* grouping by dates*/
            List<Transaction> hmapVal = hmap.get(name);
            Map<Date, List<Transaction>> inhmap = hmapVal.stream().collect(Collectors.groupingBy(w -> w.getDate() ));
            for (Date day : inhmap.keySet()){
                List<Transaction> inhampVal = inhmap.get(day);
                ArrayList<Transaction> copy = new ArrayList<>(inhampVal);
                copy.removeIf(s -> s.getAmount() <= 20000);
                if (copy.size() > 2){
                    copy.forEach((item) -> item.setFraud(true));
                    copy.forEach((item) -> item.setFraudReason("Multiple large ($>20,000) transactions by a single user in a single day"));
                    posFraud.addAll(copy);
                }
            }
        }


        /* grouping by airline */
        transactions.removeIf(t -> (!t.getMCC().contains("airline")));

        Map<String, List<Transaction>> airlineMap = transactions.stream().collect(Collectors.groupingBy(w -> w.getMCC()));


        for (String airline : airlineMap.keySet()){
            if (airlineMap.get(airline).size() < 10){
                airlineMap.get(airline).forEach((item) -> item.setFraud(true));
                airlineMap.get(airline).forEach((item) -> item.setFraudReason("Infrequently used airlines (fewer than 10 occurrences"));
                posFraud.addAll(airlineMap.get(airline));
                System.out.println(airline);
            }
        }


        return posFraud;


    }


    public static void main(String[] args) {
        ArrayList<Transaction> fraudChecklist = new FormTransaction(args[0]).getTransactions();

        FraudDetector fraudDetector = new FraudDetector();
        ArrayList<Transaction> posFraud = fraudDetector.groupedFraud(fraudChecklist);

        for (Transaction t: posFraud){
            System.out.println(t + " " + "Reason for Suspicion: "+ t.getFraudReason());
        }

}





}
