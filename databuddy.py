import pandas as pd


def get_data():
    dfs = []
    page = 0
    while True:
        new_data = pd.read_json(
            f"https://data.cdc.gov/resource/9mfq-cb36.json?$limit=10000&$offset={10000*page}&$order=created_at"
        )
        if len(new_data):
            dfs.append(new_data)
            page += 1
        else:
            break
    return pd.concat(dfs)


def get_votes():
    return pd.read_csv(
        "./data-resources/StateAbbreviations.csv", index_col="Postalcode"
    ).join(
        pd.read_csv("./data-resources/state-electoral-2016.csv", index_col="State"),
        on="State",
    )
