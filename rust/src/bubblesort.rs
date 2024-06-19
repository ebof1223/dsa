// fn bubblesort(mut arr: Vec<isize>) -> Vec<isize> {
//     let mut sorted = arr.len() - 1;
//
//     while sorted > 0 {
//         for i in 0..sorted {
//             if arr[i] > arr[i + 1] {
//                 let tmp = arr[i];
//                 arr[i] = arr[i + 1];
//                 arr[i + 1] = tmp
//             }
//         }
//         sorted -= 1;
//     }
//
//     return arr;
// }

fn bubblesort(mut arr: Vec<isize>) -> Vec<isize> {
    for i in 0..arr.len() {
        for j in 0..arr.len() - 1 - i {
            if arr[j] > arr[j + 1] {
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    return arr;
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn bubblesortn() {
        let unsorted_arr = vec![
            42, 32, 60, 17, 90, 82, 56, 29, 74, 64, 15, 87, 98, 51, 41, 19, 61, 55, 39, 71, 23, 45,
            68, 37, 91, 47, 88, 67, 22, 48, 99, 54, 25, 34, 62, 73, 16, 31, 49, 94, 81, 33, 21, 85,
            46, 72, 11, 59, 53, 76, 40, 57, 13, 79, 24, 65, 93, 43, 27, 89, 50, 12, 70, 35, 18, 63,
            84, 92, 38, 44, 100, 30, 66, 58, 83, 77, 52, 26, 78, 36, 75, 14, 86, 28, 20, 95, 97,
            69, 10, 96, 80,
        ];
        assert_eq!(
            bubblesort(unsorted_arr),
            vec![
                10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93,
                94, 95, 96, 97, 98, 99, 100
            ]
        )
    }

    #[test]
    fn bubblesort_1() {
        assert_eq!(bubblesort(vec![1, 0]), vec![0, 1])
    }
}
