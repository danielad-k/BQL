# Brightedge API 
This wrapper allows you to connect to Brightedge API

# Authenticating
Brightedge authentication is based on username, password, and account id which you can receive from the account management team. 
# Using BQL
There are two parts to using BQL package:
 1. Construct Query: 
	   ```
	counters = 5000 #how many records
    offset = 0 #start at which row
    time = {"time": "monthly"} #at what granularity
    dataset = "keyword" #using keyword dataset
    dimensions = ["keyword", "time", "search_engine"] 
    measures = ["rank", "blended_rank"]
    filtering = [["time", "eq", "201901"], ["search_engine", [["1", "45"], ["1", "46"]]]] #filter by month and search engine
				
    payload = QueryConstruct(dataset, dimensions, measures, time, filtering, counters, offset).query()
				```
 2. Get BQL data using the query: 
	   ```
    bql = BqlAPI.bql_output(payload, account_id, email, password)
				```
