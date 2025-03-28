import psycopg2

# Database connection parameters
dbname = "postgres"
user = "postgres"
password = "EconomicsMS@2023"
host = "localhost"
port = "5432"  

# Data to insert into the team table
team_data = [
    ("2TM", "Two Teams", None, None),
    ("3TM", "Three Teams", None, None),
    ("IDK", "ERROR TEAM", None, None),
    ("BAL", "Baltimore Ravens", "AFC North", "AFC"),
    ("RAV", "Baltimore Ravens", "AFC North", "AFC"),
    ("CIN", "Cincinnati Bengals", "AFC North", "AFC"),
    ("CLE", "Cleveland Browns", "AFC North", "AFC"),
    ("PIT", "Pittsburgh Steelers", "AFC North", "AFC"),
    ("BUF", "Buffalo Bills", "AFC East", "AFC"),
    ("MIA", "Miami Dolphins", "AFC East", "AFC"),
    ("NWE", "New England Patriots", "AFC East", "AFC"),
    ("NYJ", "New York Jets", "AFC East", "AFC"),
    ("HOU", "Houston Texans", "AFC South", "AFC"),
    ("HTX", "Houston Texans", "AFC South", "AFC"),
    ("IND", "Indianapolis Colts", "AFC South", "AFC"),
    ("CLT", "Indianapolis Colts", "AFC South", "AFC"),
    ("JAX", "Jacksonville Jaguars", "AFC South", "AFC"),
    ("OTI", "Tennessee Titans", "AFC South", "AFC"),
    ("TEN", "Tennesse Titans", "AFC South", "AFC"),
    ("DEN", "Denver Broncos", "AFC West", "AFC"),
    ("KAN", "Kansas City Chiefs", "AFC West", "AFC"),
    ("OAK", "Oakland Raiders", "AFC West", "AFC"),
    ("RAI", "Oakland Raiders", "AFC West", "AFC"),
    ("LAC", "Los Angeles Chargers", "AFC West", "AFC"),
    ("SDG", "Los Angeles Chargers", "AFC West", "AFC"),
    ("CHI", "Chicago Bears", "NFC North", "NFC"),
    ("DET", "Detroit Lions", "NFC North", "NFC"),
    ("GNB", "Green Bay Packers", "NFC North", "NFC"),
    ("MIN", "Minnesota Vikings", "NFC North", "NFC"),
    ("DAL", "Dallas Cowboys", "NFC East", "NFC"),
    ("NYG", "New York Giants", "NFC East", "NFC"),
    ("PHI", "Philadelphia Eagles", "NFC East", "NFC"),
    ("WAS", "Washington Redskins", "NFC East", "NFC"),
    ("ATL", "Atlanta Falcons", "NFC South", "NFC"),
    ("CAR", "Carolina Panthers", "NFC South", "NFC"),
    ("NOR", "New Orleans Saints", "NFC South", "NFC"),
    ("TAM", "Tampa Bay Buccaneers", "NFC South", "NFC"),
    ("ARI", "Arizona Cardinals", "NFC West", "NFC"),
    ("CRD", "Arizona Cardinals", "NFC West", "NFC"),
    ("STL", "St Louis Rams", "NFC West", "NFC"),
    ("LAR", "Los Angeles Rams", "NFC West", "NFC"),
    ("RAM", "Los Angeles Rams", "NFC West", "NFC"),
    ("SFO", "San Francisco 49ers", "NFC West", "NFC"),
    ("SEA", "Seattle Seahawks", "NFC West", "NFC")
]

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

# Create the team table
create_table_query = """
CREATE TABLE IF NOT EXISTS nfldb.team (
    teamabbr VARCHAR(5) PRIMARY KEY,
    name VARCHAR(100),
    division VARCHAR(50),
    conference VARCHAR(50)
)
"""
cursor.execute(create_table_query)
print("Team table created successfully!")

# Insert data into the team table
insert_query = "INSERT INTO nfldb.team (teamabbr, name, division, conference) VALUES (%s, %s, %s, %s)"
cursor.executemany(insert_query, team_data)
conn.commit()
print("Data inserted into team table successfully!")

# Close cursor and connection
cursor.close()
conn.close()
