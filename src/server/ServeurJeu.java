package server;
import java.io.*;
import java.net.*;
import java.util.*;

public class ServeurJeu {
    private ServerSocket serverSocket;
    private List<ClientHandler> clients = new ArrayList<>();

    public ServeurJeu(int port) throws IOException {
        serverSocket = new ServerSocket(port);
        System.out.println("Serveur démarré sur le port " + port);
    }

    public void start() throws IOException {
        while (true) {
            Socket clientSocket = serverSocket.accept();
            System.out.println("Nouveau joueur connecté !");
            ClientHandler clientHandler = new ClientHandler(clientSocket, this);
            clients.add(clientHandler);
            new Thread(clientHandler).start();
        }
    }

    // Diffuser un message à tous les joueurs
    public void broadcast(String message) {
        for (ClientHandler client : clients) {
            client.sendMessage(message);
        }
    }

    public static void main(String[] args) throws IOException {
        ServeurJeu serveur = new ServeurJeu(1234);
        serveur.start();
    }
}

class ClientHandler implements Runnable {
    private Socket socket;
    private ServeurJeu serveur;
    private PrintWriter out;
    private BufferedReader in;

    public ClientHandler(Socket socket, ServeurJeu serveur) throws IOException {
        this.socket = socket;
        this.serveur = serveur;
        this.out = new PrintWriter(socket.getOutputStream(), true);
        this.in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
    }

    @Override
    public void run() {
        try {
            String input;
            while ((input = in.readLine()) != null) {
                System.out.println("Message reçu : " + input);
                serveur.broadcast(input); // renvoie le message à tous
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void sendMessage(String message) {
        out.println(message);
    }
}
