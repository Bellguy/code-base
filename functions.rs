pub fn expected_minutes_in_oven() -> i32 {
    let time = 40;
    time
}
pub fn remaining_minutes_in_oven(actual_minutes_in_oven: i32) -> i32 {
    let y = expected_minutes_in_oven() - actual_minutes_in_oven;
    y
}
pub fn preparation_time_in_minutes(number_of_layers: i32) -> i32 {
    let prep = number_of_layers * 2;
    prep
}
pub fn elapsed_time_in_minutes(number_of_layers: i32, actual_minutes_in_oven: i32) -> i32 {
    let elap = preparation_time_in_minutes(number_of_layers) + actual_minutes_in_oven;
    elap
}

fn main() {
    println!("Expected time in oven: {}", expected_minutes_in_oven());
    println!("Remaining time in oven: {}", remaining_minutes_in_oven(12));
    println!("Prep time: {}", preparation_time_in_minutes(4));
    println!("Elapsed time: {}", elapsed_time_in_minutes(4, 12));
}
