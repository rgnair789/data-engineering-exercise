Objective:
----------
Pull data from API and create csv files for 1) authors 2) books 3) map between book and author.

Approach:
---------
1. Obtain data from API. This data could either be stored as a file (for large inputs) or put in memory (used set to avoid dup enteries).
2. Dump data from step 1 into csv files.

How to run:
-----------
1. Change the subject to the one of choice. I have chosen 'fantasy' in this exercise. It is specified as input parameter to get_feed method.
2. Change the directory where csv file is to be created in the python script. (variable used is target_dir)
3. Run the python script raghunathnair_gobanking_assignment.py

Tests:
-----
There are checks included for the following.
1. Feed obtained from API 
2. Check if the data for book and author has multiple values for the same key.
3. The csv file that is created exceeds a certain threshold in size. 

Enhancements:
------------
Would like to dump the data into tables:
1. Book
2. Author
3. Book_Author


DDL
---
create table d_book
(book_key varchar 
,book_name varchar 
... dimensional attributes for book
,record_inserted_ts
)

create table d_author
(author_key varchar
,author_name varchar
... dimensional attributes for author
,record_inserted_ts
)

create table book_author_map
(book_key varchar
,author_key varchar
,book_name varchar
,author_name varchar
,record_inserted_ts
)


Things to consider:
------------------
1. Volume of the feed.
2. Do we need to store historical data. partitioning on date might be needed or alternatively type-2 dimension can be used.
3. The creation of fact tables will be influenced by how its usage.
4. Would prefer to store the feed data into a file if it is large or it is necessary to save raw data as is.
5. Log file could also be created to capture the process info.

Sample output:
-------------
Book:
Book_key		Book_name
/works/OL138052W	Alice's Adventures in Wonderland
/works/OL24034W	Treasure Island
/works/OL18417W	The Wonderful Wizard of Oz
/works/OL20600W	Gulliver's Travels
/works/OL1089297W	Il principe
/works/OL259010W	A Midsummer Night's Dream
/works/OL1527356W	Le avventure di Pinocchio
/works/OL151406W	Through the Looking-Glass
/works/OL6583284W	The princess and the goblin
/works/OL262460W	The Lost World
/works/OL151411W	Alice's Adventures in Wonderland / Through the Looking Glass
/works/OL99499W	Five Children and It

Author:
Author_key			Author_name
/authors/OL2658427A	Arthur Hughes
/authors/OL462466A	Michael Foreman
/authors/OL162098A	Carlo Collodi
/authors/OL10788566A	pablo perez
/authors/OL9348793A	L. Frank Baum
/authors/OL23135A		Niccolò Machiavelli
/authors/OL9017297A	Jenny Sánchez
/authors/OL3570038A	Benjamin Lacombe
/authors/OL9242194A	David Guerra
/authors/OL23082A		George MacDonald
/authors/OL23761A		Kenneth Grahame
/authors/OL7011707A	Joseph Delaney
/authors/OL9645075A	leonardo pablo federico sanchez alonso
/authors/OL9388A		William Shakespeare

Book-Author:
Book_key		Author_key			Book_name				Author_name
/works/OL259010W	/authors/OL9388A		A Midsummer Night's Dream	William Shakespeare
/works/OL1527356W	/authors/OL162098A	Le avventure di Pinocchio	Carlo Collodi
/works/OL6583284W	/authors/OL2658427A	The princess and the goblin	Arthur Hughes
/works/OL18417W	/authors/OL11187123A	The Wonderful Wizard of Oz	Alejandro lucas matias sanchez alonso
/works/OL6583284W	/authors/OL10025480A	The princess and the goblin	The Princess and the Goblin Annotated MacDonald
/works/OL18417W	/authors/OL3570038A	The Wonderful Wizard of Oz	Benjamin Lacombe
/works/OL18417W	/authors/OL952315A	The Wonderful Wizard of Oz	J. T. Barbarese
/works/OL99499W	/authors/OL18053A		Five Children and It		Edith Nesbit
/works/OL6583284W	/authors/OL1394235A	The princess and the goblin	Cecilia Dart-Thornton
/works/OL18417W	/authors/OL9645075A	The Wonderful Wizard of Oz	leonardo pablo federico sanchez alonso
/works/OL18417W	/authors/OL9645484A	The Wonderful Wizard of Oz	alejandro sanchez
/works/OL18417W	/authors/OL462466A	The Wonderful Wizard of Oz	Michael Foreman
/works/OL18417W	/authors/OL7174484A	The Wonderful Wizard of Oz	Sébastien Perez
/works/OL18417W	/authors/OL9017297A	The Wonderful Wizard of Oz	Jenny Sánchez
/works/OL6583284W	/authors/OL10494172A	The princess and the goblin	George Macdonald
/works/OL18417W	/authors/OL9633728A	The Wonderful Wizard of Oz	federico alonso


 