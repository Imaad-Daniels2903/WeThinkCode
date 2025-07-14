import requests
import sys


def main():
    api_key = "53d5253e24f8190a2b6622490c002cf719d647a2c217f3ee8466a1fe03ff1e9a"
    api_url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        cmdl_input = sys.argv
        bitcoins = float(cmdl_input[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")

    except IndexError:
        sys.exit("Missing command-line argument")

    else:
        try:
            response = requests.get(api_url)

        except requests.RequestException:
            sys.exit("Connection error")

        else:
            data = response.json()["data"]
            amount = float(data["priceUsd"]) * bitcoins
            print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
