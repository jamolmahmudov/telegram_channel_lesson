from read_data import fromJson
import datetime

def get_number_of_posts(data:dict)->int:
    """
    Return the number of posts for a given dictionary

    Args:
        data (dict): a dictionary of posts

    Returns: 
        int: the number of posts for the given dictionary
    """
    
    return len(data["messages"])
data = fromJson('data/result.json')
print(get_number_of_posts(data))