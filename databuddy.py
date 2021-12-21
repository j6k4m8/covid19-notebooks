from typing import List, Union
import pandas as pd
from functools import cache


@cache
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


@cache
def get_states():
    return pd.read_csv(
        "./data-resources/StateAbbreviations.csv", index_col="Postalcode"
    ).join(
        pd.read_csv("./data-resources/state-electoral-2016.csv", index_col="State"),
        on="State",
    )


@cache
def get_votes(
    election_year: Union[int, List[int]] = 2020,
    all_parties: bool = False,
    pivot_by_state: bool = True,
) -> pd.DataFrame:
    """
    Get the votes for the given election year.
    """
    df = pd.read_csv("./data-resources/1976-2020-president.csv")
    year_inclusion = (
        df.year == election_year
        if isinstance(election_year, int)
        else df.year.isin(election_year)
    )
    df = (
        df[year_inclusion]
        .groupby(["year", "state", "party_simplified"])
        .sum()[["candidatevotes"]]
        .reset_index()
    )
    if not all_parties:
        df = df[df.party_simplified.isin(["DEMOCRAT", "REPUBLICAN"])]

    if not pivot_by_state:
        return df

    return df.pivot(
        index=["year", "state"], columns=["party_simplified"], values=["candidatevotes"]
    ).reset_index()
