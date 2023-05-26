from simple_salesforce import Salesforce
import yaml
import csv


def salesforce_download_to_computer():
    # 1 getting credentials from config file
    # CREDENTIALS NEEDS TO BE UPDATED

    try:
        with open("config.yaml") as file:
            config = yaml.safe_load(file)
            username = config['username']
            password = config['password']
            security_token = config['security_token']
    except Exception as e:
        print("1", e)
        return

    # 2 salesforce connection creation
    try:
        salesforce_connection = Salesforce(username=username, password=password, security_token=security_token)
        # print("session id: ", salesforce_connection.sessionId)
    except Exception as e:
        print("2", e)
        return

    # 3 query data
    try:
        with open("soql_query.txt") as file:
            query = file.read()
            # print(query)
        result = salesforce_connection.query_all(query)
        # print(result)
    except Exception as e:
        print("3", e)
        return

    # 4 Process the result
    try:
        records = result["records"]
        headers = set()
        # print("records", records)
        for record in records:
            headers.update(record.keys())
        # print("headers", headers)
    except Exception as e:
        print("4", e)
        return

    # 5 DATA download
    try:
        with open("accounts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(records)
    except Exception as e:
        print("5", e)
        return

    # 6 close the connection
    salesforce_instance = None


if __name__ == "__main__":
    salesforce_download_to_computer()