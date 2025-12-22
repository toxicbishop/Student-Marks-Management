import pymysql
import uuid
import sys


# --- CONFIGURATION ---
DB_CONFIG = {
    'host': 'oemr.in',
    'port': 9522,
    'user': 'school-admin',
    'password': 'School@2025',
    'database': 'school_db',
    'connect_timeout': 10,
    'cursorclass': pymysql.cursors.DictCursor
}
# ---------------------


def main():
    conn = None
    try:
        print(f"Connecting to {DB_CONFIG['host']} on port {DB_CONFIG['port']}...")
       
        # Connect using PyMySQL
        conn = pymysql.connect(**DB_CONFIG)
       
        print("SUCCESS: Connected to MySQL Server!")
        print("\n--- CUI STUDENT ENTRY SYSTEM ---")


        cursor = conn.cursor()


        # 1. Get Student Details
        # We flush the output buffer to ensure the prompt appears immediately
        print("Enter Student Name: ", end='', flush=True)
        std_name = sys.stdin.readline().strip()
       
        while True:
            try:
                print("Enter Roll no: ", end='', flush=True)
                line = sys.stdin.readline().strip()
                if not line: continue
                std_roll_no = int(line)
                break
            except ValueError:
                print("Roll No must be a number.")


        # Insert Student
        try:
            cursor.execute("INSERT INTO STUDENTS (ROLL_NO, NAME) VALUES (%s, %s)",
                           (std_roll_no, std_name))
        except pymysql.err.IntegrityError as e:
            # Check for Duplicate Entry (Error code 1062)
            if e.args[0] == 1062:
                print(f"-> Student ID {std_roll_no} found. Proceeding to add marks.")
            else:
                print(f"Error inserting student: {e}")
                return


        print(f"\nEnter marks for {std_name}:")


        # 2. Subject Mapping
        subjects = [
            ("Science", 101),
            ("Social", 102),
            ("Maths", 103),
            ("Eng", 104),
            ("Hindi", 105),
            ("Kannada", 106)
        ]


        # 3. Loop Inputs and Save
        for sub_name, sub_id in subjects:
            while True:
                try:
                    print(f"{sub_name}: ", end='', flush=True)
                    val = int(sys.stdin.readline().strip())
                    break
                except ValueError:
                    print("Please enter a valid number.")


            # Generate UUID
            unique_id = str(uuid.uuid4())


            sql_query = """
                INSERT INTO MARKS (ID, ROLL_NO, SUBJ_ID, MARKS)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql_query, (unique_id, std_roll_no, sub_id, val))


        conn.commit()
        print("\n[SUCCESS] Data successfully uploaded to MySQL Server.")


    except pymysql.MySQLError as e:
        print(f"\n[ERROR] Database Error: {e}")
    except Exception as e:
        print(f"\n[ERROR] System Error: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()

