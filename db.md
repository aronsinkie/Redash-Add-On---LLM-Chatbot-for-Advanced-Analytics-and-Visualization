- Channels
  - channel_id (PK)
  - name
  - description
  - creation_date

- Users
  - user_id (PK)
  - username
  - subscriber_count

- Videos
  - video_id (PK)
  - channel_id (FK)
  - title
  - description
  - upload_date
  - duration
  - views
  - likes
  - comments

- Analytics
  - analytics_id (PK)
  - video_id (FK)
  - month
  - views
  - likes
  - comments

- Expenses
  - expense_id (PK)
  - video_id (FK)
  - expense_type
  - amount
  - date
