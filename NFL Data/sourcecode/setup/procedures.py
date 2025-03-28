import psycopg2

# Database connection parameters
db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Econometrics@2023",
    "host": "localhost",
    "port": "5432"
}

# Stored procedure definitions
stored_procedures = [
    """
    CREATE OR REPLACE PROCEDURE nfldb.calculate_average_score(
        team_id_param VARCHAR(3),
        season_param INTEGER,
        OUT average_score DECIMAL(10,2)
    )
    LANGUAGE SQL
    AS $$
    BEGIN
        SELECT AVG(points_for::Decimal)
        INTO average_score
        FROM nfldb.teamseasonwithmetadata
        WHERE teamabbr = team_id_param AND year = season_param;
    END;
    $$;
    """,
    """
    CREATE OR REPLACE PROCEDURE nfldb.get_team_performance(
        team_id_param VARCHAR(3),
        season_param INTEGER
    )
    LANGUAGE SQL
    AS $$
    BEGIN
        SELECT *
        FROM nfldb.teamseasonwithmetadata
        WHERE teamabbr = team_id_param AND year = season_param;
    END;
    $$;
    """,
    """
    CREATE OR REPLACE PROCEDURE nfldb.update_team_information(
        team_id_param VARCHAR(3),
        season_param INTEGER,
        wins_param INTEGER,
        losses_param INTEGER,
        points_scored_param INTEGER,
        points_allowed_param INTEGER,
        total_yards_param INTEGER
    )
    LANGUAGE SQL
    AS $$
    BEGIN
        UPDATE nfldb.teamseasonwithmetadata
        SET
            wins = wins_param,
            losses = losses_param,
            points_scored = points_scored_param::VARCHAR,
            points_allowed = points_allowed_param::VARCHAR,
            total_yards = total_yards_param::VARCHAR
        WHERE team_id = team_id_param AND year = season_param;
    END;
    $$;
    """
]

def create_stored_procedures(connection):
    with connection.cursor() as cursor:
        for procedure in stored_procedures:
            cursor.execute(procedure)
        connection.commit()
        print("Stored procedures created successfully.")

def main():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_params)
        print("Connected to the database.")

        # Create stored procedures
        create_stored_procedures(connection)
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if connection:
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
