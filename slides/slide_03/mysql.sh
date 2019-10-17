mysql> select count(*) from attributes where type="ssdeep";
     count(*) : 4270

mysql> select count(*) from fuzzy_correlate_ssdeep;
     count(*) : 246285 

mysql> select ssdeep from attributes where id=291630;
     ssdeep  :  49152:F0Mnr<mark>n</mark>b04mvy6e4L ... hxq0v  

mysql> select * from fuzzy_correlate_ssdeep;
    +----+--------------+--------------+
    | id | chunk        | attribute_id |
    +----+--------------+--------------+
    |  1 | F0Mnr<mark>n</mark>YAAAA= |       291630 |
    |  2 | 0Mnr<mark>n</mark>b0AAAA= |       291630 |
    |  3 | Mnr<mark>n</mark>b04AAAA= |       291630 |
    |  4 | nr<mark>n</mark>b04kAAAA= |       291630 |
    |  5 | r<mark>n</mark>b04msAAAA= |       291630 |
    |  6 | <mark>n</mark>b04mvwAAAA= |       291630 |
    |  7 | b04mvy4AAAA= |       291630 |
    |  8 | 04mvy6cAAAA= |       291630 |
    +----+--------------+--------------+