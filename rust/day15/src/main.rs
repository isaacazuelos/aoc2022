#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Coord {
    x: i64,
    y: i64,
}

#[derive(Clone, Copy)]
struct Sensor {
    coord: Coord,
    // beacon: Coord,
    range: i64,
}

impl Sensor {
    const fn new(x: i64, y: i64, beacon_x: i64, beacon_y: i64) -> Sensor {
        Sensor {
            coord: Coord { x, y },
            // beacon: Coord {
            //     x: beacon_x,
            //     y: beacon_y,
            // },
            range: (x - beacon_x).abs() + (y - beacon_y).abs(),
        }
    }

    fn covers(&self, x: i64, y: i64) -> bool {
        self.range >= ((self.coord.x - x).abs() + (self.coord.y - y).abs())
    }

    fn end_of_range_on_line(&self, y: i64) -> i64 {
        let horizontal = self.range - (y - self.coord.y).abs();
        let end = self.coord.x + horizontal;
        end
    }
}

const SENSORS: &[Sensor] = &[
    Sensor::new(1384790, 3850432, 2674241, 4192888),
    Sensor::new(2825953, 288046, 2154954, -342775),
    Sensor::new(3553843, 2822363, 3444765, 2347460),
    Sensor::new(2495377, 3130491, 2761496, 2831113),
    Sensor::new(1329263, 1778185, 2729595, 2000000),
    Sensor::new(2882039, 2206085, 2729595, 2000000),
    Sensor::new(3903141, 2510440, 4006219, 3011198),
    Sensor::new(3403454, 3996578, 3754119, 4475047),
    Sensor::new(3630476, 1048796, 3444765, 2347460),
    Sensor::new(16252, 2089672, -276514, 2995794),
    Sensor::new(428672, 1150723, -281319, 668868),
    Sensor::new(2939101, 3624676, 2674241, 4192888),
    Sensor::new(3166958, 2890076, 2761496, 2831113),
    Sensor::new(3758241, 3546895, 4006219, 3011198),
    Sensor::new(218942, 3011070, -276514, 2995794),
    Sensor::new(52656, 3484635, -276514, 2995794),
    Sensor::new(2057106, 405314, 2154954, -342775),
    Sensor::new(1966905, 2495701, 2761496, 2831113),
    Sensor::new(511976, 2696731, -276514, 2995794),
    Sensor::new(3094465, 2478570, 3444765, 2347460),
    Sensor::new(806671, 228252, -281319, 668868),
    Sensor::new(3011731, 1976307, 2729595, 2000000),
];

fn part_2(sensors: &[Sensor], max: i64) -> Option<Coord> {
    let mut y = 0;
    while y <= max {
        let mut x = 0;
        while x <= max {
            let mut seen = false;
            'sensors: for sensor in sensors {
                if sensor.covers(x, y) {
                    x = sensor.end_of_range_on_line(y);
                    seen = true;
                    break 'sensors;
                }
            }

            if !seen {
                return Some(Coord { x, y });
            } else {
                x += 1;
            }
        }
        y += 1;
    }
    None
}

fn main() {
    let ans = part_2(&SENSORS, 4000000).expect("an answer was not found");
    let freq = (ans.x * 4000000) + ans.y;
    println!("part 2: {} with {:?}", freq, ans);
}

#[cfg(test)]
mod test {
    use super::*;

    const TEST_SENSORS: &[Sensor] = &[
        Sensor::new(2, 18, -2, 15),
        Sensor::new(9, 16, 10, 16),
        Sensor::new(13, 2, 15, 3),
        Sensor::new(12, 14, 10, 16),
        Sensor::new(10, 20, 10, 16),
        Sensor::new(14, 17, 10, 16),
        Sensor::new(8, 7, 2, 10),
        Sensor::new(2, 0, 2, 10),
        Sensor::new(0, 11, 2, 10),
        Sensor::new(20, 14, 25, 17),
        Sensor::new(17, 20, 21, 22),
        Sensor::new(16, 7, 15, 3),
        Sensor::new(14, 3, 15, 3),
        Sensor::new(20, 1, 15, 3),
    ];

    #[test]
    fn test_main() {
        let ans = part_2(&TEST_SENSORS, 20);
        assert_eq!(ans, Some(Coord { x: 14, y: 11 }));
    }
}
