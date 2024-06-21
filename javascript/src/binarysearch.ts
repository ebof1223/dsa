export default function binarysearch(arr: Number[], target: Number): Number {
  let lo = 0;
  let hi = arr.length - 1;

  do {
    let mid = Math.floor(lo + (hi - lo) / 2);

    if (arr[mid] === target) return mid;

    if (arr[mid] > target) {
      hi = mid;
    } else {
      lo = mid + 1;
    }
  } while (lo < hi);
  return -1;
}
