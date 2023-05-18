import sqlite3

def database():
    # Connect to the SQLite database
    conn = sqlite3.connect('prayer_time.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prayer_times (
            date TEXT PRIMARY KEY,
            sahr_end TEXT,
            fajr TEXT,
            sunrise TEXT,
            luhr TEXT,
            asr TEXT,
            maghrib TEXT,
            isha TEXT
        )
    ''')

    # Prepare the data (366 rows)
    data_rows = [
        ("01-01", "04:45", "05:00", "06:22", "12:15", "15:36", "18:06", "19:21"),
    ("02-01", "04:46", "05:01", "06:23", "12:16", "15:37", "18:07", "19:22"),
    ("03-01", "04:46", "05:01", "06:23", "12:16", "15:37", "18:07", "19:22"),
    ("04-01", "04:47", "05:02", "06:24", "12:17", "15:38", "18:08", "19:23"),
    ("05-01", "04:47", "05:02", "06:24", "12:17", "15:38", "18:08", "19:23"),
    ("06-01", "04:47", "05:02", "06:24", "12:17", "15:38", "18:08", "19:23"),
    ("07-01", "04:48", "05:03", "06:25", "12:18", "15:39", "18:09", "19:24"),
    ("08-01", "04:48", "05:03", "06:25", "12:18", "15:39", "18:09", "19:24"),
    ("09-01", "04:49", "05:04", "06:25", "12:19", "15:40", "18:10", "19:25"),
    ("10-01", "04:49", "05:04", "06:25", "12:19", "15:40", "18:10", "19:25"),
    ("11-01", "04:50", "05:05", "06:26", "12:20", "15:41", "18:11", "19:26"),
    ("12-01", "04:50", "05:05", "06:26", "12:20", "15:41", "18:11", "19:26"),
    ("13-01", "04:51", "05:06", "06:27", "12:20", "15:42", "18:12", "19:27"),
    ("14-01", "04:51", "05:06", "06:27", "12:21", "15:43", "18:13", "19:27"),
    ("15-01", "04:51", "05:06", "06:27", "12:21", "15:43", "18:13", "19:27"),
    ("16-01", "04:52", "05:07", "06:28", "12:22", "15:44", "18:14", "19:28"),
    ("17-01", "04:52", "05:07", "06:28", "12:22", "15:44", "18:14", "19:28"),
    ("18-01", "04:53", "05:08", "06:28", "12:22", "15:44", "18:15", "19:29"),
    ("19-01", "04:53", "05:08", "06:28", "12:22", "15:44", "18:15", "19:29"),
    ("20-01", "04:53", "05:08", "06:28", "12:22", "15:44", "18:15", "19:29"),
    ("21-01", "04:54", "05:09", "06:29", "12:23", "15:45", "18:16", "19:30"),
    ("22-01", "04:54", "05:09", "06:29", "12:23", "15:46", "18:17", "19:30"),
    ("23-01", "04:54", "05:09", "06:29", "12:23", "15:46", "18:17", "19:30"),
    ("24-01", "04:54", "05:09", "06:29", "12:23", "15:46", "18:17", "19:30"),
    ("25-01", "04:54", "05:09", "06:29", "12:23", "15:46", "18:17", "19:30"),
    ("26-01", "04:55", "05:10", "06:30", "12:24", "15:47", "18:18", "19:31"),
    ("27-01", "04:55", "05:10", "06:30", "12:24", "15:47", "18:18", "19:31"),
    ("28-01", "04:55", "05:10", "06:30", "12:24", "15:47", "18:18", "19:31"),
    ("29-01", "04:55", "05:10", "06:30", "12:24", "15:47", "18:18", "19:31"),
    ("30-01", "04:56", "05:11", "06:30", "12:25", "15:47", "18:19", "19:32"),
    ("31-01", "04:56", "05:11", "06:30", "12:25", "15:47", "18:19", "19:32"),
    ("01-02", "04:56", "05:11", "06:30", "12:26", "15:48", "18:20", "19:32"),
    ("02-02", "04:56", "05:11", "06:30", "12:26", "15:48", "18:20", "19:32"),
    ("03-02", "04:56", "05:11", "06:30", "12:26", "15:48", "18:20", "19:32"),
    ("04-02", "04:56", "05:11", "06:30", "12:26", "15:48", "18:20", "19:32"),
    ("05-02", "04:56", "05:11", "06:30", "12:26", "15:48", "18:20", "19:32"),
    ("06-02", "04:56", "05:11", "06:30", "12:26", "15:48", "18:20", "19:32"),
    ("07-02", "04:56", "05:11", "06:29", "12:26", "15:48", "18:21", "19:33"),
    ("08-02", "04:56", "05:11", "06:29", "12:26", "15:48", "18:21", "19:33"),
    ("09-02", "04:56", "05:11", "06:29", "12:26", "15:48", "18:21", "19:33"),
    ("10-02", "04:56", "05:11", "06:29", "12:26", "15:48", "18:21", "19:33"),
    ("11-02", "04:56", "05:11", "06:29", "12:26", "15:48", "18:21", "19:33"),
    ("12-02", "04:56", "05:11", "06:29", "12:26", "15:48", "18:21", "19:33"),
    ("13-02", "04:56", "05:11", "06:28", "12:26", "15:47", "18:22", "19:33"),
    ("14-02", "04:56", "05:11", "06:28", "12:26", "15:47", "18:22", "19:33"),
    ("15-02", "04:56", "05:11", "06:28", "12:26", "15:47", "18:22", "19:33"),
    ("16-02", "04:56", "05:11", "06:28", "12:26", "15:47", "18:22", "19:33"),
    ("17-02", "04:56", "05:11", "06:28", "12:26", "15:47", "18:22", "19:33"),
    ("18-02", "04:56", "05:11", "06:27", "12:26", "15:47", "18:22", "19:33"),
    ("19-02", "04:56", "05:11", "06:27", "12:26", "15:47", "18:22", "19:33"),
    ("20-02", "04:56", "05:11", "06:27", "12:26", "15:47", "18:22", "19:33"),
    ("21-02", "04:56", "05:11", "06:27", "12:26", "15:47", "18:22", "19:33"),
    ("22-02", "04:56", "05:11", "06:27", "12:26", "15:47", "18:22", "19:33"),
    ("23-02", "04:56", "05:11", "06:27", "12:26", "15:47", "18:22", "19:33"),
    ("24-02", "04:56", "05:11", "06:27", "12:26", "15:47", "18:22", "19:33"),
    ("25-02", "04:54", "05:09", "06:25", "12:25", "15:45", "18:23", "19:33"),
    ("26-02", "04:54", "05:09", "06:25", "12:25", "15:45", "18:23", "19:33"),
    ("27-02", "04:54", "05:09", "06:25", "12:25", "15:45", "18:23", "19:33"),
    ("28-02", "04:54", "05:09", "06:25", "12:25", "15:45", "18:23", "19:33"),
    ("29-02", "04:54", "05:09", "06:25", "12:25", "15:45", "18:23", "19:33"),
    ("01-03", "04:53", "05:08", "06:24", "12:24", "15:42", "18:22", "19:32"),
    ("02-03", "04:53", "05:08", "06:24", "12:24", "15:42", "18:22", "19:32"),
    ("03-03", "04:53", "05:08", "06:24", "12:24", "15:42", "18:22", "19:32"),
    ("04-03", "04:53", "05:08", "06:24", "12:24", "15:42", "18:22", "19:32"),
    ("05-03", "04:51", "05:06", "06:22", "12:23", "15:41", "18:22", "19:32"),
    ("06-03", "04:51", "05:06", "06:22", "12:23", "15:41", "18:22", "19:32"),
    ("07-03", "04:51", "05:06", "06:22", "12:23", "15:41", "18:22", "19:32"),
    ("08-03", "04:51", "05:06", "06:22", "12:23", "15:41", "18:22", "19:32"),
    ("09-03", "04:51", "05:06", "06:22", "12:23", "15:41", "18:22", "19:32"),
    ("10-03", "04:49", "05:04", "06:20", "12:22", "15:38", "18:22", "19:32"),
    ("11-03", "04:49", "05:04", "06:20", "12:22", "15:38", "18:22", "19:32"),
    ("12-03", "04:49", "05:04", "06:20", "12:22", "15:38", "18:22", "19:32"),
    ("13-03", "04:49", "05:04", "06:20", "12:22", "15:38", "18:22", "19:32"),
    ("14-03", "04:48", "05:03", "06:18", "12:21", "15:35", "18:22", "19:31"),
    ("15-03", "04:48", "05:03", "06:18", "12:21", "15:35", "18:22", "19:31"),
    ("16-03", "04:48", "05:03", "06:18", "12:21", "15:35", "18:22", "19:31"),
    ("17-03", "04:48", "05:03", "06:18", "12:21", "15:35", "18:22", "19:31"),
    ("18-03", "04:48", "05:03", "06:18", "12:21", "15:35", "18:22", "19:31"),
    ("19-03", "04:46", "05:01", "06:16", "12:20", "15:33", "18:22", "19:31"),
    ("20-03", "04:46", "05:01", "06:16", "12:20", "15:33", "18:22", "19:31"),
    ("21-03", "04:44", "04:59", "06:14", "12:19", "15:31", "18:21", "19:31"),
    ("22-03", "04:44", "04:59", "06:14", "12:19", "15:31", "18:21", "19:31"),
    ("23-03", "04:44", "04:59", "06:14", "12:19", "15:31", "18:21", "19:31"),
    ("24-03", "04:44", "04:59", "06:14", "12:19", "15:31", "18:21", "19:31"),
    ("25-03", "04:42", "04:57", "06:13", "12:18", "15:28", "18:21", "19:31"),
    ("26-03", "04:42", "04:57", "06:13", "12:18", "15:28", "18:21", "19:31"),
    ("27-03", "04:42", "04:57", "06:13", "12:18", "15:28", "18:21", "19:31"),
    ("28-03", "04:41", "04:56", "06:11", "12:17", "15:25", "18:20", "19:30"),
    ("29-03", "04:41", "04:56", "06:11", "12:17", "15:25", "18:20", "19:30"),
    ("30-03", "04:41", "04:56", "06:11", "12:17", "15:25", "18:20", "19:30"),
    ("31-03", "04:39", "04:54", "06:10", "12:16", "15:22", "18:20", "19:30"),
    ("01-04", "04:39", "04:54", "06:10", "12:16", "15:22", "18:20", "19:30"),
    ("02-04", "04:39", "04:54", "06:10", "12:16", "15:22", "18:20", "19:30"),
    ("03-04", "04:37", "04:52", "06:08", "12:15", "15:19", "18:20", "19:30"),
    ("04-04", "04:37", "04:52", "06:08", "12:15", "15:19", "18:20", "19:30"),
    ("05-04", "04:37", "04:52", "06:08", "12:15", "15:19", "18:20", "19:30"),
    ("06-04", "04:35", "04:50", "06:07", "12:14", "15:16", "18:19", "19:30"),
    ("07-04", "04:35", "04:50", "06:07", "12:14", "15:16", "18:19", "19:30"),
    ("08-04", "04:35", "04:50", "06:07", "12:14", "15:16", "18:19", "19:30"),
    ("09-04", "04:35", "04:50", "06:07", "12:14", "15:16", "18:19", "19:30"),
    ("10-04", "04:35", "04:50", "06:07", "12:14", "15:16", "18:19", "19:30"),
    ("11-04", "04:35", "04:50", "06:07", "12:14", "15:16", "18:19", "19:30"),
    ("12-04", "04:33", "04:48", "06:05", "12:13", "15:17", "18:19", "19:30"),
    ("13-04", "04:33", "04:48", "06:05", "12:13", "15:17", "18:19", "19:30"),
    ("14-04", "04:33", "04:48", "06:05", "12:13", "15:17", "18:19", "19:30"),
    ("15-04", "04:31", "04:46", "06:03", "12:12", "15:19", "18:19", "19:30"),
    ("16-04", "04:31", "04:46", "06:03", "12:12", "15:19", "18:19", "19:30"),
    ("17-04", "04:31", "04:46", "06:03", "12:12", "15:19", "18:19", "19:30"),
    ("18-04", "04:31", "04:46", "06:03", "12:12", "15:19", "18:19", "19:30"),
    ("19-04", "04:29", "04:44", "06:01", "12:11", "15:21", "18:19", "19:30"),
    ("20-04", "04:29", "04:44", "06:01", "12:11", "15:21", "18:19", "19:30"),
    ("21-04", "04:29", "04:44", "06:01", "12:11", "15:21", "18:19", "19:30"),
    ("22-04", "04:29", "04:44", "06:01", "12:11", "15:21", "18:19", "19:30"),
    ("23-04", "04:29", "04:44", "06:01", "12:11", "15:21", "18:19", "19:30"),
    ("24-04", "04:29", "04:44", "06:01", "12:11", "15:21", "18:19", "19:30"),
    ("25-04", "04:26", "04:41", "05:59", "12:10", "15:23", "18:19", "19:30"),
    ("26-04", "04:26", "04:41", "05:59", "12:10", "15:23", "18:19", "19:30"),
    ("27-04", "04:26", "04:41", "05:59", "12:10", "15:23", "18:19", "19:30"),
    ("28-04", "04:26", "04:41", "05:59", "12:10", "15:23", "18:19", "19:30"),
    ("29-04", "04:26", "04:41", "05:59", "12:10", "15:23", "18:19", "19:30"),
    ("30-04", "04:24", "04:39", "05:57", "12:09", "15:25", "18:19", "19:31"),
    ("01-05", "04:24", "04:39", "05:57", "12:09", "15:25", "18:19", "19:31"),
    ("02-05", "04:24", "04:39", "05:57", "12:09", "15:25", "18:19", "19:31"),
    ("03-05", "04:24", "04:39", "05:57", "12:09", "15:25", "18:19", "19:31"),
    ("04-05", "04:22", "04:37", "05:57", "12:09", "15:27", "18:19", "19:32"),
    ("05-05", "04:22", "04:37", "05:57", "12:09", "15:27", "18:19", "19:32"),
    ("06-05", "04:22", "04:37", "05:57", "12:09", "15:27", "18:19", "19:32"),
    ("07-05", "04:22", "04:37", "05:57", "12:09", "15:27", "18:19", "19:32"),
    ("08-05", "04:22", "04:37", "05:57", "12:09", "15:27", "18:19", "19:32"),
    ("09-05", "04:20", "04:35", "05:55", "12:08", "15:28", "18:20", "19:33"),
    ("10-05", "04:20", "04:35", "05:55", "12:08", "15:28", "18:20", "19:33"),
    ("11-05", "04:20", "04:35", "05:55", "12:08", "15:28", "18:20", "19:33"),
    ("12-05", "04:20", "04:35", "05:55", "12:08", "15:28", "18:20", "19:33"),
    ("13-05", "04:20", "04:35", "05:55", "12:08", "15:28", "18:20", "19:33"),
    ("14-05", "04:20", "04:35", "05:55", "12:08", "15:28", "18:20", "19:33"),
    ("15-05", "04:19", "04:34", "05:54", "12:08", "15:30", "18:20", "19:34"),
    ("16-05", "04:19", "04:34", "05:54", "12:08", "15:30", "18:20", "19:34"),
    ("17-05", "04:19", "04:34", "05:54", "12:08", "15:30", "18:20", "19:34"),
    ("18-05", "04:19", "04:34", "05:54", "12:08", "15:30", "18:20", "19:34"),
    ("19-05", "04:19", "04:34", "05:54", "12:08", "15:30", "18:20", "19:34"),
    ("20-05", "04:18", "04:33", "05:54", "12:08", "15:32", "18:21", "19:36"),
    ("21-05", "04:18", "04:33", "05:54", "12:08", "15:32", "18:21", "19:36"),
    ("22-05", "04:18", "04:33", "05:54", "12:08", "15:32", "18:21", "19:36"),
    ("23-05", "04:18", "04:33", "05:54", "12:08", "15:32", "18:21", "19:36"),
    ("24-05", "04:18", "04:33", "05:54", "12:08", "15:32", "18:21", "19:36"),
    ("25-05", "04:18", "04:33", "05:54", "12:08", "15:32", "18:21", "19:36"),
    ("26-05", "04:17", "04:32", "05:53", "12:09", "15:34", "18:22", "19:38"),
    ("27-05", "04:17", "04:32", "05:53", "12:09", "15:34", "18:22", "19:38"),
    ("28-05", "04:17", "04:32", "05:53", "12:09", "15:34", "18:22", "19:38"),
    ("29-05", "04:16", "04:31", "05:54", "12:09", "15:35", "18:23", "19:39"),
    ("30-05", "04:16", "04:31", "05:54", "12:09", "15:35", "18:23", "19:39"),
    ("31-05", "04:16", "04:31", "05:54", "12:09", "15:35", "18:23", "19:39"),
    ("01-06", "04:17", "04:32", "05:54", "12:10", "15:36", "18:24", "19:40"),
    ("02-06", "04:17", "04:32", "05:54", "12:10", "15:36", "18:24", "19:40"),
    ("03-06", "04:17", "04:32", "05:54", "12:10", "15:36", "18:24", "19:40"),
    ("04-06", "04:17", "04:32", "05:54", "12:10", "15:36", "18:24", "19:40"),
    ("05-06", "04:17", "04:32", "05:54", "12:10", "15:36", "18:24", "19:40"),
    ("06-06", "04:17", "04:32", "05:54", "12:10", "15:36", "18:24", "19:40"),
    ("07-06", "04:16", "04:31", "05:54", "12:11", "15:38", "18:25", "19:42"),
    ("08-06", "04:16", "04:31", "05:54", "12:11", "15:38", "18:25", "19:42"),
    ("09-06", "04:16", "04:31", "05:54", "12:11", "15:38", "18:25", "19:42"),
    ("10-06", "04:16", "04:31", "05:54", "12:11", "15:38", "18:25", "19:42"),
    ("11-06", "04:16", "04:31", "05:55", "12:11", "15:39", "18:26", "19:43"),
    ("12-06", "04:16", "04:31", "05:55", "12:11", "15:39", "18:26", "19:43"),
    ("13-06", "04:16", "04:31", "05:55", "12:11", "15:39", "18:26", "19:43"),
    ("14-06", "04:16", "04:31", "05:55", "12:11", "15:39", "18:26", "19:43"),
    ("15-06", "04:17", "04:32", "05:55", "12:12", "15:39", "18:27", "19:44"),
    ("16-06", "04:17", "04:32", "05:55", "12:12", "15:39", "18:27", "19:44"),
    ("17-06", "04:17", "04:32", "05:55", "12:12", "15:39", "18:27", "19:44"),
    ("18-06", "04:17", "04:32", "05:56", "12:13", "15:40", "18:28", "19:44"),
    ("19-06", "04:17", "04:32", "05:56", "12:13", "15:40", "18:28", "19:44"),
    ("20-06", "04:17", "04:32", "05:56", "12:13", "15:40", "18:28", "19:44"),
    ("21-06", "04:18", "04:33", "05:57", "12:14", "15:41", "18:29", "19:45"),
    ("22-06", "04:18", "04:33", "05:57", "12:14", "15:41", "18:29", "19:45"),
    ("23-06", "04:18", "04:33", "05:57", "12:14", "15:41", "18:29", "19:45"),
    ("24-06", "04:18", "04:33", "05:57", "12:14", "15:41", "18:29", "19:45"),
    ("25-06", "04:18", "04:33", "05:57", "12:14", "15:41", "18:29", "19:45"),
    ("26-06", "04:19", "04:34", "05:58", "12:15", "15:42", "18:30", "19:47"),
    ("27-06", "04:19", "04:34", "05:58", "12:15", "15:42", "18:30", "19:47"),
    ("28-06", "04:19", "04:34", "05:58", "12:15", "15:42", "18:30", "19:47"),
    ("29-06", "04:19", "04:34", "05:58", "12:15", "15:42", "18:30", "19:47"),
    ("30-06", "04:19", "04:34", "05:58", "12:15", "15:42", "18:30", "19:47"),
    ("01-07", "04:20", "04:35", "05:59", "12:16", "15:43", "18:31", "19:47"),
    ("02-07", "04:20", "04:35", "05:59", "12:16", "15:43", "18:31", "19:47"),
    ("03-07", "04:20", "04:35", "05:59", "12:16", "15:43", "18:31", "19:47"),
    ("04-07", "04:20", "04:35", "05:59", "12:16", "15:43", "18:31", "19:47"),
    ("05-07", "04:20", "04:35", "05:59", "12:16", "15:43", "18:31", "19:47"),
    ("06-07", "04:20", "04:35", "05:59", "12:16", "15:43", "18:31", "19:47"),
    ("07-07", "04:22", "04:37", "06:00", "12:17", "15:44", "18:32", "19:48"),
    ("08-07", "04:22", "04:37", "06:00", "12:17", "15:44", "18:32", "19:48"),
    ("09-07", "04:22", "04:37", "06:00", "12:17", "15:44", "18:32", "19:48"),
    ("10-07", "04:22", "04:37", "06:00", "12:17", "15:44", "18:32", "19:48"),
    ("11-07", "04:24", "04:39", "06:01", "12:17", "15:43", "18:32", "19:48"),
    ("12-07", "04:24", "04:39", "06:01", "12:17", "15:43", "18:32", "19:48"),
    ("13-07", "04:24", "04:39", "06:01", "12:17", "15:43", "18:32", "19:48"),
    ("14-07", "04:24", "04:39", "06:01", "12:17", "15:43", "18:32", "19:48"),
    ("15-07", "04:24", "04:39", "06:01", "12:17", "15:43", "18:32", "19:48"),
    ("16-07", "04:24", "04:39", "06:01", "12:17", "15:43", "18:32", "19:48"),
    ("17-07", "04:24", "04:39", "06:01", "12:17", "15:43", "18:32", "19:48"),
    ("18-07", "04:24", "04:39", "06:01", "12:17", "15:43", "18:32", "19:48"),
    ("19-07", "04:26", "04:41", "06:03", "12:18", "15:43", "18:32", "19:47"),
    ("20-07", "04:26", "04:41", "06:03", "12:18", "15:43", "18:32", "19:47"),
    ("21-07", "04:26", "04:41", "06:03", "12:18", "15:43", "18:32", "19:47"),
    ("22-07", "04:26", "04:41", "06:03", "12:18", "15:43", "18:32", "19:47"),
    ("23-07", "04:26", "04:41", "06:03", "12:18", "15:43", "18:32", "19:47"),
    ("24-07", "04:27", "04:42", "06:03", "12:18", "15:42", "18:31", "19:46"),
    ("25-07", "04:27", "04:42", "06:03", "12:18", "15:42", "18:31", "19:46"),
    ("26-07", "04:27", "04:42", "06:03", "12:18", "15:42", "18:31", "19:46"),
    ("27-07", "04:27", "04:42", "06:03", "12:18", "15:42", "18:31", "19:46"),
    ("28-07", "04:27", "04:42", "06:03", "12:18", "15:42", "18:31", "19:46"),
    ("29-07", "04:27", "04:42", "06:03", "12:18", "15:42", "18:31", "19:46"),
    ("30-07", "04:28", "04:43", "06:04", "12:18", "15:40", "18:31", "19:44"),
    ("31-07", "04:28", "04:43", "06:04", "12:18", "15:40", "18:31", "19:44"),
    ("01-08", "04:28", "04:43", "06:04", "12:18", "15:40", "18:31", "19:44"),
    ("02-08", "04:28", "04:43", "06:04", "12:18", "15:40", "18:31", "19:44"),
    ("03-08", "04:28", "04:43", "06:04", "12:18", "15:40", "18:31", "19:44"),
    ("04-08", "04:28", "04:43", "06:04", "12:18", "15:40", "18:31", "19:44"),
    ("05-08", "04:30", "04:45", "06:05", "12:18", "15:38", "18:29", "19:43"),
    ("06-08", "04:30", "04:45", "06:05", "12:18", "15:38", "18:29", "19:43"),
    ("07-08", "04:30", "04:45", "06:05", "12:18", "15:38", "18:29", "19:43"),
    ("08-08", "04:30", "04:45", "06:05", "12:18", "15:38", "18:29", "19:43"),
    ("09-08", "04:30", "04:45", "06:05", "12:18", "15:38", "18:29", "19:43"),
    ("10-08", "04:30", "04:45", "06:04", "12:17", "15:35", "18:27", "19:40"),
    ("11-08", "04:30", "04:45", "06:04", "12:17", "15:35", "18:27", "19:40"),
    ("12-08", "04:30", "04:45", "06:04", "12:17", "15:35", "18:27", "19:40"),
    ("13-08", "04:30", "04:45", "06:04", "12:17", "15:35", "18:27", "19:40"),
    ("14-08", "04:30", "04:45", "06:04", "12:17", "15:35", "18:27", "19:40"),
    ("15-08", "04:31", "04:46", "06:04", "12:16", "15:31", "18:26", "19:38"),
    ("16-08", "04:31", "04:46", "06:04", "12:16", "15:31", "18:26", "19:38"),
    ("17-08", "04:31", "04:46", "06:04", "12:16", "15:31", "18:26", "19:38"),
    ("18-08", "04:31", "04:46", "06:04", "12:16", "15:31", "18:26", "19:38"),
    ("19-08", "04:31", "04:46", "06:04", "12:16", "15:31", "18:26", "19:38"),
    ("20-08", "04:31", "04:46", "06:04", "12:15", "15:28", "18:24", "19:36"),
    ("21-08", "04:31", "04:46", "06:04", "12:15", "15:28", "18:24", "19:36"),
    ("22-08", "04:31", "04:46", "06:04", "12:15", "15:28", "18:24", "19:36"),
    ("23-08", "04:31", "04:46", "06:04", "12:15", "15:28", "18:24", "19:36"),
    ("24-08", "04:31", "04:46", "06:04", "12:14", "15:25", "18:22", "19:34"),
    ("25-08", "04:31", "04:46", "06:04", "12:14", "15:25", "18:22", "19:34"),
    ("26-08", "04:31", "04:46", "06:04", "12:14", "15:25", "18:22", "19:34"),
    ("27-08", "04:32", "04:47", "06:04", "12:13", "15:22", "18:21", "19:32"),
    ("28-08", "04:32", "04:47", "06:04", "12:13", "15:22", "18:21", "19:32"),
    ("29-08", "04:32", "04:47", "06:04", "12:13", "15:22", "18:21", "19:32"),
    ("30-08", "04:32", "04:47", "06:03", "12:13", "15:19", "18:19", "19:30"),
    ("31-08", "04:32", "04:47", "06:03", "12:13", "15:19", "18:19", "19:30"),
    ("01-09", "04:32", "04:47", "06:03", "12:13", "15:19", "18:19", "19:30"),
    ("02-09", "04:32", "04:47", "06:03", "12:12", "15:16", "18:18", "19:28"),
    ("03-09", "04:32", "04:47", "06:03", "12:12", "15:16", "18:18", "19:28"),
    ("04-09", "04:32", "04:47", "06:03", "12:12", "15:16", "18:18", "19:28"),
    ("05-09", "04:32", "04:47", "06:03", "12:11", "15:13", "18:16", "19:27"),
    ("06-09", "04:32", "04:47", "06:03", "12:11", "15:13", "18:16", "19:27"),
    ("07-09", "04:32", "04:47", "06:03", "12:11", "15:13", "18:16", "19:27"),
    ("08-09", "04:32", "04:47", "06:03", "12:11", "15:13", "18:16", "19:27"),
    ("09-09", "04:31", "04:46", "06:02", "12:09", "15:13", "18:14", "19:25"),
    ("10-09", "04:31", "04:46", "06:02", "12:09", "15:13", "18:14", "19:25"),
    ("11-09", "04:31", "04:46", "06:02", "12:09", "15:13", "18:14", "19:25"),
    ("12-09", "04:31", "04:46", "06:02", "12:08", "15:14", "18:13", "19:23"),
    ("13-09", "04:31", "04:46", "06:02", "12:08", "15:14", "18:13", "19:23"),
    ("14-09", "04:31", "04:46", "06:02", "12:08", "15:14", "18:13", "19:23"),
    ("15-09", "04:30", "04:45", "06:01", "12:07", "15:14", "18:11", "19:21"),
    ("16-09", "04:30", "04:45", "06:01", "12:07", "15:14", "18:11", "19:21"),
    ("17-09", "04:30", "04:45", "06:01", "12:07", "15:14", "18:11", "19:21"),
    ("18-09", "04:30", "04:45", "06:00", "12:06", "15:15", "18:08", "19:19"),
    ("19-09", "04:30", "04:45", "06:00", "12:06", "15:15", "18:08", "19:19"),
    ("20-09", "04:30", "04:45", "06:00", "12:06", "15:15", "18:08", "19:19"),
    ("21-09", "04:30", "04:45", "06:00", "12:06", "15:15", "18:08", "19:19"),
    ("22-09", "04:30", "04:45", "06:00", "12:06", "15:15", "18:08", "19:19"),
    ("23-09", "04:29", "04:44", "06:00", "12:04", "15:16", "18:07", "19:17"),
    ("24-09", "04:29", "04:44", "06:00", "12:04", "15:16", "18:07", "19:17"),
    ("25-09", "04:29", "04:44", "06:00", "12:04", "15:16", "18:07", "19:17"),
    ("26-09", "04:29", "04:44", "06:00", "12:04", "15:16", "18:07", "19:17"),
    ("27-09", "04:29", "04:44", "05:59", "12:03", "15:16", "18:05", "19:14"),
    ("28-09", "04:29", "04:44", "05:59", "12:03", "15:16", "18:05", "19:14"),
    ("29-09", "04:29", "04:44", "05:59", "12:03", "15:16", "18:05", "19:14"),
    ("30-09", "04:29", "04:44", "05:59", "12:03", "15:16", "18:05", "19:14"),
    ("01-10", "04:28", "04:43", "05:59", "12:02", "15:16", "18:03", "19:12"),
    ("02-10", "04:28", "04:43", "05:59", "12:02", "15:16", "18:03", "19:12"),
    ("03-10", "04:28", "04:43", "05:58", "12:01", "15:16", "18:01", "19:11"),
    ("04-10", "04:28", "04:43", "05:58", "12:01", "15:16", "18:01", "19:11"),
    ("05-10", "04:28", "04:43", "05:58", "12:01", "15:16", "18:01", "19:11"),
    ("06-10", "04:28", "04:43", "05:58", "12:01", "15:16", "18:01", "19:11"),
    ("07-10", "04:27", "04:42", "05:58", "12:00", "15:16", "17:59", "19:09"),
    ("08-10", "04:27", "04:42", "05:58", "12:00", "15:16", "17:59", "19:09"),
    ("09-10", "04:27", "04:42", "05:58", "11:59", "15:16", "17:58", "19:08"),
    ("10-10", "04:27", "04:42", "05:58", "11:59", "15:16", "17:58", "19:08"),
    ("11-10", "04:27", "04:42", "05:58", "11:59", "15:16", "17:58", "19:08"),
    ("12-10", "04:27", "04:42", "05:58", "11:59", "15:16", "17:58", "19:08"),
    ("13-10", "04:27", "04:42", "05:58", "11:59", "15:16", "17:58", "19:08"),
    ("14-10", "04:26", "04:41", "05:57", "11:58", "15:16", "17:56", "19:06"),
    ("15-10", "04:26", "04:41", "05:57", "11:58", "15:16", "17:56", "19:06"),
    ("16-10", "04:26", "04:41", "05:57", "11:58", "15:16", "17:56", "19:06"),
    ("17-10", "04:26", "04:41", "05:57", "11:57", "15:16", "17:55", "19:05"),
    ("18-10", "04:26", "04:41", "05:57", "11:57", "15:16", "17:55", "19:05"),
    ("19-10", "04:26", "04:41", "05:57", "11:57", "15:16", "17:55", "19:05"),
    ("20-10", "04:26", "04:41", "05:57", "11:57", "15:16", "17:55", "19:05"),
    ("21-10", "04:26", "04:41", "05:57", "11:57", "15:16", "17:55", "19:05"),
    ("22-10", "04:26", "04:41", "05:57", "11:57", "15:16", "17:55", "19:05"),
    ("23-10", "04:26", "04:41", "05:57", "11:56", "15:17", "17:53", "19:04"),
    ("24-10", "04:26", "04:41", "05:57", "11:56", "15:17", "17:53", "19:04"),
    ("25-10", "04:26", "04:41", "05:57", "11:56", "15:17", "17:53", "19:04"),
    ("26-10", "04:26", "04:41", "05:57", "11:56", "15:17", "17:53", "19:04"),
    ("27-10", "04:26", "04:41", "05:57", "11:56", "15:17", "17:53", "19:04"),
    ("28-10", "04:26", "04:41", "05:57", "11:56", "15:17", "17:53", "19:04"),
    ("29-10", "04:26", "04:41", "05:57", "11:56", "15:17", "17:53", "19:04"),
    ("30-10", "04:26", "04:41", "05:57", "11:56", "15:17", "17:53", "19:04"),
    ("31-10", "04:26", "04:41", "05:57", "11:56", "15:17", "17:53", "19:04"),
    ("01-11", "04:26", "04:41", "05:59", "11:56", "15:17", "17:51", "19:03"),
    ("02-11", "04:26", "04:41", "05:59", "11:56", "15:17", "17:51", "19:03"),
    ("03-11", "04:26", "04:41", "05:59", "11:56", "15:17", "17:51", "19:03"),
    ("04-11", "04:26", "04:41", "05:59", "11:56", "15:17", "17:51", "19:03"),
    ("05-11", "04:26", "04:41", "05:59", "11:56", "15:17", "17:51", "19:03"),
    ("06-11", "04:26", "04:41", "05:59", "11:56", "15:17", "17:51", "19:03"),
    ("07-11", "04:26", "04:41", "05:59", "11:56", "15:17", "17:51", "19:03"),
    ("08-11", "04:26", "04:41", "06:00", "11:56", "15:18", "17:50", "19:02"),
    ("09-11", "04:26", "04:41", "06:00", "11:56", "15:18", "17:50", "19:02"),
    ("10-11", "04:26", "04:41", "06:00", "11:56", "15:18", "17:50", "19:02"),
    ("11-11", "04:26", "04:41", "06:00", "11:56", "15:18", "17:50", "19:02"),
    ("12-11", "04:26", "04:41", "06:00", "11:56", "15:18", "17:50", "19:02"),
    ("13-11", "04:26", "04:41", "06:00", "11:56", "15:18", "17:50", "19:02"),
    ("14-11", "04:26", "04:41", "06:00", "11:56", "15:18", "17:50", "19:02"),
    ("15-11", "04:26", "04:41", "06:00", "11:56", "15:18", "17:50", "19:02"),
    ("16-11", "04:27", "04:42", "06:02", "11:57", "15:17", "17:51", "19:03"),
    ("17-11", "04:27", "04:42", "06:02", "11:57", "15:17", "17:51", "19:03"),
    ("18-11", "04:27", "04:42", "06:02", "11:57", "15:17", "17:51", "19:03"),
    ("19-11", "04:27", "04:42", "06:02", "11:57", "15:17", "17:51", "19:03"),
    ("20-11", "04:27", "04:42", "06:02", "11:57", "15:17", "17:51", "19:03"),
    ("21-11", "04:27", "04:42", "06:02", "11:57", "15:17", "17:51", "19:03"),
    ("22-11", "04:28", "04:43", "06:03", "11:58", "15:20", "17:51", "19:04"),
    ("23-11", "04:28", "04:43", "06:03", "11:58", "15:20", "17:51", "19:04"),
    ("24-11", "04:28", "04:43", "06:03", "11:58", "15:20", "17:51", "19:04"),
    ("25-11", "04:30", "04:45", "06:05", "11:59", "15:21", "17:51", "19:05"),
    ("26-11", "04:30", "04:45", "06:05", "11:59", "15:21", "17:51", "19:05"),
    ("27-11", "04:30", "04:45", "06:05", "11:59", "15:21", "17:51", "19:05"),
    ("28-11", "04:30", "04:45", "06:06", "12:00", "15:22", "17:52", "19:06"),
    ("29-11", "04:30", "04:45", "06:06", "12:00", "15:22", "17:52", "19:06"),
    ("30-11", "04:30", "04:45", "06:06", "12:00", "15:22", "17:52", "19:06"),
    ("01-12", "04:32", "04:47", "06:08", "12:01", "15:23", "17:53", "19:07"),
    ("02-12", "04:32", "04:47", "06:08", "12:01", "15:23", "17:53", "19:07"),
    ("03-12", "04:32", "04:47", "06:08", "12:01", "15:23", "17:53", "19:07"),
    ("04-12", "04:33", "04:48", "06:09", "12:00", "15:24", "17:54", "19:08"),
    ("05-12", "04:33", "04:48", "06:09", "12:00", "15:24", "17:54", "19:08"),
    ("06-12", "04:33", "04:48", "06:09", "12:00", "15:24", "17:54", "19:08"),
    ("07-12", "04:34", "04:49", "06:10", "12:04", "15:25", "17:55", "19:09"),
    ("08-12", "04:34", "04:49", "06:10", "12:04", "15:25", "17:55", "19:09"),
    ("09-12", "04:34", "04:49", "06:10", "12:04", "15:25", "17:55", "19:09"),
    ("10-12", "04:35", "04:50", "06:12", "12:05", "15:26", "17:56", "19:11"),
    ("11-12", "04:35", "04:50", "06:12", "12:05", "15:26", "17:56", "19:11"),
    ("12-12", "04:36", "04:51", "06:13", "12:06", "15:28", "17:57", "19:12"),
    ("13-12", "04:36", "04:51", "06:13", "12:06", "15:28", "17:57", "19:12"),
    ("14-12", "04:36", "04:51", "06:13", "12:06", "15:28", "17:57", "19:12"),
    ("15-12", "04:38", "04:53", "06:15", "12:07", "15:29", "17:58", "19:14"),
    ("16-12", "04:38", "04:53", "06:15", "12:07", "15:29", "17:58", "19:14"),
    ("17-12", "04:39", "04:54", "06:15", "12:08", "15:30", "17:59", "19:14"),
    ("18-12", "04:39", "04:54", "06:15", "12:08", "15:30", "17:59", "19:14"),
    ("19-12", "04:39", "04:54", "06:16", "12:09", "15:30", "18:00", "19:15"),
    ("20-12", "04:39", "04:54", "06:16", "12:09", "15:30", "18:00", "19:15"),
    ("21-12", "04:41", "04:56", "06:18", "12:10", "15:32", "18:01", "19:16"),
    ("22-12", "04:41", "04:56", "06:18", "12:11", "15:32", "18:02", "19:17"),
    ("23-12", "04:41", "04:56", "06:18", "12:11", "15:32", "18:02", "19:17"),
    ("24-12", "04:41", "04:56", "06:18", "12:11", "15:32", "18:02", "19:17"),
    ("25-12", "04:41", "04:56", "06:18", "12:11", "15:32", "18:02", "19:17"),
    ("26-12", "04:42", "04:57", "06:19", "12:13", "15:33", "18:03", "19:18"),
    ("27-12", "04:42", "04:57", "06:19", "12:13", "15:33", "18:03", "19:18"),
    ("28-12", "04:44", "04:59", "06:21", "12:14", "15:35", "18:04", "19:19"),
    ("29-12", "04:44", "04:59", "06:21", "12:14", "15:35", "18:04", "19:19"),
    ("30-12", "04:45", "05:00", "06:22", "12:15", "15:36", "18:05", "19:20"),
    ("31-12", "04:45", "05:00", "06:22", "12:15", "15:36", "18:05", "19:20"),
        # Add more rows here as needed
    ]

    # Insert the data into the table
    cursor.executemany('''
        INSERT OR IGNORE INTO prayer_times (date, sahr_end, fajr, sunrise, luhr, asr, maghrib, isha)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_rows)

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

database()