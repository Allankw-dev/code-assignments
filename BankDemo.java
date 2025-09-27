class Bank {
    float getRateOfInterest() {
        return 0.0f; 
    }
}

class SBI extends Bank {
    float getRateOfInterest() {
        return 8.4f;
    }
}

class ICICI extends Bank {
    float getRateOfInterest() {
        return 7.3f;
    }
}

class AXIS extends Bank {
    float getRateOfInterest() {
        return 9.7f;
    }
}

public class BankDemo {
    public static void main(String[] args) {
        Bank ref; 

        ref = new SBI();
        System.out.println("SBI Rate of Interest: " + ref.getRateOfInterest());

        ref = new ICICI();
        System.out.println("ICICI Rate of Interest: " + ref.getRateOfInterest());

        ref = new AXIS();
        System.out.println("AXIS Rate of Interest: " + ref.getRateOfInterest());
    }
}