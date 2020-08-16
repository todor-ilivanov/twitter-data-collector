# Twitter Data Collector
The project uses the python-twitter library, which acts as a wrapper around the Twitter API and conveniently
parses the  response into Python objects. Processing of the data was done on a per-account basis. The code is tested to ensure the calculations
made on the raw data produce correct entries for the resulting dataset.

The workflow of the Twitter Data Collector is the following:

1. Given a user ID, make a request to the Twitter API.
2. Receive a response including up to 200 most recent tweets.
3. Perform the necessary transformations on the data for
this user.
4. Repeat for the remaining user IDs until the desired number of real user records is reached.

These scripts were used as part of my final year project at university. The resulting dataset was used further in the project to train and evolve neural networks to detect "troll
 accounts on Twitter.
