// export default function bubblesort(arr: Number[]): Number[] {
//   let sorted_idx = arr.length - 1;
//   while (sorted_idx > 0) {
//     for (let i = 0; i < sorted_idx; i++) {
//       if (arr[i] > arr[i + 1]) {
//         let temp = arr[i];
//         arr[i] = arr[i + 1];
//         arr[i + 1] = temp;
//       }
//     }
//     --sorted_idx;
//   }
//   return arr;
// }
//
// export default function bubblesort(arr: Number[]): Number[] {
//
//   for (let i = 0; i < arr.length; ++i) {
//
//     for (let j = 0; j < arr.length - 1 - i; ++j) {
//       if (arr[j] > arr[j + 1]) {
//         let temp = arr[j];
//         arr[j] = arr[j + 1];
//         arr[j + 1] = temp;
//       }
//     }
//   }
//
//   return arr
// }

export default function bubblesort(arr: number[]): number[] {
  let sorted = arr.length - 1;

  do {
    for (let i = 0; i < sorted; i++) {
      let curr = arr[i];
      let next = arr[i + 1];

      if (curr > next) {
        let temp = curr;
        arr[i] = next;
        arr[i + 1] = temp;
      }
    }
    --sorted;
  } while (sorted > 0);
  return arr;
}
