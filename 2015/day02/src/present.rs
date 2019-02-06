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
            (2, 3, 4, 52),
            (1, 1, 10, 42),
        ];

        for (l, w, h, area) in to_test.iter() {
            let p = Present {l: *l, w: *w, h: *h};
            assert_eq!(*area, p.surface_area());
        }
    }

    #[test]
    fn test_smallest_side_area() {
        let to_test = [
            (2, 3, 4, 6),
            (1, 1, 10, 1),
            (10, 1, 1, 1),
        ];

        for (l, w, h, area) in to_test.iter() {
            let p = Present {l: *l, w: *w, h: *h};
            assert_eq!(*area, p.smallest_side_area());
        }
    }

    #[test]
    fn test_wrapping_paper_required() {
        let to_test = [
            (2, 3, 4, 58),
            (1, 1, 10, 43),
            (10, 1, 1, 43),
        ];

        for (l, w, h, area) in to_test.iter() {
            let p = Present {l: *l, w: *w, h: *h};
            assert_eq!(*area, p.wrapping_paper_required());
        }
    }

    #[test]
    fn test_ribbon_required() {
        let to_test = [
            (2, 3, 4, 34),
            (1, 1, 10, 14),
            (10, 1, 1, 14),
        ];

        for (l, w, h, length) in to_test.iter() {
            let p = Present {l: *l, w: *w, h: *h};
            assert_eq!(*length, p.ribbon_required());
        }
    }
}
