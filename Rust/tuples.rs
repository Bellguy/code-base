pub fn divmod(dividend: i16, divisor: i16) -> (i16, i16) {
    let quotient = dividend / divisor;
    let remainder = dividend % divisor;
    return (quotient, remainder)
}

pub fn evens<T>(iter: impl Iterator<Item = T>) -> impl Iterator<Item = T> {
    let even_nums = iter.enumerate()
        .filter(|(i,v)| i % 2 == 0)
        .map(|(i,v)| v);
    return even_nums
}

pub struct Position(pub i16, pub i16);
impl Position {
    pub fn manhattan(&self) -> i16 {
       (&self.0 - 0).abs() + (&self.1 - 0).abs()
    }
}

fn main() {
    let my_div = divmod(450, 79);
    let my_pos = Position(89,430).manhattan();

    println!("{:?}", my_div);
    println!("{:?}", my_pos);
}
