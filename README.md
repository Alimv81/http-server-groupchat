## Group Chat using http.server

This project is a simple group chat application implemented using the `http.server` module in Python. By running the `server.py` file, the chat server will start and launch the chat interface in the Chrome browser by default.

## How to Run the Chat Server

To run the chat server, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:

   ```shell
   python server.py
   ```

4. The chat server will start running at `http://localhost:8080`.
5. The chat interface will automatically open in the Chrome browser.

## Features

The group chat application includes the following features:

- Sending and receiving chat messages in real-time.
- Serving static files for the chat interface.
- Storing chat messages in memory in runtime.
- Deleting chat messages in stored in the server file.

## Technologies Used

The project uses the following technologies:

- Python
- `http.server` module
- Chrome browser

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Deleting Chat Messages

To delete all chat messages stored on the server, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:

   ```shell
   curl -X DELETE http://localhost:8080/delete_messages
   ```

4. All chat messages will be deleted from the server.
