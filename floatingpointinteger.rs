pub fn production_rate_per_hour(speed: u8) -> f64 {
    let speedFloat = speed as f64;
    let cars = speedFloat * 221.0;
    
    if speedFloat < 5.0 {
        let production = cars;
        production
    }
    else if speedFloat < 9.0 {
        let production = cars * 0.9;
        production
    }
    else {
        let production = cars * 0.77;
        production
    }
}
pub fn working_items_per_minute(speed: u8) -> u32 {
    let speedFloat = speed as f64;
    let cars = speedFloat * (221.0 / 60.0);
    
    if speedFloat < 5.0 {
        let production = cars;
        let productionUnsign = production as u32;
        productionUnsign
    }
    else if speedFloat < 9.0 {
        let production = cars * 0.9;
        let productionUnsign = production as u32;
        productionUnsign
    }
    else {
        let production = cars * 0.77;
        let productionUnsign = production as u32;
        productionUnsign
    }
}

fn main() {
    println!("Production rate per hour: {}", production_rate_per_hour(6));
    println!("Working items per minute: {}", working_items_per_minute(6));
}