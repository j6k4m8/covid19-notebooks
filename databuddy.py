from typing import List, Union
import pandas as pd
from functools import cache
from joblib import Parallel, delayed


@cache
def get_data(N: int = 4):
    dfs = []
    # page = 0
    # while True:
    #     new_data = pd.read_json(
    #         f"https://data.cdc.gov/resource/9mfq-cb36.json?$limit=10000&$offset={10000*page}&$order=created_at"
    #     )
    #     if len(new_data):
    #         dfs.append(new_data)
    #         page += 1
    #     else:
    #         break

    # We can download pages in parallel using joblib. The catch is that we
    # need to check after every N jobs t see if we have any new data.
    page_start = 0
    while True:
        four_new_pages = Parallel(n_jobs=4)(
            delayed(pd.read_json)(
                f"https://data.cdc.gov/resource/9mfq-cb36.json?$limit=10000&$offset={10000*page}&$order=created_at"
            )
            for page in range(page_start, page_start + N)
        )
        dfs.extend(four_new_pages)
        # If each page is 10,000 elements long, we need to continue looping.
        # If ANY of the pages are shorter than 10,000, we can stop.
        if any(len(df) < 10000 for df in four_new_pages):
            break
        else:
            page_start += N
    # sort by date
    return pd.concat(dfs).sort_values("created_at")


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
