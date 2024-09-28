use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn calculate_calibration_sum<P>(filename: P) -> io::Result<u32>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    let mut total_sum = 0;

    for line in reader.lines() {
        let line = line?;
        let digits: Vec<char> = line.chars().filter(|c| c.is_digit(10)).collect();
        
        if let (Some(first), Some(last)) = (digits.first(), digits.last()) {
            let calibration_value = format!("{}{}", first, last).parse::<u32>().unwrap_or(0);
            total_sum += calibration_value;
        }
    }

    Ok(total_sum)
}

fn main() -> io::Result<()> {
    let result = calculate_calibration_sum("file.txt")?;
    println!("The sum of all calibration values is: {}", result);
    Ok(())
}
