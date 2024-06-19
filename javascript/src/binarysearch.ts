export default function binarysearch(arr: Number[], target: Number): Number {

  let lo = 0;
  let hi = arr.length;

  do {
    let mid = Math.floor(lo + (hi - lo) / 2);
    let mid_char = arr[mid];

    if (mid_char === target) return mid

    if (mid_char > target) {
      hi = mid
    } else {
      lo = mid + 1
    }


  } while (lo < hi)
  return -1
}

