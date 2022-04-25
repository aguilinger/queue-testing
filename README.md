# Disk Queue Testing

Consists of a gRPC server written in rust and client written in python. The server will write a fixed amount of data on an interval dictated by a Poisson distribution with a set lambda. The server will stream responses consisting of the amount of time taken to write the data (the "service time" in our scenario) back to the client.

## Run

Get the server code on the instance of choice (you may have to build the server code on a VM as well, I would recommend doing that separately, copying the binary to local, and copying that binary onto a new, fresh machine for running the actual experiment) and run it. Then run the client while supplying the client IP and a lambda value by running `CLIENT_URL=[IP] LAMBDA=[LAMBDA] docker compose up`.

## Evaluate

The data will be available in a locally running redis and a jupyter notebook will be spun up alongside the docker compose to fetch and analyze the data. The schema generally follows that measurements of write times are stored in a list per lambda value they ran at under the `service:[LAMBDA]` key (i.e. a lambda of 0.2 would be at `service:0.2`). The interarrival times are also stored per lambda at `arrival:[LAMBDA]`. And finally write wait times over time are stored at `service:time`