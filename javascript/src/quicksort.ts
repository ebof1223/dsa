function partition(arr: number[], lo: number, hi: number) {
  let sorted = lo;
  for (let i = lo; i <= hi; i++) {
    if (arr[i] <= arr[hi]) {
      let temp = arr[sorted];
      arr[sorted] = arr[i];
      arr[i] = temp;
      sorted++;
    }
  }
  return sorted - 1
}


function qs(arr: number[], lo: number, hi: number) {
  if (lo >= hi) return
  const idx = partition(arr, lo, hi);
  qs(arr, lo, idx - 1)
  qs(arr, idx + 1, hi)
}

export default function quicksort(arr: number[]): number[] {
  qs(arr, 0, arr.length - 1)
  return arr
}
