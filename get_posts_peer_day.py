from read_data import fromJson
import datetime


def get_posts_peer_day(path,day:str)->int:
    """
    Return the number of posts for given day

    Args:
        data (dict): a dictionary of posts

    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    post = 0
    data=fromJson(path)['messages']   
    for i in data:
        x=i["date"].split('T')[0]
        if  x== day:
            post += 1

    return post
print(get_posts_peer_day('data/result.json','2022-09-30'))