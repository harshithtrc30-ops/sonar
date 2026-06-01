import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

public class InsecureApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Hardcoded credentials (Security Issue)
        String url = "jdbc:mysql://localhost:3306/testdb";
        String user = "root";
        String password = "root123"; // Hardcoded password

        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            Statement stmt = conn.createStatement();

            System.out.println("Enter username to search:");
            String input = sc.nextLine();

            // SQL Injection vulnerability (Security Issue)
            String query = "SELECT * FROM users WHERE username = '" + input + "'";
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("User: " + rs.getString("username"));
            }

            // Resource leak: Scanner and Connection not closed properly (Maintainability Issue)
        } catch (Exception e) {
            // Catching generic Exception (Maintainability Issue)
            System.out.println("Error occurred: " + e.getMessage());
        }
    }
}
