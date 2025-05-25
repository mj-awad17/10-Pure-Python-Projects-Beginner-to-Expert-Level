import time
from collections import defaultdict
from queue import Queue
import threading
import random

class User:
    def __init__(self, username):
        self.username = username
        self.inbox = Queue()
        self.online = True
        self.last_seen = time.time()

class ChatServer:
    def __init__(self):
        self.users = {}
        self.chat_rooms = defaultdict(list)
        self.message_history = defaultdict(list)
        
    def register_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            return True
        return False
    
    def send_message(self, from_user, to_user, message):
        if to_user in self.users:
            timestamp = time.time()
            formatted_msg = f"[{time.strftime('%H:%M:%S')}] {from_user}: {message}"
            self.users[to_user].inbox.put(formatted_msg)
            self.message_history[to_user].append(formatted_msg)
            return True
        return False
    
    def broadcast_message(self, from_user, room_name, message):
        if room_name in self.chat_rooms:
            timestamp = time.time()
            formatted_msg = f"[{time.strftime('%H:%M:%S')}] {from_user} (Room: {room_name}): {message}"
            for user in self.chat_rooms[room_name]:
                if user != from_user:
                    self.users[user].inbox.put(formatted_msg)
            return True
        return False
    
    def join_room(self, username, room_name):
        if username in self.users:
            self.chat_rooms[room_name].append(username)
            return True
        return False
    
    def leave_room(self, username, room_name):
        if room_name in self.chat_rooms and username in self.chat_rooms[room_name]:
            self.chat_rooms[room_name].remove(username)
            return True
        return False

def simulate_user_activity(server, username, target_users, rooms):
    user = server.users[username]
    while user.online:
        # Simulate receiving messages
        while not user.inbox.empty():
            message = user.inbox.get()
            print(f"[{username} received] {message}")
        
        # Simulate sending messages
        if random.random() < 0.3:  # 30% chance to send a message
            if random.random() < 0.5:  # 50% chance for direct message vs room message
                target = random.choice(target_users)
                message = f"Hello {target}! This is a direct message."
                server.send_message(username, target, message)
            else:
                room = random.choice(rooms)
                message = f"Hello everyone in {room}!"
                server.broadcast_message(username, room, message)
        
        time.sleep(random.uniform(1, 3))

def main():
    # Initialize chat server
    server = ChatServer()
    
    # Register some users
    usernames = ["Alice", "Bob", "Charlie", "David"]
    rooms = ["General", "Random", "Tech"]
    
    for username in usernames:
        server.register_user(username)
        for room in rooms:
            server.join_room(username, room)
    
    # Create and start user simulation threads
    threads = []
    for username in usernames:
        other_users = [u for u in usernames if u != username]
        thread = threading.Thread(
            target=simulate_user_activity,
            args=(server, username, other_users, rooms)
        )
        thread.daemon = True
        threads.append(thread)
        thread.start()
    
    # Let the simulation run for a while
    try:
        print("Chat simulation started. Press Ctrl+C to stop...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down chat simulation...")
        for username in usernames:
            server.users[username].online = False
        
        for thread in threads:
            thread.join()
        
        print("Chat simulation ended.")

if __name__ == "__main__":
    main()