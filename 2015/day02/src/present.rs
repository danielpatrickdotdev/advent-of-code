use std::str::Split;

#[derive(Debug)]
pub struct Present {
    l: i32,
    w: i32,
    h: i32,
}

impl Present {
    pub fn new(s: &str) -> Self {
        let mut iter = s.split("x");
        let l = Present::parse_dim(&mut iter, "length");
        let w = Present::parse_dim(&mut iter, "width");
        let h = Present::parse_dim(&mut iter, "height");

        Present {l, w, h}
    }

    pub fn wrapping_paper_required(&self) -> i32 {
        self.surface_area() + self.smallest_side_area()
    }

    pub fn ribbon_required(&self) -> i32 {
        let mut dims = vec![self.l, self.w, self.h];
        dims.sort_unstable_by(|a, b| b.cmp(a));

        let wrap = 2 * dims.pop().unwrap() + 2 * dims.pop().unwrap();

        wrap + self.l * self.w * self.h
    }

    // Private helper functions & methods

    fn parse_dim(iter: &mut Split<&str>, dim: &str) -> i32 {
        iter.next().expect(&format!("No {} provided", dim))
            .parse().expect(&format!("Invalid {} provided", dim))
    }

    fn surface_area(&self) -> i32 {
        2 * self.l * self.w + 2 * self.w * self.h + 2 * self.h * self.l
    }

    fn smallest_side_area(&self) -> i32 {
        let mut dims = vec![self.l, self.w, self.h];
        dims.sort_unstable_by(|a, b| b.cmp(a));
        dims.pop().unwrap() * dims.pop().unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_constructor() {
        let to_test = [
            ("1x1x1", 1, 1, 1),
            ("11x22x33", 11, 22, 33),
        ];

        for (input, l, w, h) in to_test.iter() {
            let p = Present::new(&input);
            assert_eq!(l, &p.l);
            assert_eq!(w, &p.w);
            assert_eq!(h, &p.h);
        }
    }

    #[test]
    fn test_surface_area() {
        let to_test = [
            (Present { l: 2, w: 3, h: 4 }, 52),
            (Present { l: 1, w: 1, h: 10 }, 42),
        ];

        for (p, area) in to_test.iter() {
            assert_eq!(*area, p.surface_area());
        }
    }

    #[test]
    fn test_smallest_side_area() {
        let to_test = [
            (Present { l: 2, w: 3, h: 4 }, 6),
            (Present { l: 1, w: 1, h: 10 }, 1),
            (Present { l: 10, w: 1, h: 1 }, 1),
        ];

        for (p, area) in to_test.iter() {
            assert_eq!(*area, p.smallest_side_area());
        }
    }

    #[test]
    fn test_wrapping_paper_required() {
        let to_test = [
            (Present { l: 2, w: 3, h: 4 }, 58),
            (Present { l: 1, w: 1, h: 10 }, 43),
            (Present { l: 10, w: 1, h: 1 }, 43),
        ];

        for (p, area) in to_test.iter() {
            assert_eq!(*area, p.wrapping_paper_required());
        }
    }

    #[test]
    fn test_ribbon_required() {
        let to_test = [
            (Present { l: 2, w: 3, h: 4 }, 34),
            (Present { l: 1, w: 1, h: 10 }, 14),
            (Present { l: 10, w: 1, h: 1 }, 14),
        ];

        for (p, length) in to_test.iter() {
            assert_eq!(*length, p.ribbon_required());
        }
    }
}
