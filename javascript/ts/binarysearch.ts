export default function binarysearch(arr: Number[], target: Number): Number {
  let l = 0;
  let h = arr.length;

  do {
    let m = Math.floor(l + (h - l) / 2);
    let num = arr[m];
    if (num === target) return m;
    if (target > num) {
      l = m + 1;
    } else {
      h = m;
    }
  } while (l < h);
  return -1;
}
