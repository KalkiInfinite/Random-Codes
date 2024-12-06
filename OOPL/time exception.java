class TimeException extends Exception {
    public TimeException(String message) {
        super(message);
    }

    public String toString() {
        return getMessage();
    }
}

public class Exp6 {
    public static void main(String[] args) {
        try {
            int minutes1 = Integer.parseInt(args[0]);
            int seconds1 = Integer.parseInt(args[1]);
            int minutes2 = Integer.parseInt(args[2]);
            int seconds2 = Integer.parseInt(args[3]);

            int totalMinutes = minutes1 + minutes2;
            int totalSeconds = seconds1 + seconds2;

            if (totalSeconds >= 60) {
                totalMinutes += totalSeconds / 60;
                totalSeconds %= 60;
            }

            if (totalMinutes >= 60) {
                throw new TimeException("Invalid format: (time value exceeds 60 minutes)");
            }

            System.out.println("The total time is : " + totalMinutes + " minutes and " + totalSeconds + " seconds");
        } catch (TimeException e) {
            System.out.println(e);
        }
    }
}
