import argparse
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Convert a date between formats.")
    parser.add_argument("date", help="Date to convert")
    parser.add_argument("--input-format", default="%Y-%m-%d", help="Input format")
    parser.add_argument("--output-format", default="%d/%m/%Y", help="Output format")
    args = parser.parse_args()

    try:
        converted = datetime.strptime(args.date, args.input_format)
        print(converted.strftime(args.output_format))
    except ValueError as error:
        parser.error(f"Could not parse date: {error}")


if __name__ == "__main__":
    main()