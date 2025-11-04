import java.time.LocalDate;
import java.time.YearMonth;
import java.time.DayOfWeek;
import java.time.format.DateTimeFormatter;

public class CalendarGenerator {

    public static void main(String[] args) {
        LocalDate today = LocalDate.now();
        int year = today.getYear();
        int month = today.getMonthValue();

        System.out.println("Displaying calendar for the current month:");
        printCalendar(year, month);
    }

    public static void printCalendar(int year, int month) {
        
        LocalDate date = LocalDate.of(year, month, 1);

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMMM yyyy");
        System.out.println("\n   " + date.format(formatter));
        System.out.println("Mo Tu We Th Fr Sa Su");

        DayOfWeek startDay = date.getDayOfWeek();
        int padding = startDay.getValue() - 1; 

        for (int i = 0; i < padding; i++) {
            System.out.print("   "); 
        }

        while (date.getMonthValue() == month) {
            
            System.out.printf("%2d ", date.getDayOfMonth());

            if (date.getDayOfWeek() == DayOfWeek.SUNDAY) {
                System.out.println();
            }

            date = date.plusDays(1);
        }

        if (date.getDayOfWeek() != DayOfWeek.MONDAY) {
             System.out.println();
        }
    }
}