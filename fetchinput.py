import requests
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] Missing the day of the challange.")
    else:
        if "AOC_SESSION" in os.environ:
            day_num = sys.argv[1]
            res = requests.get(
                f"https://adventofcode.com/2021/day/{day_num}/input",
                cookies={"session": os.environ["AOC_SESSION"]},
            )
            if res:
                with open("input.in", "wb") as f:
                    size = f.write(res.content)
                print(f"[!] Writing: {size}")
            else:
                print(f"[-] Error occured. {r.text}, {r.headers}")
        else:
            print("[!] Missing AOC_SESSION environment variable.")
