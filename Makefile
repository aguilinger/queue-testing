
build-server:
	cd write_data && cargo build

build-client:
	python3 -m grpc_tools.protoc -I./proto --python_out=data_client --grpc_python_out=data_client ./proto/data.proto

run-server:
	cd write_data && cargo run

run-client:
	python3 data_client/client.py