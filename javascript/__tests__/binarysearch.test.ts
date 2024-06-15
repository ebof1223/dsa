import { describe, expect, test } from "@jest/globals";
import binarysearch from "../src/binarysearch";

describe("array search module", () => {
  test("binary search success: value found", () => {
    expect(
      binarysearch(
        [
          0, 4, 8, 12, 15, 18, 21, 25, 29, 34, 38, 42, 45, 47, 50, 54, 57, 60,
          63, 67,
        ],
        34,
      ),
    ).toBe(9);
  });

  test("binary search success: value not found", () => {
    expect(
      binarysearch(
        [
          0, 4, 8, 12, 15, 18, 21, 25, 29, 34, 38, 42, 45, 47, 50, 54, 57, 60,
          63, 67,
        ],
        99,
      ),
    ).toBe(-1);
  });
});
