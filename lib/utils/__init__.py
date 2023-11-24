import pandas as pd
import os
import datetime
import time

def read_all_file(
    folder_path: str,
    prefix: str = "",
    suffix: str = "",
):
    """Read all files in this directory starting with prefix and ending with suffix
    Args:
        folder_path (str): Folder path to read files
        prefix (str): Prefix of file name. Defaults to "".
        suffix (str): Suffix of file name. Defaults to "".
    """
    df = pd.DataFrame()
    count_file = 0
    for file in os.listdir(folder_path):
        if file.startswith(prefix) and file.endswith(suffix):
            count_file += 1
            temp_df = pd.read_csv(os.path.join(folder_path, file))
            df = pd.concat([df, temp_df], ignore_index=True)
    return count_file, df

def save_data(
    data_list: list,
    type: str,
    folder_path: str,
):
    """Save data to csv file
    Args:
        data (list): List of data
        type (str): "posts", "comments", "sharers", "reactors"
        folder_path (str): Folder path to save data
    """
    df = pd.DataFrame(
        columns=data_list[0].keys(),
        index=range(len(data_list)),
        data=data_list,
    )
    now = datetime.datetime.utcnow()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(folder_path, f"{type}_{date_time}.csv")
    print(f"Save {type} data: ./{file_path}")
    df.to_csv(file_path, index=False)
    return df

def read_index_file(
    file_path: str,
):
    """Read index file: file .txt contains an integer
    Args:
        file_path (str): File path to read index file
    """
    try:
        with open(file_path, 'r') as f:
            i = f.read()
            if i:
                index = int(i)
            else:
                index = 0
    except Exception as e:
        print(e)
        print(f"Auto create file: ./{file_path}")
        # Create file if not exists
        with open(file_path, 'w') as f:
            f.write("0")
        index = 0
    return index

def write_index_file(
    file_path: str,
    index: int,
):
    """Write index file: file .txt contains an integer
    Args:
        file_path (str): File path to write index file
        index (int): Index to write
    """
    with open(file_path, 'w') as f:
        f.write(str(index))
    print(f'Save index {index} to resume: ./{file_path}'
)
    
def read_url_file(
    file_path: str,
):
    """Read url file: file .txt contains an url
    Args:
        file_path (str): File path to read url file
    """
    try:
        with open(file_path, 'r') as f:
            url = f.read()
    except Exception as e:
        print(e)
        # Create file if not exists
        print(f"Auto create file: ./{file_path}")
        with open(file_path, 'w') as f:
            f.write("")
        url = ""
    if url == "":
        url = None
    return url

def write_url_file(
    file_path: str,
    url: str,
):
    """Write url file: file .txt contains an url
    Args:
        file_path (str): File path to write url file
        url (str): Url to write
    """
    with open(file_path, 'w') as f:
        f.write(url)
    print(f'Save resume url: ./{file_path}'
)
    
def append_url_to_history(
    file_path: str,
    url: str,
):
    """Append url to history file: file .txt contains all urls
    Args:
        file_path (str): File path to append url to history file
        url (str): Url to append
    """
    with open(file_path, 'a') as f:
        f.write(url + '\n')
    print(f'Append resume url to history: ./{file_path}'
)
    
def sleep(seconds):
    """Sleep for seconds
    Args:
        seconds : Seconds to sleep
    """
    print(f"Sleep {seconds} seconds")
    time.sleep(seconds)

def get_post_id_list(
    df: pd.DataFrame,
    start: int,
    length: int,
):
    """Get post_id list from Post DataFrame starting from start and has length
    Args:
        df (pd.DataFrame): Dataframe to get post_id list
        start (int): Starting index
        length (int): Length of post_id list
    """
    if start < 0:
        start = 0
    if start > df.shape[0]:
        return []
    if start + length > df.shape[0]:
        return df.iloc[start:]['post_id'].to_list()
    return df.iloc[start:start+length]['post_id'].to_list()
