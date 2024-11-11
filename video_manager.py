import sqlite3
conn = sqlite3.connect("videos.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videolist(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_all_videos():
    print('\n')
    print("*"*60)

    cursor.execute("SELECT * FROM videolist")
    video = cursor.fetchall()
    if not video:
        print("No any video saved yet")
    else:
        for row in video:
            print(f'Name: {row[1]}, Duration: {row[2]}')          

    print("*"*60, '\n')


def add_videos(name, time):
    cursor.execute("INSERT INTO videolist (name, time) VALUES (?, ?)",(name,time))
    conn.commit()


def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videolist SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    conn.commit()


def delete_videos(video_id):
    cursor.execute("DELETE FROM videolist WHERE id = ?",(video_id,))
    conn.commit()

def main():
    while True:
        print("Youtube Video Manager")
        print("1. List all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app.")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video duration: ")
            add_videos(name, time)
        elif choice == '3':
            index = input("Enter video ID to update: ")
            name = input("Enter video name: ")
            time = input("Enter video duration: ")
            update_videos(index,name,time)
        elif choice == '4':
            index = input("enter video ID to delete: ")
            delete_videos(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice")
            
    conn.close()


if __name__ == "__main__":
    main()