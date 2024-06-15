pub fn binarysearch(vec: Vec<isize>, target: isize) -> isize {
    let lo = 0;
    let hi = vec.len();

    while lo < hi {
        let mid = lo + (hi - lo) / 2;
        if vec[mid] == target {
            return mid;
        }
    }
    -1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let vec = vec![
            0, 4, 8, 12, 15, 18, 21, 25, 29, 34, 38, 42, 45, 47, 50, 54, 57, 60, 63, 67,
        ];
        let result = binarysearch(vec, 34);
        assert_eq!(result, 4);
    }
}
