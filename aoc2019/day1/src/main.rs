const INPUT: &str = include_str!("../input_1.txt");


fn fuel_requirements(mass: i64) -> i64 {
    (mass as f64 / 3.0).floor() as i64 - 2
}

fn part1(input: &str) -> i64 {
    input
        .lines()
        .map(|line| line.parse::<i64>().expect("Should be an int"))
        .map(|mass| fuel_requirements(mass))
        .sum()
}

fn part2(input: &str) -> i64 {
    let mut fuel_total = 0;

    for line in input.lines(){
        let mass = line.parse::<i64>().expect("Should be an int");
        let mut fuel = fuel_requirements(mass);

        while fuel > 0 {
            fuel_total += fuel;
            fuel = fuel_requirements(fuel);
        }
    }

    fuel_total
}

fn main() {
    println!("part1: {}", part1(INPUT));
    println!("part2: {}", part2(INPUT));
}
