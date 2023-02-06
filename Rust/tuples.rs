pub fn divmod(dividend: i16, divisor: i16) -> (i16, i16) {
    let quotient = dividend / divisor;
    let remainder = dividend % divisor;
    return (quotient, remainder)
}

pub fn evens<T>(iter: impl Iterator<Item = T>) -> impl Iterator<Item = T> {
    let coll = iter;
    
    // TODO: Finish implementing
    /*
    for (index, T) in coll.enumerate() {
        if index % 2 == 0 {
            
        }
    */
}

pub struct Position(pub i16, pub i16);
impl Position {
    pub fn manhattan(&self) -> i16 {
        // TODO
        unimplemented!("implement `fn manhattan`")
    }
}

fn main() {
    
}
