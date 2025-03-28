import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="EconomicsMS@2023",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Define the SQL query to create the view
create_view_query = """
CREATE OR REPLACE VIEW nfldb.teamseasonwithmetadata AS
SELECT * FROM (
    VALUES
    ('KAN', 'Kansas City Chiefs', 'AFC West', 'AFC', 2018, 12, 4, 565, 421, 6810),
    ('RAM', 'Los Angeles Rams', 'NFC West', 'NFC', 2018, 13, 3, 527, 384, 6738),
    ('NOR', 'New Orleans Saints', 'NFC South', 'NFC', 2018, 13, 3, 504, 353, 6067),
    ('NWE', 'New England Patriots', 'AFC East', 'AFC', 2018, 11, 5, 436, 325, 6295),
    ('CLT', 'Indianapolis Colts', 'AFC South', 'AFC', 2018, 10, 6, 433, 344, 6179),
    ('SEA', 'Seattle Seahawks', 'NFC West', 'NFC', 2018, 10, 6, 428, 347, 5653),
    ('SDG', 'Los Angeles Chargers', 'AFC West', 'AFC', 2018, 12, 4, 428, 329, 5962),
    ('PIT', 'Pittsburgh Steelers', 'AFC North', 'AFC', 2018, 9, 6, 428, 360, 6453),
    ('CHI', 'Chicago Bears', 'NFC North', 'NFC', 2018, 12, 4, 421, 283, 5502),
    ('ATL', 'Atlanta Falcons', 'NFC South', 'NFC', 2018, 7, 9, 414, 423, 6226),
    ('HTX', 'Houston Texans', 'AFC South', 'AFC', 2018, 11, 5, 402, 316, 5802),
    ('TAM', 'Tampa Bay Buccaneers', 'NFC South', 'NFC', 2018, 5, 11, 396, 464, 6648),
    ('RAV', 'Baltimore Ravens', 'AFC North', 'AFC', 2018, 10, 6, 389, 287, 5999),
    ('GNB', 'Green Bay Packers', 'NFC North', 'NFC', 2018, 6, 9, 376, 400, 5905),
    ('CAR', 'Carolina Panthers', 'NFC South', 'NFC', 2018, 7, 9, 376, 382, 5972),
    ('NYG', 'New York Giants', 'NFC East', 'NFC', 2018, 5, 11, 369, 412, 5697),
    ('CIN', 'Cincinnati Bengals', 'AFC North', 'AFC', 2018, 6, 10, 368, 455, 4972),
    ('PHI', 'Philadelphia Eagles', 'NFC East', 'NFC', 2018, 9, 7, 367, 348, 5845),
    ('MIN', 'Minnesota Vikings', 'NFC North', 'NFC', 2018, 8, 7, 360, 341, 5529),
    ('CLE', 'Cleveland Browns', 'AFC North', 'AFC', 2018, 7, 8, 359, 392, 5900),
    ('SFO', 'San Francisco 49ers', 'NFC West', 'NFC', 2018, 4, 12, 342, 435, 5769),
    ('DAL', 'Dallas Cowboys', 'NFC East', 'NFC', 2018, 10, 6, 339, 324, 5501),
    ('NYJ', 'New York Jets', 'AFC East', 'AFC', 2018, 4, 12, 333, 441, 4787),
    ('DEN', 'Denver Broncos', 'AFC West', 'AFC', 2018, 6, 10, 329, 349, 5602),
    ('DET', 'Detroit Lions', 'NFC North', 'NFC', 2018, 6, 10, 324, 360, 5236),
    ('MIA', 'Miami Dolphins', 'AFC East', 'AFC', 2018, 7, 9, 319, 433, 4638),
    ('OTI', 'Tennessee Titans', 'AFC South', 'AFC', 2018, 9, 7, 310, 303, 5002),
    ('RAI', 'Oakland Raiders', 'AFC West', 'AFC', 2018, 4, 12, 290, 467, 5379),
    ('WAS', 'Washington Redskins', 'NFC East', 'NFC', 2018, 7, 9, 281, 359, 4795),
    ('BUF', 'Buffalo Bills', 'AFC East', 'AFC', 2018, 6, 10, 269, 374, 4778),
    ('JAX', 'Jacksonville Jaguars', 'AFC South', 'AFC', 2018, 5, 11, 245, 316, 4832),
    ('CRD', 'Arizona Cardinals', 'NFC West', 'NFC', 2018, 3, 13, 225, 425, 3865),
    ('RAV', 'Baltimore Ravens', 'AFC North', 'AFC', 2019, 14, 2, 531, 282, 6521),
    ('SFO', 'San Francisco 49ers', 'NFC West', 'NFC', 2019, 13, 3, 479, 310, 6097),
    ('TAM', 'Tampa Bay Buccaneers', 'NFC South', 'NFC', 2019, 7, 9, 458, 449, 6366),
    ('NOR', 'New Orleans Saints', 'NFC South', 'NFC', 2019, 13, 3, 458, 341, 5982),
    ('KAN', 'Kansas City Chiefs', 'AFC West', 'AFC', 2019, 12, 4, 451, 308, 6067),
    ('MIN', 'Minnesota Vikings', 'NFC North', 'NFC', 2019, 10, 6, 443, 303, 5490),
    ('NWE', 'New England Patriots', 'AFC East', 'AFC', 2019, 12, 4, 420, 225, 5301),
    ('GNB', 'Green Bay Packers', 'NFC North', 'NFC', 2019, 13, 3, 376, 313, 5491),
    ('SEA', 'Seattle Seahawks', 'NFC West', 'NFC', 2019, 11, 5, 405, 398, 6080),
    ('BUF', 'Buffalo Bills', 'AFC East', 'AFC', 2019, 10, 6, 314, 259, 5281),
    ('TEN', 'Tennessee Titans', 'AFC South', 'AFC', 2019, 9, 7, 402, 331, 5419),
    ('PIT', 'Pittsburgh Steelers', 'AFC North', 'AFC', 2019, 8, 8, 289, 303, 4849),
    ('DAL', 'Dallas Cowboys', 'NFC East', 'NFC', 2019, 8, 8, 434, 321, 6901),
    ('PHI', 'Philadelphia Eagles', 'NFC East', 'NFC', 2019, 9, 7, 385, 354, 6322),
    ('LAR', 'Los Angeles Rams', 'NFC West', 'NFC', 2019, 9, 7, 394, 364, 5985),
    ('HOU', 'Houston Texans', 'AFC South', 'AFC', 2019, 10, 6, 378, 385, 5921),
    ('DEN', 'Denver Broncos', 'AFC West', 'AFC', 2019, 7, 9, 282, 316, 4798),
    ('IND', 'Indianapolis Colts', 'AFC South', 'AFC', 2019, 7, 9, 361, 373, 5378),
    ('CHI', 'Chicago Bears', 'NFC North', 'NFC', 2019, 8, 8, 280, 298, 4749),
    ('DET', 'Detroit Lions', 'NFC North', 'NFC', 2019, 3, 12, 341, 423, 5210),
    ('NYJ', 'New York Jets', 'AFC East', 'AFC', 2019, 7, 9, 276, 359, 4797),
    ('ATL', 'Atlanta Falcons', 'NFC South', 'NFC', 2019, 7, 9, 381, 399, 6115),
    ('CAR', 'Carolina Panthers', 'NFC South', 'NFC', 2019, 5, 11, 340, 470, 5888),
    ('CLE', 'Cleveland Browns', 'AFC North', 'AFC', 2019, 6, 10, 335, 393, 5755),
    ('ARI', 'Arizona Cardinals', 'NFC West', 'NFC', 2019, 5, 10, 361, 442, 5448),
    ('LAC', 'Los Angeles Chargers', 'AFC West', 'AFC', 2019, 5, 11, 337, 345, 5642),
    ('RAI', 'Las Vegas Raiders', 'AFC West', 'AFC', 2019, 7, 9, 313, 419, 5791),
    ('MIA', 'Miami Dolphins', 'AFC East', 'AFC', 2019, 5, 11, 306, 494, 4518),
    ('WAS', 'Washington Football Team', 'NFC East', 'NFC', 2019, 3, 13, 266, 435, 4863)
) AS s(team_id, team_name, division, conference, year, wins, losses, points_scored, points_allowed, total_yards)
"""

# Execute the SQL query to create the view
cur.execute(create_view_query)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
