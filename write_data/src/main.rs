#![feature(duration_checked_float)]
use std::fs::File;
use std::io::prelude::*;
use std::time::{Duration, Instant};
use std::thread;
use rand::distributions::{Exp, IndependentSample};
use rand::Rng;
use std::sync::mpsc;

#[derive(Debug)]
struct ThreadData {
    time: Instant,
    interarrival: f64,
    service: u128,
}

fn wait(lambda: f64) -> f64 {
    let exp = Exp::new(lambda);
    let v = exp.ind_sample(&mut rand::thread_rng());
    return v
}

fn main() {

    let (tx, rx) = mpsc::channel();
    thread::spawn(move || {
        let lambda = 0.2;
        let mut growing_file = File::create("data_file.txt").unwrap();
        loop {
            
            let interarrival = wait(lambda);
    
            let ii_duration = Duration::try_from_secs_f64(lambda);
            thread::sleep(ii_duration.unwrap());
            let random_bytes = rand::thread_rng().gen::<[u8; 32]>();
    
            
            let now = Instant::now();
            growing_file.write_all(&random_bytes);
            let write_service_time = now.elapsed();
    
            let data = ThreadData {
                time: now,
                interarrival: interarrival,
                service: write_service_time.as_nanos(),
            };
            tx.send(data).unwrap();
        }
    });
    
    for received in rx {
        println!("Got: {:?}", received);
    }
}
