<!--
import psycopg2

def sync_dim_tables_from_associate_team_map():
    # 🔧 Update your DB config here
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost",
        port="5432"
    )

    try:
        with conn.cursor() as cur:
            # Step 1: Get all associate-team pairs
            cur.execute("SELECT associate_name, team_name FROM associate_team_map")
            mappings = cur.fetchall()

            for associate_name, team_name in mappings:
                # Step 2: Insert associate if not exists
                cur.execute("""
                    INSERT INTO dim_catalog_associates (associate_name)
                    VALUES (%s)
                    ON CONFLICT (associate_name) DO NOTHING
                """, (associate_name,))

                # Step 3: Insert team if not exists
                cur.execute("""
                    INSERT INTO dim_teams (team_name)
                    VALUES (%s)
                    ON CONFLICT (team_name) DO NOTHING
                """, (team_name,))

        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"❌ Error syncing: {e}")
    finally:
        conn.close()


# Run the sync
sync_dim_tables_from_associate_team_map()

 -->