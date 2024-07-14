import subprocess
import shlex

THRESHOLD = 90.0


def diskspace_usage():
    with open("diskspace.txt", "w", encoding="utf-8") as f:
        # Get the column headings and data
        output = subprocess.check_output(["df", "-h"]).decode("utf-8").split("\n")
        col_head = output[0]
        data = output[2]

        col_headings = shlex.split(col_head)
        values = shlex.split(data)

        # Create dictionary of column headings and their values
        disk_info = dict(zip(col_headings, values))

        print(
            f"Current diskspace usage for filesystem: {disk_info["Filesystem"]} is {disk_info["Use%"]}..."
        )

        # Get the 'Use%' column heading/value and remove the '%' character. Convert to int in order to compare
        use_percentage = float(disk_info["Use%"].rstrip("%"))

        # Compare with the threshold
        if use_percentage > THRESHOLD:
            print("Threshold breached, email sys admin!!!")
        else:
            print("Diskspace usage is below 90%...👍️ ")


def main():
    diskspace_usage()


if __name__ == "__main__":
    main()
