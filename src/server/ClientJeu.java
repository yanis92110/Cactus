package server;
import java.io.*;
import java.net.*;

public class ClientJeu {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 8080);
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        BufferedReader console = new BufferedReader(new InputStreamReader(System.in));

        // Thread pour écouter le serveur
        new Thread(() -> {
            try {
                String msg;
                while ((msg = in.readLine()) != null) {
                    System.out.println("Serveur : " + msg);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }).start();

        // Envoyer les messages tapés au serveur
        String userInput;
        while ((userInput = console.readLine()) != null) {
            out.println(userInput);
        }
    }
}
