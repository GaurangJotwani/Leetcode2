import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    emails = person.groupby('email').size().reset_index(name = 'num')

    duplicate_emails_df = emails[emails['num'] > 1][['email']]
    return duplicate_emails_df