import sqlite3

con = sqlite3.connect('youtube_videos_db')

cursor =con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS VIDEOS(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
) ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print (row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)",(name,time))
    con.commit()

def update_video(new_name,new_time,video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?",(video_id,))
    con.commit()


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. ADD videos")
        print("3. Update videos")
        print("4. Delete Videos")
        print("5. Exit app")
        choice= input("Enter your choice:")

        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice=='3':
            video_id=input("Enter video id to update: ")
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice=='4':
            video_id=input("Enter video id to delete: ")
            delete_video(name,time)
        elif choice=='5':
            break
        else:
            print("Invalid choice")

    con.close()


if __name__=="__main__":
    main()