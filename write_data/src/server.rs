#![feature(duration_checked_float)]
use rand::distributions::{Exp, IndependentSample};
use rand::Rng;
use std::fs::File;
use std::io::prelude::*;
use std::thread;
use std::time::{Duration, Instant, SystemTime, UNIX_EPOCH};
use tokio::sync::mpsc;
use tokio_stream::wrappers::ReceiverStream;
use tonic::{transport::Server, Request, Response, Status};

use write_data::data_stream_server::{DataStream, DataStreamServer};
use write_data::{DataRequest, DataResponse};

pub mod write_data {
    tonic::include_proto!("data");
}

#[derive(Debug, Default)]
pub struct MyDataStream {}

fn wait(lambda: f64) -> f64 {
    let exp = Exp::new(lambda);
    let v = exp.ind_sample(&mut rand::thread_rng());
    return v;
}

#[tonic::async_trait]
impl DataStream for MyDataStream {
    type StreamDataStream = ReceiverStream<Result<DataResponse, Status>>;
    async fn stream_data(
        &self,
        request: Request<DataRequest>,
    ) -> Result<Response<Self::StreamDataStream>, Status> {
        println!("Got a request: {:?}", request);

        let (tx, rx) = mpsc::channel(4);
        tokio::spawn(async move {
            let lambda = 0.2;
            let mut growing_file = File::create("data_file.txt").unwrap();
            let random_bytes = rand::thread_rng().gen::<[u8; 32]>();
            loop {
                let interarrival = wait(lambda);

                let ii_duration = Duration::try_from_secs_f64(lambda);
                thread::sleep(ii_duration.unwrap());

                let now = Instant::now();
                growing_file.write_all(&random_bytes);
                let write_service_time = now.elapsed();

                let system_now = SystemTime::now();
                let data = DataResponse {
                    time: system_now
                        .duration_since(UNIX_EPOCH)
                        .unwrap()
                        .as_millis()
                        .to_string(),
                    interarrival: interarrival,
                    service: write_service_time.as_nanos().to_string(),
                };
                tx.send(Ok(data)).await;
            }
        });

        Ok(Response::new(ReceiverStream::from(rx)))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:50051".parse()?;
    let stream = MyDataStream::default();

    Server::builder()
        .add_service(DataStreamServer::new(stream))
        .serve(addr)
        .await?;

    Ok(())
}
