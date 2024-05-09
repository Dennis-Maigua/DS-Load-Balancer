# Define the number of requests and concurrent clients
NUM_REQUESTS=10000
CONCURRENT_CLIENTS=10

# Send requests in parallel using GNU parallel
seq $NUM_REQUESTS | parallel -j $CONCURRENT_CLIENTS curl -s http://localhost:8080
