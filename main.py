from waapi import WaapiClient, CannotConnectToWaapiException
import csv
import pprint


def create_soundbank(client, item):
    try:
        args = {
            "parent": r"\SoundBanks\Default Work Unit",
            "type": "SoundBank",
            "name": f"NPC_{item}"
        }

        result = client.call("ak.wwise.core.object.create", args)
        pprint.pprint(result)
    except CannotConnectToWaapiException:
        print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")


def main():
    with open('list.csv', 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            for item in row:
                print(item)

                with WaapiClient() as client:
                    create_soundbank(client, item)


if __name__ == "__main__":
    main()
