import java.util.ArrayList;
import java.util.Scanner;

public class ToDoList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> tasks = new ArrayList<>();

        while (true) {
            System.out.println("\n---- TO-DO LIST ----");
            System.out.println("1. Add Task");
            System.out.println("2. View Tasks");
            System.out.println("3. Remove Task");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();
            sc.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter a new task: ");
                    String task = sc.nextLine();
                    tasks.add(task);
                    System.out.println("✅ Task added!");
                    break;

                case 2:
                    System.out.println("\nYour Tasks:");
                    if (tasks.isEmpty()) {
                        System.out.println("No tasks available.");
                    } else {
                        for (int i = 0; i < tasks.size(); i++) {
                            System.out.println((i + 1) + ". " + tasks.get(i));
                        }
                    }
                    break;

                case 3:
                    System.out.print("Enter task number to remove: ");
                    int index = sc.nextInt();
                    if (index > 0 && index <= tasks.size()) {
                        tasks.remove(index - 1);
                        System.out.println("🗑️ Task removed!");
                    } else {
                        System.out.println("Invalid task number.");
                    }
                    break;

                case 4:
                    System.out.println("👋 Exiting To-Do List. Goodbye!");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice. Try again.");
            }
        }
    }
}
